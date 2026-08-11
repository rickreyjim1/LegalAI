# Módulo 1.2: Profundización

**Título:** Transformación de la Práctica Jurídica
**Subtítulo:** Lo que la IA sí puede (y no puede) hacer

---

## Introducción al Módulo 1.2

Este módulo profundiza en cómo la Inteligencia Artificial Generativa está cambiando la práctica jurídica diaria, estableciendo qué tareas pueden delegarse de manera segura y cuáles son los límites técnicos actuales.

---

## Ética y Uso Responsable (Gemini)

El análisis de documentos legales con IA exige un estándar ético riguroso:

* **Privilegio Abogado-Cliente:** El abogado sigue siendo el garante del secreto profesional.
* **Sesgos y Equidad:** La IA puede heredar sesgos de sus datos de entrenamiento.
* **Responsabilidad de Uso (Gemini):** Se debe usar como asistente y no como tomador de decisiones. El output debe ser siempre revisado por un humano.

---

## Creación de Prompts Estructurados

¿Por qué usar formatos estructurados en vez de texto plano?

El texto plano requiere lectura humana para interpretar dónde empieza y termina un dato. Los formatos estructurados permiten que otras herramientas informáticas extraigan la información automáticamente sin errores.

* **JSON (JavaScript Object Notation):** Formato universal basado en "llave: valor". Ideal para extraer metadatos puros (ej. `{"vencimiento": "2024-12-31"}`).
* **.MD (Markdown):** Formato de texto con marcas ligeras (como `\#` para títulos o `*` para listas). Ideal para generar borradores de documentos legales o memos que mantengan formato de lectura fácil.

**Ejemplo:** *"Extrae las fechas de vencimiento y preséntalas en un JSON estructurado por partes involucradas."*

---

## Ejemplo de Salida: JSON vs .MD

\begin{columns}[T]
\begin{column}{0.48\textwidth}
\textbf{Salida en JSON}
\begin{lstlisting}[basicstyle=\ttfamily\scriptsize]
{
  "contrato": {
    "tipo": "[Ej: Arrendamiento]",
    "partes": [
      "[Nombre Parte 1]",
      "[Nombre Parte 2]"
    ],
    "vencimiento": "YYYY-MM-DD",
    "penalidad": "[Resumen]"
  }
}
\end{lstlisting}
\end{column}

\begin{column}{0.48\textwidth}
\textbf{Salida en Markdown}
\begin{lstlisting}[basicstyle=\ttfamily\scriptsize]
### Datos del Contrato
* **Tipo:** [Ej: Arrendamiento]

### Partes Involucradas
1. [Nombre Parte 1]
2. [Nombre Parte 2]

### Fechas y Condiciones
* **Vencimiento:** YYYY-MM-DD
* **Penalidad:** [Resumen]
\end{lstlisting}
\end{column}
\end{columns}

---

## Privacidad: ¿A dónde va la información?

El uso de modelos gratuitos (como ChatGPT o Gemini básico) conlleva riesgos de privacidad:

* **Modelos Gratuitos:** Por defecto, los datos ingresados (prompts) **pueden ser utilizados** para entrenar futuras versiones del modelo [@geminiprivacy].
* **Pérdida de Confidencialidad:** Introducir datos reales de un cliente en estas versiones viola los deberes éticos.
* **Solución:** Utilizar versiones **Enterprise/Corporativas**, modelos locales, o desactivar explícitamente el uso de datos para entrenamiento.

---

## Recapitulemos

![¿Cómo te sientes?](Images/Slido1.png)

[https://app.sli.do/event/225ytceXVMF9WqQb2yXQcp](https://app.sli.do/event/225ytceXVMF9WqQb2yXQcp)

---

## Lo que la IA SÍ puede (y NO puede) hacer

| Tarea Jurídica                               | Nivel de Riesgo | Recomendación                                       |
| --------------------------------------------- | --------------- | ---------------------------------------------------- |
| Redacción de correos y memos simples         | Bajo            | Uso rutinario con supervisión básica               |
| Búsqueda de jurisprudencia en bases abiertas | Alto            | NO RECOMENDADO (Riesgo de alucinación)              |
| Resumen de expedientes largos                 | Medio           | Ideal para IA, validando contra el PDF original      |
| Análisis predictivo de sentencias            | Alto            | Requiere herramientas especializadas (ej. Lexis+ AI) |

**Notas del Mentor:** *Discutir con el grupo las implicaciones de delegar la investigación jurídica. Referencia clave: Surden (2019) [@surden2019] sobre los límites de la IA en el razonamiento deductivo.*

---

## Sondeo

![Usos posibles](Images/Slido2.png)

[https://app.sli.do/event/d4t1CEhzQVnvahXucVLCqT](https://app.sli.do/event/d4t1CEhzQVnvahXucVLCqT)

---

## Casos de Uso Reales en la Práctica

* **Investigación y Análisis Legal:** Utilizar la IA para encontrar patrones en grandes volúmenes de documentos, no para buscar la "verdad" legal.
* **Revisión de Contratos:** Identificar cláusulas faltantes o riesgosas (Ej. cláusulas de indemnidad asimétricas).
* **Orientación a Clientes:** Redactar respuestas iniciales en lenguaje claro y accesible.
* **Gestión Documental:** Extracción de metadatos (fechas, partes, montos) de expedientes masivos.

---

## El Peligro de la Confianza Ciega (Mata v. Avianca)

**El puente entre el potencial y el riesgo:**

En 2023, abogados en EE. UU. usaron ChatGPT para investigar jurisprudencia y presentaron un escrito con casos que la IA **inventó (alucinó)** [@matavavianca].

* Fueron sancionados por el juez.
* Demostró que delegar la investigación sin verificación es negligencia profesional grave.

---

## Límites Críticos de la IA Generativa

* **Falta de Actualización:** Los modelos fundacionales tienen una fecha de corte de conocimiento. No conocen la ley aprobada ayer.
* **Falta de Hechos Específicos:** La IA no conoce el contexto único de su cliente a menos que usted se lo proporcione.
* **Alucinaciones:** La tendencia de la IA a inventar respuestas plausibles pero falsas cuando no tiene información suficiente.

**Notas del Mentor:** *Recordar la Ley 1581 de 2012 [@ley1581]. Introducir datos del cliente para "darle contexto" a la IA en herramientas gratuitas es una violación a la privacidad.*

---

## Protocolo de Verificación Legal

* **Grounding (Anclaje):** Proporcionar a la IA los documentos fuente sobre los cuales debe basar su respuesta.
* **Prompts Restrictivos:** Instruir explícitamente a la IA: "Responde ÚNICAMENTE basado en los documentos adjuntos".
* **Verificación Humana:** El abogado siempre debe revisar el documento final. La responsabilidad legal recae en el humano.

---

## Flujo de Verificación (Ejemplo Práctico)

\begin{center}
\resizebox{0.9\textwidth}{!}{
\begin{tikzpicture}[node distance=3cm, auto, thick,
    box/.style={rectangle, draw=blue!80, fill=blue!10, very thick, text width=3.5cm, align=center, rounded corners, minimum height=1.5cm},
    arrow/.style={->, >=stealth, very thick, blue!80}]
    \node[box] (n1) {1. Subir PDF del Contrato (Grounding)};
    \node[box, right of=n1, xshift=1.5cm] (n2) {2. Prompt restrictivo con formato JSON};
    \node[box, right of=n2, xshift=1.5cm] (n3) {3. Verificar JSON contra original};
    \draw[arrow] (n1) -- (n2);
    \draw[arrow] (n2) -- (n3);
\end{tikzpicture}
}
\end{center}

---

## Tu Opinión

![Ética y Responsabilidad](Images/Slido3.png)

[https://app.sli.do/event/9jutLvGy9zr5HcmKtmq1nd](https://app.sli.do/event/9jutLvGy9zr5HcmKtmq1nd)

---

## Ejercicio Práctico: Grounding con NotebookLM

**Herramienta:** Gemini Notebook [@notebooklm2024]

**Objetivo:** Interactuar con un expediente masivo sin riesgo de alucinaciones.

* Subir la sentencia o expediente en PDF.
* Generar una guía de estudio automática.
* Hacer preguntas específicas al documento.
* Verificar las citas (Gemini Notebook muestra de qué página extrajo la información).

**Notas del Mentor:** *Realizar demostración en vivo. Mostrar cómo al hacer una pregunta fuera del documento, la herramienta responde "No se encuentra en las fuentes", comportamiento ideal en LegalTech.*

---

## ¡Sigamos en Contacto!

La Inteligencia Artificial avanza todos los días. ¡No duden en escribirme para compartir ideas, resolver dudas o seguir conversando sobre cómo la IA puede transformar su práctica jurídica!

* **WhatsApp:** (57) 3012726157
* **Email:** [rareyesj@gmail.com](mailto:rareyesj@gmail.com)

**¡Muchas gracias por su participación!**
