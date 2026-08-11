"""
Legal AI Prompt Templates & Frameworks
"""

from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field


class PromptFramework(BaseModel):
    name: str
    code: str
    description: str
    template: str
    example: str


FRAMEWORKS: Dict[str, PromptFramework] = {
    "care": PromptFramework(
        name="CARE Framework (Conceptos y Análisis)",
        code="CARE",
        description="Estructura estándar para solicitudes de análisis o conceptos jurídicos corporativos.",
        template="""[ROL]: Eres un {rol_legal} en la jurisdicción de {jurisdiccion}.
[CONTEXTO]: {contexto_hechos}
[ACCIÓN]: {accion_solicitada}
[RESULTADO ESPERADO]: {formato_resultado}
[EVALUACIÓN Y RESTRICCIONES]: {restricciones_legales}""",
        example="""[ROL]: Eres un abogado tributarista senior en Colombia.
[CONTEXTO]: Una empresa de software colombiana vende licencias SaaS a clientes en EE.UU.
[ACCIÓN]: Determina las implicaciones del impuesto sobre la renta y retención en la fuente.
[RESULTADO ESPERADO]: Memorando legal ejecutivo de máximo 3 páginas con recomendaciones.
[EVALUACIÓN Y RESTRICCIONES]: Cita únicamente el Estatuto Tributario colombiano vigente y doctrina de la DIAN."""
    ),
    "cot": PromptFramework(
        name="Chain-of-Thought (Ingeniería de Razonamiento)",
        code="COT",
        description="Desglose de pensamiento paso a paso para evitar alucinaciones en análisis jurídicos complejos.",
        template="""Analiza la siguiente situación jurídica desglosando tu razonamiento paso a paso antes de emitir cualquier conclusión final:

Situación: {situacion}

Pasos obligatorios de razonamiento:
1. Identifica las fuentes normativas y jurisprudenciales aplicables.
2. Analiza los elementos constitutivos de la figura jurídica en cuestión.
3. Contrasta los hechos materiales con cada uno de los elementos normativos.
4. Evalúa las excepciones o defensas aplicables.
5. Emite la conclusión y recomendación final.""",
        example="""Analiza si existe responsabilidad civil extracontractual en este accidente de tránsito corporativo desglosando tu razonamiento paso a paso..."""
    ),
    "tree_of_thought": PromptFramework(
        name="Tree-of-Thought (Estrategia Procesal Paralela)",
        code="TOT",
        description="Mapeo de múltiples vías defensivas o alternativas de solución con análisis de riesgo.",
        template="""Desarrolla 3 alternativas estratégicas distintas para resolver el siguiente problema legal:

Problema: {problema_legal}

Para cada una de las 3 alternativas, detalla:
a) Base normativa y argumentativa principal.
b) Riesgo probatorio y procesal (Bajo / Medio / Alto).
c) Probabilidad estimada de éxito y tiempos probables.
d) Impacto económico o reputacional para el cliente.""",
        example="""Desarrolla 3 alternativas estratégicas procesales ante un pliego de cargos formulado por la Superintendencia de Industria y Comercio (SIC)..."""
    ),
    "red_team": PromptFramework(
        name="Red Teaming Legal (Validación Cruzada)",
        code="RED_TEAM",
        description="Auto-crítica y auditoría del borrador desde la perspectiva de la contraparte o del juez.",
        template="""Actúa como el abogado litigante de la contraparte ({contraparte}).
Revisa y audita el siguiente borrador de respuesta:

Borrador:
{borrador_texto}

Identifica:
1. Las 3 principales debilidades o vacíos argumentativos.
2. La mejor objeción probatoria que formularías.
3. Cómo reforzarías el documento para hacerlo blindado.""",
        example="""Actúa como el apoderado de la parte demandante e identifica las debilidades en nuestra contestación de demanda..."""
    )
}


def get_framework(code: str) -> Optional[PromptFramework]:
    """Retrieve framework by code (case-insensitive)."""
    return FRAMEWORKS.get(code.lower())


def list_frameworks() -> List[PromptFramework]:
    """List all available legal prompt frameworks."""
    return list(FRAMEWORKS.values())
