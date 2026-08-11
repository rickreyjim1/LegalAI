import os
import sys
from pathlib import Path
import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from legal_ai import __version__
from legal_ai.tex_builder import build_tex_deck
from legal_ai.prompts import list_frameworks, get_framework

console = Console()


@click.group()
@click.version_option(version=__version__, prog_name="LegalAI CLI")
def main():
    """LegalAI - Toolkit de Estrategia y Aplicación de IA en el Derecho."""
    pass


@main.command(name="info")
def project_info():
    """Muestra el estado del entorno y los módulos del curso LegalAI."""
    console.print(Panel.fit("[bold blue]LegalAI - Toolkit & Cursos de IA Legal[/bold blue]", subtitle=f"v{__version__}"))

    table = Table(title="Módulos del Curso Registrados")
    table.add_column("Archivo", style="cyan")
    table.add_column("Estado", style="green")
    table.add_column("Ruta Absolute", style="dim")

    workspace = Path.cwd()
    modules = ["modulo1.md", "modulo2.md", "modulo3.md", "modulo4.md"]

    for mod in modules:
        mod_path = workspace / "original_documents" / mod
        status = "Existe" if mod_path.exists() else "Pendiente"
        color = "green" if mod_path.exists() else "yellow"
        table.add_row(mod, f"[{color}]{status}[/{color}]", str(mod_path))

    console.print(table)
    console.print(f"\n[bold]Entorno Python:[/bold] {sys.version.split()[0]}")
    console.print(f"[bold]Directorio de Trabajo:[/bold] {workspace}")



@main.command(name="build-tex")
@click.argument("input_file", type=click.Path(exists=True, path_type=Path))
@click.option("--output", "-o", type=click.Path(path_type=Path), help="Ruta del archivo de salida (.tex).")
def build_tex(input_file: Path, output: Path):
    """Compila un archivo Markdown de curso a una presentación LaTeX Beamer (.tex)."""
    decks_dir = Path.cwd() / "decks"
    decks_dir.mkdir(exist_ok=True)
    if not output:
        output = decks_dir / input_file.with_suffix(".tex").name

    console.print(f"[bold yellow]Compilando LaTeX desde:[/bold yellow] {input_file.name}")

    try:
        out_path = build_tex_deck(md_file_path=str(input_file), output_path=str(output))
        console.print(f"[bold green][OK] Código fuente LaTeX generado exitosamente:[/bold green] {out_path}")
        console.print(f"[dim]Recuerda compilar el archivo {out_path.name} usando pdflatex o subirlo a Overleaf.[/dim]")
    except Exception as e:
        console.print(f"[bold red]Error al generar archivo LaTeX:[/bold red] {e}")
        sys.exit(1)


@main.command(name="build-pdf")
@click.argument("input_file", type=click.Path(exists=True, path_type=Path))
@click.option("--output", "-o", type=click.Path(path_type=Path), help="Ruta del archivo de salida (.pdf).")
def build_pdf(input_file: Path, output: Path):
    """Compila un archivo Markdown de curso a una presentación PDF vía MikTeX (pdflatex)."""
    import subprocess
    import shutil
    
    decks_dir = Path.cwd() / "decks"
    decks_dir.mkdir(exist_ok=True)
    
    tex_output = decks_dir / input_file.with_suffix(".tex").name
    if not output:
        output = decks_dir / input_file.with_suffix(".pdf").name

    console.print(f"[bold yellow]1. Generando LaTeX desde:[/bold yellow] {input_file.name}")
    try:
        out_path = build_tex_deck(md_file_path=str(input_file), output_path=str(tex_output))
        console.print(f"[bold green][OK] Código fuente LaTeX generado:[/bold green] {out_path}")
    except Exception as e:
        console.print(f"[bold red]Error al generar archivo LaTeX:[/bold red] {e}")
        sys.exit(1)
        
    console.print(f"[bold yellow]2. Compilando PDF usando pdflatex...[/bold yellow]")
    try:
        # We run pdflatex twice and bibtex in between if references exist
        # Need to run in the decks_dir so auxiliary files are generated there
        subprocess.run(["pdflatex", "-interaction=nonstopmode", tex_output.name], cwd=decks_dir, check=True, capture_output=True)
        # Check if references.bib exists in the root folder, if so copy it to decks temporarily
        refs = Path.cwd() / "references.bib"
        if refs.exists():
            shutil.copy(refs, decks_dir / "references.bib")
            console.print(f"[bold yellow]3. Procesando referencias con bibtex...[/bold yellow]")
            subprocess.run(["bibtex", tex_output.stem], cwd=decks_dir, check=False, capture_output=True)
            subprocess.run(["pdflatex", "-interaction=nonstopmode", tex_output.name], cwd=decks_dir, check=True, capture_output=True)
            subprocess.run(["pdflatex", "-interaction=nonstopmode", tex_output.name], cwd=decks_dir, check=True, capture_output=True)
            
        console.print(f"[bold green][OK] PDF generado exitosamente:[/bold green] {output.name}")
    except subprocess.CalledProcessError as e:
        console.print(f"[bold red]Error en la compilación de MikTeX:[/bold red]\n{e.output.decode('utf-8', errors='ignore')}")
        sys.exit(1)
    except FileNotFoundError:
        console.print(f"[bold red]Error: No se encontró 'pdflatex'. Asegúrate de que MikTeX esté instalado y en el PATH del sistema.[/bold red]")
        sys.exit(1)


@main.command(name="watch")
@click.argument("directory", type=click.Path(exists=True, path_type=Path))
def watch(directory: Path):
    """Monitorea archivos Markdown y recompila automáticamente los PDFs."""
    import time
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
    
    class MarkdownChangeHandler(FileSystemEventHandler):
        def __init__(self):
            self.last_run = 0
            
        def on_modified(self, event):
            if not event.is_directory and event.src_path.endswith(".md"):
                current_time = time.time()
                if current_time - self.last_run > 1.0:
                    self.last_run = current_time
                    file_path = Path(event.src_path)
                    console.print(f"\n[bold magenta]¡Cambio detectado![/bold magenta] Recompilando: {file_path.name}")
                    try:
                        import subprocess
                        subprocess.run([sys.executable, "-m", "legal_ai.cli", "build-pdf", str(file_path)], check=True)
                        console.print("[bold green][OK] Recompilación completada automáticamente.[/bold green]\n")
                    except subprocess.CalledProcessError:
                        console.print("[bold red][ERROR] Fallo durante la recompilación automática.[/bold red]\n")

    event_handler = MarkdownChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, str(directory), recursive=False)
    observer.start()
    
    console.print(f"[bold cyan][WATCH] Monitoreando cambios en:[/bold cyan] {directory}")
    console.print("[dim]Presiona Ctrl+C para detener.[/dim]")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
        console.print("\n[yellow]Monitoreo detenido.[/yellow]")
    observer.join()


@main.group(name="prompt")
def prompt_group():
    """Herramientas de Prompt Engineering Legal (CARE, CoT, Red-Teaming)."""
    pass


@prompt_group.command(name="list")
def prompt_list():
    """Lista las plantillas y frameworks de Prompting Legal disponibles."""
    table = Table(title="Frameworks de Prompting Legal")
    table.add_column("Código", style="bold cyan")
    table.add_column("Nombre", style="bold white")
    table.add_column("Descripción", style="dim")

    for fw in list_frameworks():
        table.add_row(fw.code, fw.name, fw.description)

    console.print(table)


@prompt_group.command(name="show")
@click.argument("code")
def prompt_show(code: str):
    """Muestra la estructura y ejemplo de un framework específico (Ej. care, cot, tot, red_team)."""
    fw = get_framework(code)
    if not fw:
        console.print(f"[bold red]Framework '{code}' no encontrado.[/bold red] Usa 'legal-ai prompt list' para ver los disponibles.")
        return

    console.print(Panel(fw.template, title=f"[bold green]{fw.name} - Plantilla[/bold green]"))
    console.print(Panel(fw.example, title=f"[bold blue]Ejemplo Práctico en Derecho[/bold blue]"))


if __name__ == "__main__":
    main()
