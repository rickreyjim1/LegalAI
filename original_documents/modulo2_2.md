---
title: "Módulo 2.2: Técnicas Avanzadas y Frameworks de Prompting"
format: revealjs
---

# Módulo 2.2: Técnicas Avanzadas y Frameworks de Prompting (Clase 2)

## Portada

**Título:** Técnicas Avanzadas y Frameworks de Prompting
**Subtítulo:** Estandarización de procesos e ingeniería de razonamiento (Sesión 2)
**Notas del Mentor:** *¡Hola de nuevo! Bienvenidos a la segunda clase del Módulo 2. Hoy daremos el salto definitivo. Pasaremos de estructurar prompts individuales a diseñar sistemas de pensamiento para la IA (como Chain-of-Thought) y frameworks empresariales (CARE, ADP, TAM) que pueden estandarizar el trabajo de toda su firma de abogados.*

---

## Objetivos de la Clase 2

* **Repaso (15 min):** Consolidar los 5 componentes del prompt y técnicas de shot prompting.
* **Técnicas Avanzadas:** Dominar Chain-of-Thought, Break the Task Down y Super Prompting.
* **Frameworks Metodológicos:** Implementar CARE, ADP y TAM en la práctica diaria de la firma.
* **Auditoría Cruzada:** Usar técnicas de Red Teaming para encontrar vacíos legales y blindar entregables.
* **Taller Avanzado:** Resolver un caso real de tu práctica profesional en vivo.

---

## Repaso: Los 5 Componentes del Prompt

* Todo prompt profesional debe contener la estructura de 5 pilares para evitar la variabilidad estadística y las alucinaciones:
    * **Rol:** ¿Quién es la IA? (Jurisdicción y experiencia).
    * **Contexto:** Hechos materiales limpios.
    * **Instrucción:** El verbo imperativo de la acción.
    * **Restricciones:** Límites técnicos y normativos duros.
    * **Formato:** Estructura visual exacta de la respuesta.

---

## Repaso: Delimitando el Rol y Contexto

* **El Rol** no es un adorno; redirige la atención probabilística de la red neuronal hacia un corpus de texto especializado.
* **El Contexto** debe segmentarse para evitar que la IA asuma datos inexistentes.
* **Consejo:** Usar delimitadores visuales (ej. `\"\"\"` o `---`) para aislar el contexto del resto de las instrucciones del prompt.

**Notas del Mentor:** *Recuerden: si no le dan contexto, la IA usará el promedio estadístico de Internet. Y en derecho, el promedio suele ser incorrecto para el caso concreto de su cliente.*

---

## Repaso: Instrucciones y Restricciones Robustas

\begin{table}
\resizebox{\textwidth}{!}{
\begin{tabular}{|l|l|}
\hline
\textbf{Instrucción Débil} & \textbf{Instrucción Robusta} \\ \hline
"Mira si este contrato está bien." & "Analiza la cláusula 5 e identifica riesgos de sobrefacturación." \\ \hline
"Haz un memo legal." & "Redacta un memorando ejecutivo de 3 secciones bajo el formato Markdown." \\ \hline
"Usa leyes de Colombia." & "Cita únicamente la Ley 1581 de 2012 y doctrina oficial de la SIC." \\ \hline
\end{tabular}
}
\end{table}

**Notas del Mentor:** *La diferencia entre un resultado mediocre y uno sobresaliente está en la rigurosidad de las restricciones que le impongan a la IA.*

---

## Repaso: Formatos y Shot Prompting

* **Shot Prompting** es el método más rápido para guiar la forma de trabajar del modelo:
    * **Zero-Shot:** Para tareas de baja complejidad.
    * **One-Shot:** Cuando quieres fijar un formato visual específico.
    * **Few-Shot:** Clave para imitar el tono de redacción, estilo lingüístico y profundidad analítica de la firma.

---

## Introducción a Técnicas Avanzadas

* Cuando el problema jurídico es complejo (ej. planificar una estrategia judicial o resolver un conflicto tributario cruzado), los prompts tradicionales de una sola instrucción fallan.
* **¿Por qué?:** Los LLMs tienden a cometer errores si se les pide una conclusión de forma inmediata sin permitirles procesar los pasos lógicos intermedios [@openai2023].
* **Solución:** Ingeniería de razonamiento.

---

## Chain-of-Thought (CoT): Razonamiento Secuencial

* **¿Qué es?:** Forzar al modelo a exteriorizar y desglosar su razonamiento paso a paso antes de emitir la conclusión jurídica final.
* **Efecto:** Reduce las alucinaciones hasta en un 50% porque alinea los tokens de razonamiento antes de calcular la respuesta definitiva.
* **Instrucción Clave:** *"Piensa paso a paso..."* o *"Desglosa tu razonamiento legal bajo las siguientes fases..."*

**Notas del Mentor:** *Si le pides a un abogado junior que te dé un veredicto en 2 segundos, probablemente se equivoque. Si le pides que analice primero la norma, luego las pruebas y finalmente concluya, su rigor aumenta. Con la IA ocurre exactamente lo mismo.*

---

## CoT en Acción: Evitando la Alucinación

**Prompt con CoT Aplicado:**
> *"Analiza si los hechos descritos configuran un despido injustificado bajo el Código Sustantivo del Trabajo.*
> *Antes de dar tu conclusión, sigue estrictamente este orden de razonamiento:*
> *1. Identifica la causal de terminación invocada por el empleador.*
> *2. Contrasta dicha causal con los requisitos formales de la ley.*
> *3. Revisa la jurisprudencia reciente aplicable.*
> *4. Concluye únicamente después de completar los pasos 1, 2 y 3."*

---

## Break the Task Down: Descomposición de Tareas

* **El Principio:** No intentes resolver todo en un solo prompt masivo.
* **Fases del Flujo de Trabajo:**
    * **Paso 1 (Extracción):** Extrae los hechos clave del documento.
    * **Paso 2 (Análisis):** Cruza los hechos con la norma aplicable.
    * **Paso 3 (Redacción):** Redacta el concepto jurídico basado en el análisis del Paso 2.
* **Resultado:** Cada paso genera una salida limpia y verificable, evitando la fatiga cognitiva del modelo.

---

## Super Prompting: Prompts Interactivos

* **¿Qué es?:** Diseñar prompts que transforman a la IA en un consultor activo que hace preguntas antes de dar una respuesta.
* **Estructura del Super Prompt:**
    * *"Actúa como un Socio de Litigio. Tu objetivo es ayudarme a preparar la contestación de la demanda. No redactes nada todavía. Hazme preguntas de una en una sobre los hechos del caso. Cuando tengas suficiente información, avísame y genera el primer borrador."*
* **Beneficio:** Evita que tengas que escribir un prompt de 3 páginas con todo el contexto de una sola vez.

**Notas del Mentor:** *Esta es la forma favorita de trabajar de los directores jurídicos: convertir el chat en una entrevista interactiva.*

---

## Frameworks de Estandarización en la Firma

Para que una firma de abogados adopte IA a gran escala, no basta con dar accesos a los asociados; se deben estandarizar los flujos de trabajo mediante frameworks reutilizables.

Analizaremos tres metodologías estratégicas:
1. **CARE** (Para Análisis y Conceptos).
2. **ADP** (Para Revisión y Auditoría).
3. **TAM** (Para Redacción y Comunicación).

---

## CARE Framework: Análisis y Conceptos

Diseñado para la elaboración de memorandos, conceptos jurídicos y análisis de viabilidad:

* **C - Contexto:** Delimitar hechos y partes involucradas.
* **A - Acción:** Definir la tarea jurídica (ej. *"Evaluar el riesgo tributario..."*).
* **R - Resultado:** Formato y extensión esperada del entregable.
* **E - Evaluación:** Restricciones, leyes específicas a considerar y análisis de riesgos.

---

## CARE en Acción: Ejemplo Práctico

\begin{lstlisting}[basicstyle=\ttfamily\scriptsize]
[CONVENIO CARE]
1. CONTEXTO: Cliente extranjero adquiere propiedad raiz en Colombia mediante fiducia.
2. ACCION: Identificar la tarifa del impuesto de registro aplicable.
3. RESULTADO: Memorando ejecutivo de 2 paginas con titulos en Markdown.
4. EVALUACION: Limitate al Estatuto Tributario y Ley 223 de 1995. Advierte sobre los riesgos de interpretacion de la DIAN.
\end{lstlisting}

**Notas del Mentor:** *Estructurar los requerimientos bajo CARE asegura que cualquier asociado de la firma genere conceptos de calidad uniforme.*

---

## ADP Framework: Auditoría y Revisión

Especialmente diseñado para la revisión automatizada de contratos e instrumentos jurídicos:

* **A - Actor:** Definir desde qué posición se audita (ej. *"Actúa como abogado del Arrendatario..."*).
* **D - Documento:** Especificar el tipo de contrato y sus cláusulas clave.
* **P - Propósito:** Qué se busca proteger o identificar (ej. *"Limitar la responsabilidad por daños indirectos..."*).

---

## ADP en Acción: Ejemplo Práctico

**Prompt con ADP:**
> *[ACTOR]: Eres el abogado de la Empresa Compradora.*
> *[DOCUMENTO]: Revisa el contrato de suministro adjunto.*
> *[PROPÓSITO]: Identifica cualquier cláusula que imponga penalidades unilaterales a mi cliente o que extienda los plazos de entrega sin compensación. Propón una redacción alternativa equitativa para cada riesgo encontrado.*

---

## TAM Framework: Redacción de Documentos

Ideal para redactar cartas formales, correos electrónicos a clientes, requerimientos extrajudiciales o comunicados corporativos:

* **T - Tarea:** El objetivo de la comunicación (ej. *"Solicitar la restitución del inmueble..."*).
* **A - Audiencia:** A quién va dirigido y cuál debe ser la relación jerárquica/de tono.
* **M - Método:** El canal y tono lingüístico (ej. *"Formal, firme pero conciliador; a través de correo electrónico"*).

---

## TAM en Acción: Ejemplo Práctico

**Prompt con TAM:**
> *[TAREA]: Redactar un requerimiento de cobro por mora en arrendamiento comercial.*
> *[AUDIENCIA]: Representante legal de la empresa arrendataria (relación comercial de 5 años que queremos conservar).*
> *[MÉTODO]: Correo electrónico formal, persuasivo, citando el contrato pero abriendo la puerta a un acuerdo de pago.*

---

## Taller Avanzado: Clínica de Prompts Complejos

**Dinámica Grupal (60 Minutos):**

1. **Elige tu Reto:** Un caso real y complejo de tu escritorio (ej. planeación de una defensa ante un ente de control).
2. **Implementación de Framework:** Diseña un prompt estructurado usando el framework **CARE** combinado con **Chain-of-Thought**.
3. **Ejecución y Auditoría:** Ejecuta el prompt en la IA y prepárate para la fase de Red Teaming.

**Notas del Mentor:** *Esta es la parte más valiosa de la sesión. Asegúrense de que los participantes usen datos simulados o anonimizados para cumplir con las normas de confidencialidad.*

---

## Red Teaming Legal: Auditoría Cruzada

* **El Paso Final:** Una vez que la IA te da una respuesta (ej. una contestación de demanda), no la asumas como perfecta.
* **El Prompt de Red Teaming:**
  \begin{lstlisting}[basicstyle=\ttfamily\scriptsize]
  [INSTRUCCION]
  Actua como el abogado de la contraparte.
  Encuentra los 3 puntos mas debiles de la respuesta de la IA anterior.
  Dime como atacarias esos argumentos en el juzgado.
  \end{lstlisting}
* **Resultado:** Un blindaje total del documento antes de la firma del abogado.

---

## Buenas Prácticas Organizacionales

* **Biblioteca de Prompts:** Centralizar los prompts exitosos (CARE, ADP) en un documento compartido de la firma para evitar la pérdida de conocimiento.
* **Capacitación Continua:** Los modelos cambian; auditar semestralmente que las plantillas sigan funcionando de manera óptima [@sal2024].
* **Control de Calidad:** Ningún entregable generado por IA sale de la firma sin la revisión final de un abogado matriculado.

---

## Cierre y Próximos Pasos

* **Resumen:** Hemos pasado del prompt amateur a la ingeniería de razonamiento y frameworks estructurados.
* **Tu Misión:** Implementar al menos una plantilla CARE o ADP en tus tareas de la próxima semana y medir las horas de trabajo ahorradas.
* **Próximo Módulo (Módulo 3):** Automatización avanzada e integración de sistemas.

**¡Muchas gracias por su atención y compromiso!**

---
