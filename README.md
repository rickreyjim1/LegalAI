# LegalAI - Estrategia y Aplicación de IA en el Derecho

Un toolkit profesional y conjunto de cursos para abogados, firmas y profesionales del derecho que buscan integrar Inteligencia Artificial en sus procesos de trabajo.

## 🚀 Características
- **Módulos Educativos:** Diapositivas y contenido estructurado en Markdown (`modulo1.md`, `modulo2.md`, etc.).
- **Compilador Beamer / LaTeX:** Generación automatizada de presentaciones PDF profesionales vía MikTeX (`pdflatex`).
- **Live Recompilation (`--watch`):** Monitoreo reactivo de archivos en tiempo real para previsualización inmediata.
- **Frameworks de Prompting:** Plantillas para CARE, Chain-of-Thought, Tree-of-Thought, y Red-Teaming Legal.
- **Multi-Agent Orchestrator:** Generación de diapositivas con agentes especializados (Reader, Scraper, Writer, Validator).

## 🛠️ Instalación y Configuración

```bash
# 1. Crear el entorno virtual con Python 3.12+
py -3.12 -m venv .venv

# 2. Activar el entorno virtual (Windows PowerShell)
.\.venv\Scripts\Activate.ps1

# 3. Instalar dependencias y el paquete en modo editable
pip install -e .
```

## 📋 Uso de la CLI

```bash
# Ver comandos y opciones disponibles
legal-ai --help

# Ver resumen del estado del proyecto y módulos registrados
legal-ai info

# Compilar una presentación Markdown a PDF (Beamer / LaTeX)
legal-ai build-pdf original_documents/modulo1.md

# ⚡ Compilar y monitorear cambios en tiempo real con el parámetro --watch (-w)
# Cualquier cambio guardado en el archivo recompilará el PDF automáticamente
legal-ai build-pdf original_documents/modulo1.md --watch

# Monitorear un directorio completo de archivos Markdown
legal-ai watch original_documents/

# Generar únicamente el código fuente LaTeX (.tex)
legal-ai build-tex original_documents/modulo1.md

# Generar una presentación completa con el pipeline de agentes multi-rol
legal-ai generate "IA y Secreto Profesional en Litigio" -o original_documents/secreto_ia.md

# Consultar frameworks de Legal Prompting
legal-ai prompt list
legal-ai prompt show care
```
