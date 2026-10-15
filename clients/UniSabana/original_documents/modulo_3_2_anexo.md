---
title: "Módulo 3.2 (Anexo): Catálogo de Frameworks y Prompts Jurídicos"
subtitle: "Plantillas Maestras y Ejemplos Prácticos de Ingeniería de Prompts"
author: "Ricardo A. Reyes"
institute: "Universidad de La Sabana"
format: revealjs
background_image: Images/UniSabana.jpg
---

# Módulo 3.2: Anexo de Prompts

## Portada
**Título:** Catálogo de Frameworks y Prompts Jurídicos (Anexo 3.2)
**Subtítulo:** Plantillas Maestras y Ejemplos Prácticos de Ingeniería de Prompts
**Notas del Mentor:** *¡Bienvenidos a este Anexo del Módulo 3.2! Aquí encontrarán el compendio completo de todos los frameworks de Prompt Engineering Legal de nuestro toolkit, con sus estructuras base y casos de uso prácticos para la práctica diaria de la firma.*

---

## Catálogo de Frameworks de Prompting Legal

Frameworks de estandarización cognitiva y flujos de trabajo para la firma:

* **CARE:** Análisis de viabilidad y conceptos jurídicos corporativos.
* **ADP:** Auditoría contractual, due diligence y detección de asimetrías.
* **TAM:** Redacción persuasiva, negociación y correspondencia formal.
* **CoT (Chain-of-Thought):** Razonamiento secuencial paso a paso.
* **ToT (Tree-of-Thought):** Análisis de vías y escenarios procesales alternativos.
* **IRAC / CRAC:** Metodología dogmática formal de subsunción jurídica.
* **Grounding Blindado:** Operación en circuito cerrado anti-alucinaciones.
* **Blueprint Institucional:** Parametrización estandarizada con variables `[ ]`.
* **Pipeline Modular:** Encadenamiento secuencial con control humano (*Human-in-the-Loop*).
* **Few-Shot Jurídico:** Calibración mediante ejemplos modelo demostrativos.
* **Red Teaming Legal:** Auto-crítica y contradictorio simulando a la contraparte.

---

## Framework CARE: Estructura y Plantilla

* **Nombre:** CARE Framework (Conceptos y Análisis)
* **Objetivo:** Estructura estándar para solicitudes de análisis o conceptos jurídicos corporativos.
* **Plantilla Maestra:**
  * **[ROL]:** Eres un `[ROL_LEGAL]` en la jurisdicción de `[JURISDICCIÓN]`.
  * **[CONTEXTO]:** `[CONTEXTO_Y_HECHOS_RELEVANTES]`
  * **[ACCIÓN]:** `[ACCIÓN_O_ANALISIS_SOLICITADO]`
  * **[RESULTADO ESPERADO]:** `[FORMATO_Y_EXTENSION_DEL_ENTREGABLE]`
  * **[EVALUACIÓN Y RESTRICCIONES]:** `[RESTRICCIONES_LEGALES_Y_FUENTES]`

---

## Framework CARE: Caso Práctico en Derecho

* **Caso de Aplicación (Tributario / Corporativo):**
  * **[ROL]:** Eres un abogado tributarista senior en Colombia.
  * **[CONTEXTO]:** Una empresa de software colombiana vende licencias SaaS a clientes en EE.UU.
  * **[ACCIÓN]:** Determina las implicaciones del impuesto sobre la renta y retención en la fuente.
  * **[RESULTADO ESPERADO]:** Memorando legal ejecutivo de máximo 3 páginas con recomendaciones.
  * **[EVALUACIÓN Y RESTRICCIONES]:** Cita únicamente el Estatuto Tributario colombiano vigente y doctrina de la DIAN.

---

## Framework ADP: Estructura y Plantilla

* **Nombre:** ADP Framework (Auditoría Contractual y Due Diligence)
* **Objetivo:** Especializado en revisión de contratos, due diligence y detección de cláusulas leoninas o de riesgo.
* **Plantilla Maestra:**
  * **[ACTOR]:** Eres el apoderado legal de la parte `[POSICIÓN_DEL_CLIENTE]` *(Comprador / Arrendatario / Empleador)*.
  * **[DOCUMENTO]:** `[TIPO_DE_DOCUMENTO_O_CLÁUSULAS]`
  * **[PROPÓSITO]:**
    1. Identifica cláusulas que impongan obligaciones asimétricas, penalidades desproporcionadas o riesgos ocultos para mi cliente.
    2. Evalúa topes de indemnidad, causales de terminación anticipada y ley aplicable.
    3. Para cada riesgo detectado, redacta una propuesta de redacción alternativa justa y equilibrada.

---

## Framework ADP: Caso Práctico en Derecho

* **Caso de Aplicación (Contratación Mercantil y SLA):**
  * **[ACTOR]:** Eres el abogado de la Empresa Compradora.
  * **[DOCUMENTO]:** Revisa el contrato de suministro y SLA adjunto.
  * **[PROPÓSITO]:** Identifica penalidades unilaterales, extensiones de plazo sin compensación y limitaciones de responsabilidad del proveedor. Propón cláusulas de reemplazo en formato tabla comparativa.

---

## Framework TAM: Estructura y Plantilla

* **Nombre:** TAM Framework (Redacción y Comunicación Legal)
* **Objetivo:** Diseñado para redactar correspondencia formal, cobros extrajudiciales, memoriales y comunicación con clientes.
* **Plantilla Maestra:**
  * **[TAREA]:** `[OBJETIVO_DE_COMUNICACIÓN]` *(ej. cobro extrajudicial, respuesta a requerimiento, comunicación a socios)*.
  * **[AUDIENCIA]:** `[DESTINATARIO_Y_RELACIÓN]` *(ej. contraparte comercial clave, entidad de control, cliente institucional)*.
  * **[MÉTODO]:** Canal: `[CANAL]` | Tono: `[TONO_Y_ESTILO]` | Marco de Negociación: `[LÍMITES]`.

---

## Framework TAM: Caso Práctico en Derecho

* **Caso de Aplicación (Cobro Extrajudicial Conciliador):**
  * **[TAREA]:** Redactar un requerimiento de cobro por mora de 90 días en cánones de arrendamiento comercial.
  * **[AUDIENCIA]:** Representante legal de la empresa arrendataria *(relación comercial histórica de 5 años que deseamos preservar)*.
  * **[MÉTODO]:** Correo electrónico formal y persuasivo; tono asertivo pero conciliador; citando el contrato y ofreciendo una mesa de acuerdo de pago en un plazo de 5 días hábiles.

---

## Chain-of-Thought (CoT): Estructura y Plantilla

* **Nombre:** Chain-of-Thought (Ingeniería de Razonamiento)
* **Objetivo:** Desglose de pensamiento paso a paso para evitar alucinaciones en análisis jurídicos complejos.
* **Plantilla Maestra:**
  * Analiza la siguiente situación jurídica desglosando tu razonamiento paso a paso antes de emitir cualquier conclusión final:
  * **Situación:** `[SITUACIÓN_FÁCTICA]`
  * **Pasos obligatorios de razonamiento:**
    1. Identifica las fuentes normativas y jurisprudenciales aplicables.
    2. Analiza los elementos constitutivos de la figura jurídica en cuestión.
    3. Contrasta los hechos materiales con cada uno de los elementos normativos.
    4. Evalúa las excepciones, defensas o causales de exoneración aplicables.
    5. Emite la conclusión y recomendación procesal final.

---

## Chain-of-Thought (CoT): Caso Práctico en Derecho

* **Caso de Aplicación (Responsabilidad Civil y Daño Ambiental):**
  * *"Analiza si se configuran los elementos de responsabilidad civil extracontractual por daño ambiental en este caso de derrame industrial, evaluando nexo causal, daño cierto y culpa probada paso a paso antes de emitir conclusiones."*
* **Impacto Operativo:**
  * Obliga al modelo a descomponer el análisis de causación y culpabilidad antes de emitir el dictamen, erradicando saltos argumentativos.

---

## Tree-of-Thought (ToT): Estructura y Plantilla

* **Nombre:** Tree-of-Thought (Estrategia Procesal Paralela)
* **Objetivo:** Mapeo de múltiples vías procesales o defensivas alternativas con análisis comparativo de riesgo y viabilidad.
* **Plantilla Maestra:**
  * Desarrolla 3 alternativas estratégicas distintas para resolver el siguiente problema legal:
  * **Problema Legal:** `[PROBLEMA_LEGAL]`
  * Para cada una de las 3 alternativas, detalla de forma independiente:
    * a) Tesis jurídica principal y soporte normativo.
    * b) Nivel de riesgo probatorio y procesal *(Bajo / Medio / Alto)*.
    * c) Probabilidad estimada de éxito y tiempos procesales probables.
    * d) Impacto económico, operativo o reputacional para el cliente.
    * e) Matriz resumen comparativa final recomendando la mejor opción.

---

## Tree-of-Thought (ToT): Caso Práctico en Derecho

* **Caso de Aplicación (Defensa Sancionatoria ante la SIC):**
  * *"Desarrolla 3 alternativas estratégicas defensivas ante un pliego de cargos formulado por la Superintendencia de Industria y Comercio (SIC) por presunta infracción a la libre competencia:"*
    * **Alternativa 1:** Solicitud de garantías y compromisos anticipados de terminación.
    * **Alternativa 2:** Formulación de excepciones previas de prescripción y nulidad por debido proceso.
    * **Alternativa 3:** Defensa de fondo en descargos probatorios y dictamen económico de mercado.

---

## Framework IRAC / CRAC: Estructura y Plantilla

* **Nombre:** IRAC / CRAC (Subsunción Jurídica Universal)
* **Objetivo:** Estructura formal internacional para conceptos, dictámenes jurídicos y alegatos de conclusión.
* **Plantilla Maestra:**
  * **[ISSUE / PROBLEMA JURÍDICO]:** Formula con precisión la pregunta jurídica central a resolver.
  * **[RULE / REGLA DE DERECHO]:** Identifica las normas vigentes, principios generales y precedentes vinculantes.
  * **[APPLICATION / SUBSUNCIÓN]:** Aplica la regla jurídica identificada a los hechos fácticos concretos del caso.
  * **[CONCLUSION / DICTAMEN FINAL]:** Emite una respuesta contundente al problema planteado y los pasos de mitigación recomendados.

---

## Framework IRAC / CRAC: Caso Práctico en Derecho

* **Caso de Aplicación (Estabilidad Laboral Reforzada):**
  * **[ISSUE]:** ¿Vulnera el empleador la estabilidad laboral reforzada al desvincular a un empleado con recomendación médica sin autorización del MinTrabajo?
  * **[RULE]:** Cita el artículo 26 de la Ley 361 de 1997 y la jurisprudencia unificada de la Corte Constitucional (SU-049/17 y Sala Laboral CSJ).
  * **[APPLICATION]:** Subsume el caso de terminación con indemnización frente al conocimiento previo de la patología por el empleador.
  * **[CONCLUSION]:** Determina el riesgo de reintegro y pago de 180 días de salario.

---

## Grounding Blindado: Estructura y Plantilla

* **Nombre:** Grounding Blindado (Circuito Cerrado Anti-Alucinación)
* **Objetivo:** Forzar al modelo a operar exclusivamente con base en la evidencia y textos suministrados, prohibiendo invenciones.
* **Plantilla Maestra:**
  * **[ROL]:** Eres un auditor judicial y analista de expedientes estricto.
  * **[INSTRUCCIÓN]:** Responde las preguntas basándote ÚNICA Y EXCLUSIVAMENTE en el texto del expediente adjunto.
  * **[RESTRICCIONES INFRANQUEABLES]:**
    1. Si una respuesta no se encuentra taxativamente en el documento, responde exactamente: *"Dato no verificable en el expediente suministrado"*.
    2. Prohibido asumir hechos, extrapolar intenciones o inventar radicados, fechas o normas.
    3. Cita la página y párrafo exacto de donde fue extraída cada afirmación fáctica.

---

## Grounding Blindado: Caso Práctico en Derecho

* **Caso de Aplicación (Auditoría Contractual Estricta):**
  * *"Audita el siguiente contrato de arrendamiento. Si no encuentras una cláusula expresa sobre subarriendo o cesión, declara 'Dato no verificable en el contrato' y bajo ninguna circunstancia asumas la regla supletiva del Código Civil."*
* **Garantía Profesional:**
  * Máxima seguridad ante tribunales arbitrales y autoridades judiciales: cero riesgo de alucinaciones normativas o fácticas.

---

## Blueprint Institucional: Estructura y Plantilla

* **Nombre:** Blueprint Institucional (Los 5 Pilares de la PromptLibrary)
* **Objetivo:** Estructura estándar de la firma para registrar y compartir prompts reutilizables con variables delimitadas en corchetes `[ ]`.
* **Plantilla Maestra:**
  * **1. [ROL EXPERTO]:** Eres `[ROL_ESPECIALISTA]` de la firma.
  * **2. [CONTEXTO]:** Analizas un caso de `[ÁREA_PRÁCTICA]` relativo a `[TIPO_DE_CASO]`.
  * **3. [INSTRUCCIÓN MAESTRA]:** Procesa `[DOCUMENTO_ENTRADA]` para generar `[ENTREGABLE]` identificando `[CRITERIO_1]` y `[CRITERIO_2]`.
  * **4. [RESTRICCIONES]:** Respeta el secreto profesional y cita solo normativa vigente en `[JURISDICCIÓN]`.
  * **5. [FORMATO DE ENTREGA]:** Formato tabular estructurado en `[COLUMNAS_TABLA]`.

---

## Blueprint Institucional: Caso Práctico en Derecho

* **Caso de Aplicación (Auditoría de Contingencias en Due Diligence):**
  * Blueprint maestro para la calificación de contingencias en Due Diligence laboral:
  * **Campos Variables Parametrizados:**
    * `[TIPO_DE_EMPRESA]`: Empresa del sector industrial con 250 empleados.
    * `[MUESTRA_EXPEDIENTES]`: 30 procesos ordinarios laborales en curso.
    * `[CRITERIOS_REVISIÓN]`: Pretensiones económicas, estado de pruebas y probabilidad de condena (Remota / Posible / Probable).
    * `[FORMATO]`: Tabla comparativa con provisiones contables sugeridas.

---

## Pipeline Modular: Estructura y Plantilla

* **Nombre:** Pipeline Modular (Encadenamiento con Control Humano)
* **Objetivo:** Secuencia de prompts modulares en 3 etapas discretas con puntos de validación del abogado (*Human-in-the-Loop*).
* **Plantilla Maestra:**
  * **Paso 1 (Extracción Fáctica):** Extrae exclusivamente la cronología fáctica (fechas, partes, pretensiones). Detén la ejecución hasta que el abogado valide la tabla.
  * **Paso 2 (Análisis Crítico):** Detecta contradicciones probatorias y debilidades. El abogado aprueba los argumentos seleccionados.
  * **Paso 3 (Generación de Escrito):** Redacta el borrador del memorial o alegato en formato judicial formal.

---

## Pipeline Modular: Caso Práctico en Derecho

* **Caso de Aplicación (Contestación de Demanda Ordinaria Laboral):**
  * **Etapa 1:** Extracción automatizada de hechos, fechas de despido y liquidaciones previas.
  * **Control 1:** El abogado verifica que no falten pruebas documentales.
  * **Etapa 2:** Análisis de excepciones previas (prescripción de 3 años, falta de legitimación).
  * **Control 2:** El abogado define la línea estratégica de defensa.
  * **Etapa 3:** Generación del proyecto de contestación hecho por hecho.

---

## Few-Shot Jurídico: Estructura y Plantilla

* **Nombre:** Few-Shot Jurídico (Demostración por Ejemplos)
* **Objetivo:** Calibración en contexto suministrando ejemplos del estilo, formato y nivel de exhaustividad requerido.
* **Plantilla Maestra:**
  * **[INSTRUCCIÓN GENERAL]:** `[INSTRUCCIÓN_DE_LA_TAREA]`
  * **[EJEMPLO MODELO 1 - ENTRADA]:** `[EJEMPLO_DOCUMENTO_ENTRADA]`
  * **[EJEMPLO MODELO 1 - SALIDA ESPERADA]:** `[EJEMPLO_SALIDA_IDEAL]`
  * **[CASO REAL A PROCESAR]:** `[DOCUMENTO_REAL]`
  * *"Genera el resultado para el caso real replicando con absoluta precisión el tono, rigor dogmático y estructura de las salidas modelo."*

---

## Few-Shot Jurídico: Caso Práctico en Derecho

* **Caso de Aplicación (Fichas Jurisprudenciales de Casación):**
  * **Entrada Modelo:** Fragmento de sentencia de casación laboral sobre culpa patronal en accidente de trabajo.
  * **Salida Modelo:** Ficha estructurada en *Ratio Decidendi*, *Problema Jurídico Central* y *Regla Vinculante*.
  * **Ejecución Real:** El modelo procesa un fallo de 80 páginas replicando el mismo rigor y estilo analítico de la firma sin divagar.

---

## Red Teaming Legal: Estructura y Plantilla

* **Nombre:** Red Teaming Legal (Validación y Contradictorio)
* **Objetivo:** Auto-crítica y auditoría rigurosa del borrador asumiendo el rol del apoderado de la contraparte o del juez.
* **Plantilla Maestra:**
  * *"Actúa como el abogado litigante más incisivo de la contraparte o como el Juez de conocimiento."*
  * **Informe de Auditoría Requerido:**
    1. Las 3 principales fisuras, contradicciones o vacíos argumentativos del escrito.
    2. La mejor objeción probatoria o excepción previa que formularías contra nuestra postura.
    3. El contraargumento jurisprudencial más sólido que podría derribar nuestra tesis.
    4. Recomendaciones concretas de blindaje para neutralizar esos ataques antes de radicar.

---

## Red Teaming Legal: Caso Práctico en Derecho

* **Caso de Aplicación (Auditoría de Demanda de Reconvención Arbitral):**
  * *"Actúa como el apoderado de la entidad demandada en un litigio contractual ante tribunal arbitral y destruye los argumentos de nuestro borrador de demanda de reconvención para encontrar nuestros flancos débiles."*
* **Beneficio Estratégico:**
  * Blindaje preventivo de pretensiones y pruebas antes de la radicación formal, anticipando las objeciones del contradictor.

---

## ¡Sigamos en Contacto!

La Inteligencia Artificial avanza todos los días. ¡No duden en escribirme para compartir ideas, resolver dudas o seguir conversando sobre cómo la IA puede transformar su práctica jurídica!

* **WhatsApp:** (57) 3012726157
* **Email:** [rareyesj@gmail.com](mailto:rareyesj@gmail.com)

**¡Muchas gracias por su participación!**
