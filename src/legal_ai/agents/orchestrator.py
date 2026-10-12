import os
import re
import subprocess
from pathlib import Path

try:
    from crewai import Agent, Task, Crew, Process
    from .tools import web_search_tool, rag_search_tool
    HAS_CREWAI = True
except ImportError:
    HAS_CREWAI = False


def create_agents(expertise: str = "Senior Researcher"):
    llm = "gemini/gemini-2.5-flash"

    researcher = Agent(
        role=f"Senior Domain Researcher ({expertise})",
        goal="Find authoritative academic references, empirical evidence, state-of-the-art developments, and key literature regarding {topic}",
        backstory=f"You are a world-class researcher and subject-matter expert with deep domain knowledge as a {expertise}. You excel at analyzing literature, synthesizing complex topics, and extracting high-impact academic citations.",
        verbose=True,
        allow_delegation=False,
        llm=llm,
        tools=[web_search_tool, rag_search_tool],
    )

    writer = Agent(
        role=f"Master Instructional Designer ({expertise})",
        goal="Draft highly professional, clear, structured, and educational Beamer Markdown presentations in Spanish with practical exercises.",
        backstory=f"You are a top-tier educator, professor, and instructional designer specializing in {expertise}. You excel at breaking down complex topics into clear slides, practical audience exercises, interactive questions, and structured lessons.",
        verbose=True,
        allow_delegation=False,
        llm=llm,
    )

    return researcher, writer


def create_tasks(researcher, writer, topic: str, output_md_path: Path, expertise: str = "Senior Researcher"):
    research_task = Task(
        description=f"""Conduct thorough research regarding: "{topic}" from the perspective of a {expertise}.
Find 3-5 high quality academic references, empirical findings, DOIs, and 2-3 key takeaways or surprising facts.""",
        expected_output="A comprehensive research brief with citations, key evidence, and domain-specific insights.",
        agent=researcher,
    )

    write_task = Task(
        description=f"""Using the research brief, write a complete, highly professional Beamer presentation in Markdown format (using `revealjs` frontmatter) in SPANISH about: "{topic}".

Guidelines:
1. Target Audience: Professional audience / General public.
2. Perspective & Tone: Professional, authoritative yet accessible, embodying the expertise of a {expertise}.
3. NO images or image placeholders needed. Focus entirely on clear slide structure, clean text formatting, and high-value educational content.
4. Structure the presentation slides cleanly using `---` dividers:
   - Slide 1: Cover slide with Title, Subtitle, Author, and Institute.
   - Slide 2: Objetivos de la sesión y Contexto General.
   - Slide 3-5: Marco Conceptual y Conceptos Clave (con viñetas claras y explicativas).
   - Slide 6-7: Casos de Estudio y Ejemplos Prácticos Aplicados.
   - Slide 8-9: Ejercicios Prácticos y Actividades Interactivas (paso a paso para el público).
   - Slide 10: "Sabías que..." / Datos Curiosos respaldados por la investigación.
   - Slide 11: Conclusiones y Puntos Clave (Takeaways).
   - Slide 12: Referencias Bibliográficas (en formato académico IEEE/APA con DOIs si están disponibles).
5. Format strictly in clean Markdown suitable for Pandoc/Beamer LaTeX conversion.
6. Do NOT include markdown code block backticks (```markdown) in your final output, output only raw markdown text.""",
        expected_output="A complete, professional Markdown presentation file ready for Beamer compilation.",
        agent=writer,
        output_file=str(output_md_path),
    )

    return [research_task, write_task]


def renderer_agent(md_path: Path) -> Path:
    """Automatically invokes local MikTeX (pdflatex) via the legal-ai CLI."""
    import sys
    print("[Renderer Agent] Compiling PDF via MikTeX...")
    try:
        subprocess.run([sys.executable, "-m", "legal_ai.cli", "build-pdf", str(md_path)], check=True)
        input_dir = md_path.parent
        if input_dir.name == "original_documents":
            decks_dir = input_dir.parent / "decks"
        else:
            decks_dir = Path.cwd() / "decks"
        pdf_name = md_path.with_suffix(".pdf").name
        pdf_path = decks_dir / pdf_name
        if pdf_path.exists():
            print(f"[SUCCESS] Renderer Agent successfully generated: {pdf_path}")
            return pdf_path
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Renderer Agent Failed: {e}")
    return None


def parse_topic_and_expertise(topic_raw: str, expertise_param: str = None) -> tuple[str, str]:
    """
    Parses topic string for embedded Expertise: or Role: prefixes if present.
    Supports format: 'Expertise: Journalist | Topic: Data Analysis'
    """
    expertise = expertise_param or "Senior Researcher"
    topic = topic_raw.strip()

    if "expertise:" in topic.lower():
        match = re.search(r'expertise\s*:\s*([^,|\n]+)', topic, re.IGNORECASE)
        if match:
            expertise = match.group(1).strip()
            topic = re.sub(r'expertise\s*:\s*[^,|\n]+[,|\n]?', '', topic, flags=re.IGNORECASE).strip()

    if "topic:" in topic.lower():
        match = re.search(r'topic\s*:\s*(.+)', topic, re.IGNORECASE | re.DOTALL)
        if match:
            topic = match.group(1).strip()

    return topic, expertise


def run_pipeline(arg1: str, arg2: str = None, arg3: str = None, expertise: str = None):
    """
    Flexible multi-agent orchestrator pipeline runner.
    Supports signatures:
    - run_pipeline(topic, output_md_name, expertise="...")
    - run_pipeline("Expertise: Journalist", topic, output_md_name)
    """
    from dotenv import load_dotenv
    load_dotenv(override=True)

    if os.environ.get("GEMINI_API_KEY"):
        os.environ["GOOGLE_API_KEY"] = os.environ.get("GEMINI_API_KEY")

    print("[INFO] Starting LegalAI Multi-Agent Pipeline (Powered by CrewAI)...\n")
    if not os.environ.get("GOOGLE_API_KEY"):
        print("[WARN] No se encontró GOOGLE_API_KEY o GEMINI_API_KEY. Los agentes no podrán funcionar correctamente.")
        return

    if not HAS_CREWAI:
        print("[WARN] CrewAI not installed. Please run pip install -r requirements.txt.")
        return

    # Determine positional arguments
    if arg3 and arg3.endswith(".md"):
        exp_input = arg1
        topic_input = arg2
        output_md_name = arg3
        if "expertise:" in exp_input.lower():
            parsed_exp = exp_input.split(":", 1)[1].strip()
        else:
            parsed_exp = exp_input
        topic, current_expertise = parse_topic_and_expertise(topic_input, parsed_exp)
    else:
        topic_input = arg1
        output_md_name = arg2 or "original_documents/presentation.md"
        topic, current_expertise = parse_topic_and_expertise(topic_input, expertise)

    output_path = Path(output_md_name)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"[INFO] Expertise Persona: {current_expertise}")
    print(f"[INFO] Topic: {topic}")
    print(f"[INFO] Target Output Markdown: {output_path}\n")

    researcher, writer = create_agents(current_expertise)
    tasks = create_tasks(researcher, writer, topic, output_path, current_expertise)

    crew = Crew(
        agents=[researcher, writer],
        tasks=tasks,
        process=Process.sequential,
        verbose=True,
    )

    result = crew.kickoff()
    print("\n[SUCCESS] CrewAI Content Generation Complete!")

    # Render PDF via local MikTeX / pdflatex
    renderer_agent(output_path)


if __name__ == "__main__":
    Path("original_documents").mkdir(exist_ok=True)
    Path("original_documents/pdf_library").mkdir(exist_ok=True)

    run_pipeline(
        "Análisis de datos y toma de decisiones usando IA para público en general",
        "clients/Capgemini/original_documents/analisis_de_datos.md",
        expertise="PhD in Medicine",
    )
