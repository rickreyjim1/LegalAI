# LegalAI - Estrategia y Aplicación de IA en el Derecho

Un toolkit profesional y conjunto de cursos para abogados, firmas y profesionales del derecho que buscan integrar Inteligencia Artificial en sus procesos de trabajo.

## 🚀 Características
- **Módulos Educativos:** Diapositivas y contenido estructurado en Markdown (`modulo1.md`, `modulo2.md`, etc.).
- **CLI (`legal-ai`):** Herramienta de línea de comandos para compilar diapositivas a PowerPoint (`.pptx`) e interactuar con plantillas de Prompting Legal.
- **Frameworks de Prompting:** Plantillas para CARE, Chain-of-Thought, Tree-of-Thought, y Red-Teaming Legal.

## 🛠️ Instalación y Configuración

```bash
# 1. Crear el entorno virtual con Python 3.12+
py -3.14 -m venv .venv

# 2. Activar el entorno virtual (Windows PowerShell)
.\.venv\Scripts\Activate.ps1

# 3. Instalar dependencias y el paquete en modo editable
pip install -e .
```

## 📋 Uso de la CLI

```bash
# Ver comandos disponibles
legal-ai --help

# Ver resumen del estado del proyecto
legal-ai info

# Generar presentación PowerPoint a partir de un módulo Markdown
legal-ai build-deck modulo1.md --output modulo1_presentacion.pptx

# Mostrar plantillas de Legal Prompting
legal-ai prompt list
```
