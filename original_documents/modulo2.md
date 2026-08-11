---
title: "Módulo 2: Fundamentos de Legal Prompting"
format: revealjs
---

# Módulo 2: Fundamentos de Legal Prompting (Clase 1)

## Portada

**Título:** Legal Prompting: Aprende a hablarle a la IA
**Subtítulo:** De la interacción básica a resultados jurídicos precisos (Sesión 1)
**Notas del Mentor:** *¡Bienvenidos a la primera clase del Módulo 2! Hoy dejaremos atrás el uso amateur de la IA. Si alguna vez han sentido frustración porque ChatGPT o Claude les da respuestas genéricas o alucina leyes, hoy entenderán por qué ocurre y cómo solucionarlo. Vamos a aprender a estructurar instrucciones con nivel de socio de firma.* [Dinámica: Preguntar al grupo: ¿Quién ha obtenido la respuesta más inútil de una IA y cómo era el prompt?]

---

## Objetivos de la Clase 1

* Superar el "Mito del Oráculo" y entender el funcionamiento estadístico de la IA.
* Dominar los 5 componentes estructurales de un prompt jurídico de alta precisión.
* Aprender cuándo y cómo usar Zero-Shot, One-Shot y Few-Shot prompting.
* Diseñar plantillas reutilizables para clonar el estilo de redacción de la firma.
* Taller Práctico: Construcción de prompts para contratos y conceptos iniciales.

---

## El Mito del Oráculo: ¿Por qué falla la IA?

* **La falacia de la omnisciencia:** Creer que la IA "sabe" qué ley aplica o qué estilo prefiere tu firma sin que se lo digas.
* **El costo de la vaguedad:** Un prompt vago (ej. *"Haz un contrato de arrendamiento"*) produce una respuesta genérica, inútil y potencialmente peligrosa.
* **Solución:** Reemplazar el modo "buscador de Google" por el modo "instrucción delegada".

**Notas del Mentor:** *La IA no tiene telepatía jurídica. Piensen en ella como un pasante brillante de primer año: tiene toda la teoría en la cabeza, pero cero contexto sobre tu cliente, tu jurisdicción específica o las sutilezas del caso.*

---

## Cómo Piensa un LLM: Probabilidad Semántica

* **No es una base de datos:** No busca archivos en una carpeta; genera palabras basadas en estadísticas de probabilidad.
* **Predicción de Tokens:** Ante una palabra dada, calcula cuál es la palabra más probable que debería seguir [@surden2019].
* **El sesgo de lo común:** Sin restricciones específicas, la IA siempre elegirá la respuesta más común y genérica de internet.

**Notas del Mentor:** *Comprender esto es clave: la IA no está "razonando" de la misma forma que nosotros. Está completando texto de forma matemática. Nuestro trabajo al redactar un prompt es reducir el espacio de probabilidades a solo las respuestas correctas.*

---

## La Ventana de Contexto: Su Lienzo de Trabajo

* **¿Qué es?:** La cantidad de información que la IA puede "mantener en memoria" durante una sola conversación.
* **Atención y Distracción:** A mayor volumen de información sin estructurar, la IA tiende a ignorar las instrucciones del medio (pérdida en el medio).
* **Uso Eficiente:** Estructurar el contexto con etiquetas claras (ej. `[HECHOS]`, `[CONTRATO]`) para que la IA priorice correctamente.

---

## Los 5 Componentes de un Prompt Legal Efectivo

Para garantizar consistencia y rigor en los entregables, todo prompt profesional debe estructurarse bajo estos 5 pilares [@sal2024]:

1. **Rol:** La identidad y nivel de experiencia asignado a la IA.
2. **Contexto:** Hechos del caso, jurisdicción y antecedentes.
3. **Instrucción/Tarea:** El verbo exacto de lo que debe ejecutar.
4. **Restricciones:** Límites legales, éticos y técnicos.
5. **Formato de Salida:** La estructura visual del entregable.

**Notas del Mentor:** *Memoricen estos 5 elementos. Si falta uno solo, el riesgo de alucinación o de recibir un documento inútil aumenta exponencialmente. Vamos a ver cada uno en detalle.*

---

## Componente 1: El Rol (Asignación de Identidad)

* **¿Por qué importa?:** El rol activa una red semántica específica dentro del modelo. No es lo mismo pedir un concepto como "abogado tributarista" que como "juez de la república".
* **Definición precisa:** Debe incluir jerarquía, especialidad y jurisdicción.
* **Ejemplo Pobre:** *"Eres un abogado."*
* **Ejemplo Elite:** *"Actúa como un Socio de Litigio Civil con 15 años de experiencia en la jurisdicción colombiana."*

---

## Componente 2: El Contexto (El Anclaje a la Realidad)

* **Propósito:** Delimitar el universo de hechos sobre el cual la IA debe operar.
* **Estructura:** Separar los hechos materiales de las opiniones. Usar viñetas o bloques etiquetados.
* **Ejemplo:**
  \begin{lstlisting}[basicstyle=\ttfamily\scriptsize]
  [CONTEXTO DE HECHOS]
  1. Empresa A (arrendador) y Empresa B (arrendatario).
  2. Incumplimiento en el pago del canon por 3 meses consecutivos.
  3. El contrato tiene clausula de resolucion automatica.
  \end{lstlisting}

**Notas del Mentor:** *El contexto debe ser factual y objetivo. Eviten adjetivos innecesarios para que la IA no sesgue el análisis jurídico inicial.*

---

## Componente 3: La Instrucción (El Verbo de Acción)

* **Evitar la ambigüedad:** Usar verbos directos e imperativos.
* **Segmentar la tarea:** Si la tarea es compleja, divídela en pasos secuenciales dentro del mismo prompt.
* **Verbos recomendados:** *Redacta, Analiza, Extrae, Compara, Sintetiza*.
* **Ejemplo:** *"Extrae todas las obligaciones del arrendatario y agrúpalas en obligaciones de hacer y no hacer."*

---

## Componente 4: Restricciones (El Blindaje del Prompt)

* **El escudo contra alucinaciones:** Las restricciones le dicen a la IA qué **NO** hacer.
* **Tipos de restricciones:**
    * **Normativas:** *"Cita únicamente el Código de Comercio colombiano."*
    * **De comportamiento:** *"Si no encuentras una cláusula de indemnidad, escribe 'No detectada'. No asumas su existencia."*
    * **De confidencialidad:** *"No utilices nombres reales de personas naturales."*

**Notas del Mentor:** *Las restricciones son la parte más importante para mitigar riesgos éticos y de negligencia profesional.*

---

## Componente 5: Formato de Salida (El Entregable)

* **Optimización del tiempo:** Ahorra horas de edición manual obligando a la IA a entregar la información formateada para tu uso final.
* **Formatos comunes:**
    * Tabla comparativa con columnas específicas.
    * Memorando ejecutivo con estructura de títulos en Markdown.
    * Listado con viñetas ordenadas de mayor a menor riesgo.
* **Ejemplo:** *"Presenta los riesgos identificados en una tabla con las columnas: Cláusula, Riesgo Asociado, Nivel de Riesgo (Alto/Medio/Bajo), y Redacción Alternativa Sugerida."*

---

## Deconstrucción de Prompts: El Caso Pobre

**Prompt Pobre:**
> *"Revisa este contrato y dime si tiene problemas. Es de un cliente en Bogotá."*

* **¿Por qué fallará?:**
    * **Rol:** No asignado (la IA responderá como un asistente de chat genérico).
    * **Contexto:** Insuficiente (¿qué tipo de contrato?, ¿quién es el cliente?).
    * **Instrucción:** Vaga ("dime si tiene problemas" es subjetivo).
    * **Restricciones:** Cero (riesgo total de inventar leyes de otros países).
    * **Formato:** Libre (probablemente entregará un bloque denso de texto).

---

## Deconstrucción de Prompts: La Alternativa Elite

**Prompt Elite:**
> *[ROL]: Actúa como un abogado especialista en contratos comerciales en Colombia.*
> *[CONTEXTO]: Mi cliente (arrendatario) va a firmar este borrador de contrato de local comercial en Bogotá.*
> *[INSTRUCCIÓN]: Analiza el contrato adjunto e identifica cláusulas abusivas o desequilibradas.*
> *[RESTRICCIONES]: Limita tu análisis al régimen comercial colombiano. No analices vivienda urbana. Si una cláusula es estándar, no la listes.*
> *[FORMATO]: Entrega el resultado en una tabla con: Cláusula analizada, Riesgo para el arrendatario, y Redacción sugerida.*

**Notas del Mentor:** *Comparemos los dos resultados en pantalla. El segundo prompt reduce el tiempo de revisión en un 80% porque el entregable va directo al grano.*

---

## Clasificación del Prompting: Shot Prompting

La forma en que presentamos ejemplos al modelo define la precisión del resultado [@murray2024]:

* **Zero-Shot Prompting:** Cero ejemplos. La IA depende únicamente de su base conceptual general.
* **One-Shot Prompting:** Se incluye un único ejemplo para ilustrar el formato o tono esperado.
* **Few-Shot Prompting:** Se incluyen entre 3 y 5 ejemplos detallados de entrada y salida.

---

## Zero-Shot Prompting en el Derecho

* **Cuándo usarlo:** Para tareas estándar de bajo riesgo cognitivo.
* **Ejemplos idóneos:**
    * Traducir un correo de lenguaje legal técnico a lenguaje ciudadano.
    * Resumir una providencia judicial larga en 5 puntos clave.
    * Extraer nombres de entidades y montos de una demanda.
* **Riesgo:** Alta dependencia del "azar estadístico" del modelo.

---

## One-Shot Prompting en el Derecho

* **Cuándo usarlo:** Cuando el formato de salida es altamente personalizado o específico de tu firma.
* **Dinámica:**
    * *Instrucción:* "Redacta una cláusula de confidencialidad."
    * *Ejemplo:* "Aquí tienes un ejemplo de cómo estructuramos la cláusula en nuestra firma: [Insertar Ejemplo]."
    * *Tarea:* "Ahora, redacta una similar para un contrato de desarrollo de software."

**Notas del Mentor:** *El One-Shot es ideal para estructurar la salida visual (como tablas o encabezados especiales) sin abrumar la ventana de contexto con demasiados tokens.*

---

## Few-Shot Prompting: Clonar el Estilo Jurídico

* **El secreto de la personalización:** Si quieres que la IA escriba conceptos jurídicos que suonen exactamente como tú, debes darle ejemplos de tu trabajo previo exitoso.
* **Cómo estructurarlo:**
    * **Ejemplo 1:** Hechos A $\rightarrow$ Concepto Redactado A.
    * **Ejemplo 2:** Hechos B $\rightarrow$ Concepto Redactado B.
    * **Nueva Entrada:** Hechos C $\rightarrow$ [La IA generará el Concepto C imitando el estilo de A y B].

---

## Few-Shot: Estructura Visual del Prompt

\begin{lstlisting}[basicstyle=\ttfamily\scriptsize]
[EJEMPLO 1]
1. Entrada de hechos: ...
2. Salida de concepto: ...
===
[EJEMPLO 2]
1. Entrada de hechos: ...
2. Salida de concepto: ...
===
[NUEVA TAREA]
1. Entrada de hechos: [Nuevos Hechos de tu Cliente]
2. Salida de concepto:
\end{lstlisting}

*La IA detectará los patrones de puntuación, terminología legal, uso de citas y estructura formal de los ejemplos y los replicará.*

---

## Taller Inicial: Diseña tus Primeros Prompts

**Instrucciones de la Actividad (45 Minutos):**

1. **Seleccionar un reto real:** Ej. Redactar una carta de terminación de contrato laboral con justa causa, o un requerimiento extrajudicial de cobro.
2. **Construir el prompt:** Escribir el prompt utilizando de manera estricta los 5 componentes (Rol, Contexto, Instrucción, Restricciones, Formato).
3. **Prueba y Ajuste:** Ejecutar el prompt en el modelo y documentar las correcciones necesarias en la sección de Restricciones.

**Notas del Mentor:** *Caminen por el aula. Ayuden a los participantes a afinar la sección de 'Restricciones', que suele ser donde los abogados primerizos son demasiado abstractos. Oblíguenlos a ser ultraespecíficos.*

---

## Criterios de Evaluación de un Prompt Legal

Para auditar si tu prompt es de nivel profesional, verifica:

* **¿Es reproducible?:** Si lo ejecutas 3 veces, ¿genera resultados consistentes en estructura y rigor?
* **¿Es agnóstico al modelo?:** ¿Funciona de manera similar en Claude, Gemini y GPT-4?
* **¿Controla la alucinación?:** ¿Contiene directrices de qué hacer ante vacíos de información?

---

## Preguntas y Cierre (Clase 1)

* **Reflexión final:** El prompt engineering no es programación; es el arte de delegar con precisión jurídica.
* **Para la próxima sesión:** Entraremos en técnicas avanzadas de razonamiento secuencial (Chain-of-Thought) y frameworks de estandarización para toda la firma.

**¡Muchas gracias!**

---
