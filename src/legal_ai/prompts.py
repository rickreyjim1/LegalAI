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
    "adp": PromptFramework(
        name="ADP Framework (Auditoría Contractual y Due Diligence)",
        code="ADP",
        description="Especializado en revisión de contratos, due diligence y detección de cláusulas leoninas o de riesgo.",
        template="""[ACTOR]: Eres el apoderado legal de la parte {posicion_cliente} (ej. Comprador / Arrendatario / Empleador).
[DOCUMENTO]: {tipo_documento_o_clausula}
[PROPÓSITO]:
1. Identifica cláusulas que impongan obligaciones asimétricas, penalidades desproporcionadas o riesgos ocultos para mi cliente.
2. Evalúa topes de indemnidad, causales de terminación anticipada y ley aplicable.
3. Para cada riesgo detectado, redacta una propuesta de redacción alternativa justa y equilibrada.

Documento a Auditar:
{texto_documento}""",
        example="""[ACTOR]: Eres el abogado de la Empresa Compradora.
[DOCUMENTO]: Revisa el contrato de suministro y SLA adjunto.
[PROPÓSITO]: Identifica penalidades unilaterales, extensiones de plazo sin compensación y limitaciones de responsabilidad del proveedor. Propón cláusulas de reemplazo en formato tabla comparativa."""
    ),
    "tam": PromptFramework(
        name="TAM Framework (Redacción y Comunicación Legal)",
        code="TAM",
        description="Diseñado para redactar correspondencia formal, cobros extrajudiciales, memoriales y comunicación con clientes.",
        template="""[TAREA]: {objetivo_comunicacion} (ej. cobro extrajudicial, respuesta a requerimiento, comunicación a socios).
[AUDIENCIA]: {destinatario_y_relacion} (ej. contraparte comercial clave, entidad de control, cliente institucional).
[MÉTODO]: Canal: {canal} | Tono: {tono_estilo} | Marco de Negociación: {limite_negociacion}.

Instrucciones Específicas:
{detalles_instruccion}""",
        example="""[TAREA]: Redactar un requerimiento de cobro por mora de 90 días en cánones de arrendamiento comercial.
[AUDIENCIA]: Representante legal de la empresa arrendataria (relación comercial histórica de 5 años que deseamos preservar).
[MÉTODO]: Correo electrónico formal y persuasivo; tono asertivo pero conciliador; citando el contrato y ofreciendo una mesa de acuerdo de pago en un plazo de 5 días hábiles."""
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
4. Evalúa las excepciones, defensas o causales de exoneración aplicables.
5. Emite la conclusión y recomendación procesal final.""",
        example="""Analiza si se configuran los elementos de responsabilidad civil extracontractual por daño ambiental en este caso de derrame industrial, evaluando nexo causal, daño cierto y culpa probada paso a paso antes de emitir conclusiones."""
    ),
    "tot": PromptFramework(
        name="Tree-of-Thought (Estrategia Procesal Paralela)",
        code="TOT",
        description="Mapeo de múltiples vías procesales o defensivas alternativas con análisis comparativo de riesgo y viabilidad.",
        template="""Desarrolla 3 alternativas estratégicas distintas para resolver el siguiente problema legal:

Problema Legal: {problema_legal}

Para cada una de las 3 alternativas, detalla de forma independiente:
a) Tesis jurídica principal y soporte normativo.
b) Nivel de riesgo probatorio y procesal (Bajo / Medio / Alto).
c) Probabilidad estimada de éxito y tiempos procesales probables.
d) Impacto económico, operativo o reputacional para el cliente.
e) Matriz resumen comparativa final recomendando la mejor opción.""",
        example="""Desarrolla 3 alternativas estratégicas defensivas ante un pliego de cargos formulado por la Superintendencia de Industria y Comercio (SIC) por presunta infracción a la libre competencia: 1) Garantías y compromisos anticipados, 2) Excepción de prescripción y nulidad, 3) Defensa de fondo en descargos probatorios."""
    ),
    "irac": PromptFramework(
        name="IRAC / CRAC (Subsunción Jurídica Universal)",
        code="IRAC",
        description="Estructura formal internacional para conceptos, dictámenes jurídicos y alegatos de conclusión.",
        template="""Estructura tu análisis jurídico siguiendo estrictamente el estándar IRAC:

[ISSUE / PROBLEMA JURÍDICO]: Formula con precisión la pregunta jurídica central a resolver.
[RULE / REGLA DE DERECHO]: Identifica las normas vigentes, principios generales y precedentes jurisprudenciales vinculantes.
[APPLICATION / ANÁLISIS DE SUBSUNCIÓN]: Aplica la regla jurídica identificada a los hechos fácticos concretos del caso.
[CONCLUSION / DICTAMEN FINAL]: Emite una respuesta contundente al problema planteado y los pasos de mitigación recomendados.

Caso a Analizar:
{caso_concreto}""",
        example="""[ISSUE]: ¿Vulnera el empleador la estabilidad laboral reforzada al desvincular a un empleado con recomendación médica sin autorización del MinTrabajo?
[RULE]: Cita el artículo 26 de la Ley 361 de 1997 y la jurisprudencia unificada de la Corte Constitucional (SU-049/17 y SL de la Corte Suprema).
[APPLICATION]: Subsume el caso de terminación con indemnización frente al conocimiento previo de la patología por el empleador.
[CONCLUSION]: Determina el riesgo de reintegro y pago de 180 días de salario."""
    ),
    "grounding": PromptFramework(
        name="Grounding Blindado (Circuito Cerrado Anti-Alucinación)",
        code="GROUNDING",
        description="Forzar al modelo a operar exclusivamente con base en la evidencia y textos suministrados, prohibiendo invenciones.",
        template="""[ROL]: Eres un auditor judicial y analista de expedientes estricto.
[INSTRUCCIÓN]: Responde las preguntas formuladas basándote ÚNICA Y EXCLUSIVAMENTE en el texto del expediente adjunto.
[RESTRICCIONES INFRANQUEABLES]:
1. Si una respuesta no se encuentra taxativamente en el documento, responde exactamente: 'Dato no verificable en el expediente suministrado'.
2. Tienes estrictamente prohibido asumir hechos, extrapolar intenciones de las partes o inventar números de radicado, fechas o artículos de ley.
3. Para cada afirmación fáctica, cita la página y párrafo exacto de donde fue extraída.

Expediente / Documento:
{documento_fuente}

Preguntas a Responder:
{cuestionario}""",
        example="""Audita el siguiente contrato de arrendamiento. Si no encuentras una cláusula expresa sobre subarriendo o cesión, declara 'Dato no verificable en el contrato' y bajo ninguna circunstancia asumas la regla del Código Civil."""
    ),
    "blueprint": PromptFramework(
        name="Blueprint Institucional (Los 5 Pilares de la PromptLibrary)",
        code="BLUEPRINT",
        description="Estructura estándar de la firma para registrar y compartir prompts reutilizables con variables delimitadas en corchetes [ ].",
        template="""# BLUEPRINT MAESTRO: {titulo_blueprint}
- Código Oficial: [PL-{area_practica}-{codigo}]
- Autor / Certificado por: [Nombre / Comité de IA]
- Modelos Certificados: [GPT-4o / Claude 3.5 Sonnet / Gemini Pro]

1. [ROL EXPERTO]: Eres {rol_especialista} de la firma.
2. [CONTEXTO]: Analizas un caso de {area_practica} relativo a [{VARIABLE_TIPO_CASO}].
3. [INSTRUCCIÓN MAESTRA]:
   Procesa [{VARIABLE_DOCUMENTO_ENTRADA}] para generar [{VARIABLE_ENTREGABLE}] identificando:
   - [{VARIABLE_CRITERIO_1}]
   - [{VARIABLE_CRITERIO_2}]
4. [RESTRICCIONES]:
   - Respeta estrictamente el secreto profesional y la política de confidencialidad.
   - Cita únicamente normativa vigente en [{VARIABLE_JURISDICCION}].
5. [FORMATO DE ENTREGA]: Formato tabular en Markdown estructurado en [{VARIABLE_COLUMNAS_TABLA}].""",
        example="""Blueprint maestro para la calificación de contingencias en Due Diligence laboral, con variables parametrizadas para tipo de empresa, número de trabajadores y muestra de expedientes."""
    ),
    "pipeline": PromptFramework(
        name="Pipeline Modular (Encadenamiento con Control Humano)",
        code="PIPELINE",
        description="Secuencia de prompts modulares en 3 etapas discretas con puntos de validación del abogado (Human-in-the-Loop).",
        template="""EJECUCIÓN POR ETAPAS MODULARES (Pipeline Jurídico):

Etapa Activa: [{etapa_seleccionada}]

Paso 1 (Extracción):
- Insumo: {expediente_completo}
- Tarea: Extrae exclusivamente tabla fáctica (fechas, partes, pretensiones, excepciones propuestas).
- Punto de Control: Detén la ejecución hasta que el abogado valide la tabla fáctica.

Paso 2 (Análisis Crítico):
- Insumo: Tabla fáctica validada en el Paso 1.
- Tarea: Detecta contradicciones probatorias y debilidades de la contraparte.
- Punto de Control: El abogado aprueba los argumentos seleccionados.

Paso 3 (Generación de Escrito):
- Insumo: Matriz argumentativa validada en el Paso 2.
- Tarea: Redacta el borrador del memorial o alegato en formato judicial formal.""",
        example="""Pipeline en 3 etapas para contestación de demandas laborales: 1) Extracción de hechos y términos, 2) Auditoría de excepciones previas y de mérito, 3) Redacción del memorial de contestación."""
    ),
    "few_shot": PromptFramework(
        name="Few-Shot Jurídico (Demostración por Ejemplos)",
        code="FEW_SHOT",
        description="Entrenamiento en contexto proporcionando ejemplos concretos del estilo y formato exacto esperado.",
        template="""[INSTRUCCIÓN GENERAL]:
{instruccion_tarea}

[EJEMPLO MODELO 1 - ENTRADA]:
{ejemplo_entrada_1}
[EJEMPLO MODELO 1 - SALIDA ESPERADA]:
{ejemplo_salida_1}

[CASO REAL A PROCESAR]:
{caso_real}

Genera el resultado para el caso real replicando con absoluta precisión el tono, rigor dogmático y estructura de las salidas modelo.""",
        example="""Extracción de fichas jurisprudenciales de sentencias de casación: Se aporta un ejemplo de sentencia con su correspondiente resumen de ratio decidendi, hechos relevantes y problema jurídico resuelto, para que el modelo procese un fallo de 80 páginas idénticamente."""
    ),
    "red_team": PromptFramework(
        name="Red Teaming Legal (Validación y Contradictorio)",
        code="RED_TEAM",
        description="Auto-crítica y auditoría rigurosa del borrador asumiendo el rol del apoderado de la contraparte o del juez.",
        template="""Actúa como el abogado litigante más incisivo de la contraparte ({contraparte}) o como el Juez de conocimiento.
Revisa y audita críticamente el siguiente borrador de memorial/concepto:

Borrador a Auditar:
{borrador_texto}

Genera tu informe de auditoría identificando:
1. Las 3 principales fisuras, contradicciones o vacíos argumentativos del escrito.
2. La mejor objeción probatoria o excepción previa que formularías contra nuestra postura.
3. El contraargumento jurisprudencial más sólido que podría derribar nuestra tesis.
4. Recomendaciones concretas de blindaje para neutralizar esos ataques antes de la radicación.""",
        example="""Actúa como el apoderado de la entidad demandada en un litigio contractual ante tribunal arbitral y destruye los argumentos de nuestro borrador de demanda de reconvención para encontrar nuestros flancos débiles."""
    )
}

# Alias for backwards compatibility and easy lookup by acronym
FRAMEWORKS["tot"] = FRAMEWORKS["tree_of_thought"] = FRAMEWORKS["tot"]


def get_framework(code: str) -> Optional[PromptFramework]:
    """Retrieve framework by code or key (case-insensitive)."""
    code_lower = code.lower().strip()
    if code_lower in FRAMEWORKS:
        return FRAMEWORKS[code_lower]
    for fw in FRAMEWORKS.values():
        if fw.code.lower() == code_lower:
            return fw
    return None


def list_frameworks() -> List[PromptFramework]:
    """List all available legal prompt frameworks (unique entries)."""
    seen = set()
    unique_frameworks = []
    for fw in FRAMEWORKS.values():
        if fw.code not in seen:
            seen.add(fw.code)
            unique_frameworks.append(fw)
    return unique_frameworks


def export_frameworks_to_markdown(
    title: str = "Módulo 3.2 (Anexo): Catálogo de Frameworks y Prompts Jurídicos",
    subtitle: str = "Plantillas Maestras y Ejemplos Prácticos de Ingeniería de Prompts",
    author: str = "Ricardo A. Reyes",
    institute: str = "Universidad de La Sabana",
    background_image: str = "Images/UniSabana.jpg"
) -> str:
    """Exports all prompt frameworks as Beamer presentation slides in Markdown format."""
    lines = [
        "---",
        f'title: "{title}"',
        f'subtitle: "{subtitle}"',
        f'author: "{author}"',
        f'institute: "{institute}"',
        "format: revealjs",
        f"background_image: {background_image}",
        "---",
        "",
        "# Módulo 3.2: Anexo de Prompts",
        "",
        "## Portada",
        f"**Título:** {title}",
        f"**Subtítulo:** {subtitle}",
        "**Notas del Mentor:** *Compendio completo de frameworks de prompting legal para la firma.*",
        "",
        "---",
        "",
        "## Catálogo de Frameworks de Prompting Legal",
        "",
        "Frameworks de estandarización cognitiva y flujos de trabajo para la firma:",
        ""
    ]

    for fw in list_frameworks():
        lines.append(f"* **{fw.code}:** {fw.description}")

    for fw in list_frameworks():
        lines.extend([
            "",
            "---",
            "",
            f"## Framework {fw.code}: Estructura y Plantilla",
            "",
            f"* **Nombre:** {fw.name}",
            f"* **Objetivo:** {fw.description}",
            "* **Plantilla Maestra:**"
        ])
        for t_line in fw.template.splitlines():
            if t_line.strip():
                lines.append(f"  * {t_line.strip()}")

        lines.extend([
            "",
            "---",
            "",
            f"## Framework {fw.code}: Caso Práctico en Derecho",
            "",
            "* **Aplicación Forense / Caso Real:**"
        ])
        for e_line in fw.example.splitlines():
            if e_line.strip():
                lines.append(f"  * {e_line.strip()}")

    lines.extend([
        "",
        "---",
        "",
        "## ¡Sigamos en Contacto!",
        "",
        "La Inteligencia Artificial avanza todos los días. ¡No duden en escribirme para compartir ideas, resolver dudas o seguir conversando sobre cómo la IA puede transformar su práctica jurídica!",
        "",
        "* **WhatsApp:** (57) 3012726157",
        "* **Email:** [rareyesj@gmail.com](mailto:rareyesj@gmail.com)",
        "",
        "**¡Muchas gracias por su participación!**",
        ""
    ])

    return "\n".join(lines)

