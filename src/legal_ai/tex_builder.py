import os
import re
from pathlib import Path
from typing import Optional
from jinja2 import Environment, FileSystemLoader

from dataclasses import dataclass, field
from typing import List, Dict, Any

@dataclass
class SlideData:
    title: str = ""
    content_lines: List[str] = field(default_factory=list)
    images: List[str] = field(default_factory=list)
    latex_content: str = ""

def parse_markdown_slides(md_content: str) -> List[SlideData]:
    lines = md_content.splitlines()
    slides = []
    
    start_idx = 0
    frontmatter = {}
    if lines and lines[0].strip() == "---":
        start_idx = 1
        while start_idx < len(lines) and lines[start_idx].strip() != "---":
            line = lines[start_idx].strip()
            if ":" in line:
                key, val = line.split(":", 1)
                frontmatter[key.strip()] = val.strip().strip('"').strip("'")
            start_idx += 1
        start_idx += 1
        
    current_slide = SlideData()
    for line in lines[start_idx:]:
        if line.strip() == "---":
            if current_slide.title or current_slide.content_lines:
                slides.append(current_slide)
            current_slide = SlideData()
        elif line.strip().startswith("# ") and not current_slide.title:
            current_slide.title = re.sub(r'"([^"]*)"', r"``\1''", line.strip()[2:].strip().replace("&", r"\&"))
        elif line.strip().startswith("## ") and not current_slide.title:
            current_slide.title = re.sub(r'"([^"]*)"', r"``\1''", line.strip()[3:].strip().replace("&", r"\&"))
        else:
            current_slide.content_lines.append(line)
            
    if current_slide.title or current_slide.content_lines:
        slides.append(current_slide)
        
    return slides, frontmatter

def markdown_to_latex(content_lines: list[str]) -> str:
    """Converts a list of markdown lines (with bullets/numbers/formatting) to LaTeX syntax."""
    latex_lines = []
    level = -1
    in_table = False
    
    for raw_line in content_lines:
        line = raw_line
        if not line.strip():
            if not in_table and level < 0:
                latex_lines.append("")
            continue
        if "Notas del Mentor:" in line:
            continue
            
        # Protect image tags from text escaping
        img_placeholders = []
        def save_img(m):
            img_placeholders.append(m.group(0))
            return f"@@IMGPH{len(img_placeholders)-1}@@"
        
        clean = re.sub(r'!\[(.*?)\]\((.*?)\)', save_img, line)

        # Convert subheadings inside slide content (e.g. ## Subheading, ### Subheading) to bold text
        if clean.strip().startswith("#"):
            clean = re.sub(r'^\s*#+\s*(.*)', r'**\1**', clean)

        clean = re.sub(r'\*\*(.*?)\*\*', r'\\textbf{\1}', clean)
        clean = re.sub(r'__(.*?)__', r'\\textbf{\1}', clean)
        clean = re.sub(r'(?<!\*)\*(?!\s)(.*?)(?<!\s)\*(?!\*)', r'\\textit{\1}', clean)
        clean = re.sub(r'"([^"]*)"', r"``\1''", clean)
        
        # Handle inline code: `code`
        clean = re.sub(
            r'`([^`]+)`',
            lambda m: '\\texttt{' + m.group(1).replace('_', '\\_').replace('%', '\\%').replace('&', '\\&').replace('#', '\\#') + '}',
            clean
        )
        
        # Handle regular links: [text](url)
        clean = re.sub(r'(?<!!)\[([^\]]+)\]\(([^)]+)\)', r'\\href{\2}{\1}', clean)
        
        # Handle citations: [@citation]
        clean = re.sub(r'\[@(.*?)\]', r'\\cite{\1}', clean)
        
        # Handle special LaTeX characters (% & _ #) in plain text
        clean = clean.replace("%", "\\%").replace("&", "\\&").replace("#", "\\#")
        clean = re.sub(r'(?<!\\)_', r'\\_', clean)
        
        # Restore image tags with LaTeX figure syntax
        for idx, img_tag in enumerate(img_placeholders):
            m = re.match(r'!\[(.*?)\]\((.*?)\)', img_tag)
            if m:
                alt, path = m.group(1), m.group(2)
                tex_img = f'\\begin{{figure}}\\centering\\includegraphics[height=0.6\\textheight,keepaspectratio]{{{path}}}\\caption{{{alt}}}\\end{{figure}}'
                clean = clean.replace(f"@@IMGPH{idx}@@", tex_img)
        
        stripped = clean.strip()
        
        # Handle Markdown Tables
        if stripped.startswith("|") and stripped.endswith("|"):
            if "---" in stripped:
                continue
            cells = [c.strip() for c in stripped.strip('|').split('|')]
            if not in_table:
                in_table = True
                cols = " | ".join(["l"] * len(cells))
                latex_lines.append(r"\begin{table}")
                latex_lines.append(r"\resizebox{\textwidth}{!}{")
                latex_lines.append(rf"\begin{{tabular}}{{|{cols}|}}")
                latex_lines.append(r"\hline")
                latex_lines.append(" & ".join([f"\\textbf{{{c}}}" for c in cells]) + r" \\ \hline")
            else:
                latex_lines.append(" & ".join(cells) + r" \\ \hline")
            continue
        elif in_table:
            in_table = False
            latex_lines.append(r"\end{tabular}")
            latex_lines.append(r"}")
            latex_lines.append(r"\end{table}")
            
        list_match = re.match(r'^(\*|-|\d+\.)\s+(.*)', stripped)
        if list_match:
            # Calculate indentation for nested lists
            indent_count = len(line) - len(line.lstrip(' \t'))
            current_level = 1 if indent_count >= 2 or line.startswith('\t') else 0
            
            text = list_match.group(2).strip()
            
            # Open nested itemize
            while level < current_level:
                indent_str = "  " * (level + 1)
                latex_lines.append(f"{indent_str}\\begin{{itemize}}")
                level += 1
            # Close nested itemize
            while level > current_level:
                indent_str = "  " * level
                latex_lines.append(f"{indent_str}\\end{{itemize}}")
                level -= 1
                
            indent_str = "  " * (level + 1)
            latex_lines.append(f"{indent_str}\\item {text}")
        else:
            # Close all itemize environments if regular text is encountered
            while level >= 0:
                indent_str = "  " * level
                latex_lines.append(f"{indent_str}\\end{{itemize}}")
                level -= 1
            latex_lines.append(stripped)
            
    # Close any remaining itemize environments at the end of the slide
    while level >= 0:
        indent_str = "  " * level
        latex_lines.append(f"{indent_str}\\end{{itemize}}")
        level -= 1
        
    if in_table:
        latex_lines.append(r"\end{tabular}")
        latex_lines.append(r"}")
        latex_lines.append(r"\end{table}")
        
    return "\n".join(latex_lines)

def build_tex_deck(md_file_path: str, output_path: Optional[str] = None) -> Path:
    """
    Parses a Markdown file and generates a LaTeX Beamer presentation.
    Uses the beamer_template.tex.j2 in the templates folder.
    """
    if not output_path:
        output_path = str(Path(md_file_path).with_suffix('.tex'))
        
    with open(md_file_path, "r", encoding="utf-8") as f:
        md_content = f.read()

    # Reuse the markdown parser from the PPTX builder
    slides_data, frontmatter = parse_markdown_slides(md_content)
    
    # Process slides for LaTeX output
    presentation_title = frontmatter.get("title", "LegalAI Presentation")
    presentation_subtitle = frontmatter.get("subtitle", "")
    author = frontmatter.get("author", "Ricardo Reyes-Jimenez")
    institute = frontmatter.get("institute", "Universidad de La Sabana")
    background_image = frontmatter.get("background_image", "")
    
    processed_slides = []
    
    for idx, slide in enumerate(slides_data):
        if idx == 0 and ("Módulo" in slide.title or "Portada" in slide.title):
            # Try to extract subtitle/info from cover slide
            presentation_title = slide.title
            
            for line in slide.content_lines:
                if "Título:" in line or "Titulo:" in line:
                    presentation_title = line.split(":", 1)[1].strip().replace("**", "")
                elif "Subtítulo:" in line or "Subtitulo:" in line:
                    presentation_subtitle = line.split(":", 1)[1].strip().replace("**", "")
            
            presentation_short_title = presentation_title.split(":")[0] if ":" in presentation_title else presentation_title[:30]
            
            # The cover slide itself does not need a frame block in our template, 
            # because the template already has \begin{frame} \titlepage \end{frame}
            # So we skip adding it to processed_slides
            continue
            
        # Add latex_content property for Jinja
        slide.latex_content = markdown_to_latex(slide.content_lines)
        processed_slides.append(slide)
        
    # Check if slides already contain a references slide
    has_ref_slide = any(
        "referencia" in s.title.lower() or "bibliograf" in s.title.lower() or "reference" in s.title.lower()
        for s in processed_slides
    )
    
    # Check if a non-empty references.bib exists in client or current dir
    md_path = Path(md_file_path)
    client_refs = md_path.parent.parent / "references.bib" if md_path.parent.name == "original_documents" else Path.cwd() / "references.bib"
    
    if not client_refs.exists() and (Path.cwd() / "references.bib").exists():
        client_refs = Path.cwd() / "references.bib"
        
    has_bib_file = client_refs.exists() and client_refs.stat().st_size > 50

    show_bibtex = (not has_ref_slide) and has_bib_file

    # Setup Jinja environment with custom delimiters to avoid conflicting with LaTeX {}
    template_dir = Path(__file__).parent / "templates"
    env = Environment(
        loader=FileSystemLoader(template_dir),
        block_start_string='<%',
        block_end_string='%>',
        variable_start_string='<<',
        variable_end_string='>>',
        comment_start_string='<#',
        comment_end_string='#>',
        autoescape=False
    )
    
    template = env.get_template("beamer_template.tex.j2")
    
    rendered_tex = template.render(
        presentation_title=presentation_title,
        presentation_short_title=locals().get('presentation_short_title', presentation_title[:30]),
        presentation_subtitle=presentation_subtitle,
        author=author,
        institute=institute,
        background_image=background_image,
        slides=processed_slides,
        show_bibtex=show_bibtex
    )
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(rendered_tex)
        
    return Path(output_path)
