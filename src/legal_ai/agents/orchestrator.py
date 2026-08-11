import os
import subprocess
from pathlib import Path

try:
    from crewai import Agent, Task, Crew, Process
    from langchain_google_genai import ChatGoogleGenerativeAI
    from .tools import web_search_tool, rag_search_tool, image_generation_tool
    HAS_CREWAI = True
except ImportError:
    HAS_CREWAI = False

def create_agents():
    llm = "gemini/gemini-2.5-flash"
    
    researcher = Agent(
        role='Senior Legal Tech Researcher',
        goal='Find authoritative academic references, recent case laws, and local jurisprudence regarding {topic}',
        backstory='You are an expert legal researcher working in a top-tier law firm in Colombia. You excel at finding precise citations in both local laws and global academic databases.',
        verbose=True,
        allow_delegation=False,
        llm=llm,
        tools=[web_search_tool, rag_search_tool]
    )

    writer = Agent(
        role='Expert Instructional Designer',
        goal='Draft highly engaging, fun, and educational Beamer Markdown presentations in Spanish.',
        backstory='You are a charismatic professor of law and technology. You transform dry legal topics into exciting, storytelling-driven lectures that captivate your audience.',
        verbose=True,
        allow_delegation=False,
        llm=llm
    )
    
    designer = Agent(
        role='Creative Visual Designer',
        goal='Analyze the presentation draft, generate stunning relevant AI images, and insert their paths into the Markdown.',
        backstory='You are a world-class graphic designer who visualizes abstract legal concepts into engaging illustrations. You know exactly what prompt to use to generate the perfect image.',
        verbose=True,
        allow_delegation=False,
        llm=llm,
        tools=[image_generation_tool]
    )
    
    return researcher, writer, designer

def create_tasks(researcher, writer, designer, topic, output_md_path):
    research_task = Task(
        description=f'Search for recent academic papers and local PDF context (if available) regarding: {topic}. Extract 3-5 high quality, real references and fun facts.',
        expected_output='A detailed research brief containing real academic citations, DOIs, and 2 interesting facts to use in the presentation.',
        agent=researcher
    )

    write_task = Task(
        description=f'''Using the research brief, write a complete Beamer presentation in Markdown format (using `revealjs` frontmatter) in SPANISH about: {topic}.

Guidelines:
1. Make the content extremely ENGAGING and FUN.
2. Use storytelling and interactive questions for the audience.
3. Include a "Sabias que..." (Did you know) section using the references provided by the researcher.
4. Include a References section at the end with real citations.
5. Provide suggestions for where images should go using exactly this syntax: `[IMAGE_NEEDED: Describe the visual concept here|suggested_filename.png]`
6. Use citations if necessary like `[@cita]`.

Format strictly in Markdown suitable for pandoc/Beamer conversion. Do not include markdown code block backticks (```markdown) in your final output, just output the raw text.''',
        expected_output='A complete, engaging Markdown file ready for Beamer compilation with image placeholders.',
        agent=writer
    )
    
    design_task = Task(
        description='''Review the drafted Markdown presentation.
1. Find all `[IMAGE_NEEDED: prompt|filename.png]` tags.
2. For each tag, use your Image Generation Tool. Pass exactly "prompt|filename.png" to the tool.
3. Replace the `[IMAGE_NEEDED...]` tag with a standard Markdown image link pointing to `Images/filename.png` like so: `![Image Description](Images/filename.png)`
4. Output the final, perfectly formatted Markdown presentation containing all the new image links. Do not include markdown code block backticks.''',
        expected_output='The final Markdown presentation with image placeholders fully resolved to downloaded images.',
        agent=designer,
        output_file=str(output_md_path)
    )
    
    return [research_task, write_task, design_task]

def renderer_agent(md_path: Path) -> Path:
    """Automatically invokes local MikTeX (pdflatex) via the legal-ai CLI."""
    print("[Renderer Agent] Compiling PDF via MikTeX...")
    try:
        subprocess.run(["legal-ai", "build-pdf", str(md_path)], check=True)
        pdf_name = md_path.with_suffix(".pdf").name
        pdf_path = Path.cwd() / "decks" / pdf_name
        if pdf_path.exists():
            print(f"[SUCCESS] Renderer Agent successfully generated: {pdf_path}")
            return pdf_path
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Renderer Agent Failed: {e}")
    return None

def run_pipeline(raw_material_path: str, output_md_name: str):
    from dotenv import load_dotenv
    load_dotenv(override=True)
    
    # Map GEMINI_API_KEY to GOOGLE_API_KEY if needed
    if os.environ.get("GEMINI_API_KEY"):
        os.environ["GOOGLE_API_KEY"] = os.environ.get("GEMINI_API_KEY")
    
    print("[INFO] Starting LegalAI Multi-Agent Pipeline (Powered by CrewAI)...\n")
    if not os.environ.get("GOOGLE_API_KEY"):
        print("[WARN] No se encontro GOOGLE_API_KEY o GEMINI_API_KEY. Los agentes no podran funcionar correctamente.")
        return
        
    if not HAS_CREWAI:
        print("[WARN] CrewAI not installed. Please run pip install -r requirements.txt.")
        return
        
    topic = Path(raw_material_path).read_text(encoding='utf-8') if Path(raw_material_path).exists() else raw_material_path
    
    researcher, writer, designer = create_agents()
    tasks = create_tasks(researcher, writer, designer, topic, Path(output_md_name))
    
    crew = Crew(
        agents=[researcher, writer, designer],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )
    
    # Execute the Crew
    result = crew.kickoff()
    print("[SUCCESS] CrewAI Generation Complete!")
    
    # Render the result
    renderer_agent(Path(output_md_name))

if __name__ == "__main__":
    Path("original_documents").mkdir(exist_ok=True)
    Path("original_documents/pdf_library").mkdir(exist_ok=True)
    
    # For testing:
    run_pipeline("El impacto de la Inteligencia Artificial en el Derecho Laboral Colombiano", "original_documents/modulo_laboral_final.md")
