---
title: "Módulo 1: IA y Derecho: Todo lo que necesitas saber antes de empezar"
format: revealjs
---
# Módulo 1: IA y Derecho: Todo lo que necesitas saber antes de empezar (Grupo Alto)

## Portada

**Título:** IA y Derecho: Todo lo que necesitas saber antes de empezar
**Subtítulo:** De Modelos Fundacionales a Estrategia Legal (Módulo 1)
**Notas del Mentor:** *¡Hola, equipo! Al ser el grupo 'Alto', asumo que ya han interactuado con IA. Mi objetivo hoy no es enseñarles a abrir ChatGPT, sino entender cómo está estructurada la tecnología por debajo (sin código), para que tomen decisiones estratégicas como líderes de la firma.* [Dinámica: Pregunta de apertura: '¿Cuál fue la última tarea legal que intentaron delegar a una IA y falló?']

---

## Objetivos de la Sesión 

* Entender la arquitectura tecnológica moderna (2026): IA Generativa vs Tradicional.
* Orquestación: Por qué las plataformas legales usan múltiples modelos a la vez.
* Adopción real: Qué funciona hoy en Colombia y el mundo.
* Casos de uso inmediatos y herramientas clave (Harvey, Lexis+AI, Claude, etc.).
* Gestión de Riesgos: Privacidad y Propiedad Intelectual.

---

## Desmitificando la Tecnología (El "Matryoshka" de la IA)

**Conceptos Fundamentales:**

* **Inteligencia Artificial (IA):** Máquinas replicando capacidades cognitivas.
* **Machine Learning & Deep Learning:** Aprendizaje a partir de datos históricos mediante redes neuronales.
* **IA Generativa y LLMs (Large Language Models):** Modelos estadísticos avanzados que predicen lenguaje. No "piensan" como abogados, calculan probabilidades semánticas.

**Notas del Mentor:** *Aclaración clave: La IA no es una base de datos ni un buscador perfecto. Es un motor de razonamiento probabilístico. Si lo usan como Google, fallará.* [Dinámica: Ejercicio de comparación entre buscar en LexisNexis tradicional vs. consultar a un LLM].

---

## El "Matryoshka" de la IA (Visual)

![Matryoshka de la IA](Images/matryoshka_ai_1785900912673.png)

---

## Evolución 2026: De Modelos Solos a Sistemas Orquestados

**¿Cómo funciona una plataforma LegalTech de alto nivel (ej. Harvey o Lexis+AI)?**

* **No es un solo modelo:** No le hablan a un único 'cerebro'.
* **Sistemas Multi-Modelo:** Hay un modelo que lee tu pregunta (Router), otro especializado en extraer leyes, otro en razonar el caso, y otro que redacta el texto final.
* **RAG (Generación Aumentada por Recuperación):** La IA consulta la base de datos de jurisprudencia de la firma *antes* de responder, eliminando alucinaciones [@relativity2024].

**Notas del Mentor:** *Explicar esto a abogados: Piensen en un despacho. El modelo 'Router' es el socio que recibe el caso; se lo pasa al paralegal (modelo de búsqueda de jurisprudencia); el paralegal le da los documentos al asociado senior (modelo de razonamiento legal) quien redacta el concepto. La IA moderna es todo el despacho trabajando en segundos.* [Pregunta: ¿Cómo ven esto aplicado a su departamento de litigios?]

---

## Automatización vs. Inteligencia Artificial

**El Cambio en el Despacho**

* **RPA (Tradicional):** Macros, flujos rígidos. (`SI A $\rightarrow$ ENTONCES B`). Falla si el documento cambia.
* **IA Generativa:** Interpreta contexto. Puede leer un correo furioso, entender la intención, y redactar una respuesta conciliatoria.

**Notas del Mentor:** *La RPA es el tren (sigue las vías). La IA Generativa es un vehículo todoterreno. El abogado debe saber cuándo usar cuál.*

---

## RPA vs IA Generativa (Visual)

![RPA vs IA Generativa](Images/rpa_vs_genai_1785900922553.png)

---

## Casos de Uso de Alto Impacto y Herramientas (2026)

| Herramienta    | Caso de Uso Principal                         | Sitio Web                                                                     | Referencia           |
| -------------- | --------------------------------------------- | ----------------------------------------------------------------------------- | -------------------- |
| Harvey AI      | Investigación y Análisis Complejo           | [harvey.ai](https://www.harvey.ai/)                                            | [@harvey2024]        |
| Lexis+ AI      | Investigación Jurídica y Jurisprudencia     | [lexisnexis.com](https://www.lexisnexis.com/en-us/products/lexis-plus-ai.page) | [@lexis2024]         |
| Luminance      | Due Diligence y Revisión de Contratos        | [luminance.com](https://www.luminance.com)                                     | [@luminance2024]     |
| vLex           | Inteligencia Legal Global y Derecho Comparado | [vlex.com](https://vlex.com)                                                   | [@vlex2024]          |
| CoCounsel      | Asistente Legal Integrado (Casetext/TR)       | [casetext.com](https://legal.thomsonreuters.com/en/casetext)                   | [@cocounsel2024]     |
| Spellbook      | Redacción y Revisión en Microsoft Word      | [spellbook.legal](https://www.spellbook.legal)                                 | [@spellbook2024]     |
| Clearbrief     | Verificación de Hechos y Escritos Judiciales | [clearbrief.com](https://clearbrief.com)                                       | [@clearbrief2024]    |
| Relativity aiR | E-Discovery y Revisión Documental Masiva     | [relativity.com](https://www.relativity.com/data-solutions/ai/)                | [@relativityair2024] |
| Everlaw        | Gestión de Litigios e Investigaciones        | [everlaw.com](https://www.everlaw.com)                                         | [@everlaw2024]       |
| Ironclad AI    | Gestión del Ciclo de Vida de Contratos (CLM) | [ironcladapp.com](https://ironcladapp.com)                                     | [@ironclad2024]      |

**Notas del Mentor:** *Aquí nos detenemos. Quiero escuchar qué herramientas tienen implementadas. Vamos a analizar por qué NotebookLM es el secreto mejor guardado para litigantes con expedientes de 5,000 páginas.* [Actividad: Demostración rápida de cómo NotebookLM cruza información de 3 PDFs].

---

## Adopción Real: Colombia y el Resto del Mundo

* **Tendencia Global:** Las firmas ya no evalúan "si" usar IA, sino "cómo" integrarla en flujos (Word, Teams) y medir el ROI [@thomsonreuters2024].
* **Colombia / LatAm:** Transición de pilotos a infraestructura base. Los clientes empiezan a exigir eficiencias basadas en IA en la facturación (Adiós al modelo de horas facturables en tareas repetitivas).

**Notas del Mentor:** *Debate: ¿Están sus clientes dispuestos a pagarles por 10 horas de revisión de contratos si saben que una IA lo hace en 5 minutos? ¿Cómo cambia su modelo de negocio?*

---

## La IA: ¿Amiga o Enemiga? (Visual)

![IA en el Entorno Laboral](Images/ia_amiga_enemiga.png)

---

## Gestión de Riesgos: Privacidad (Ley 1581)

* **El Error de Novato:** Subir contratos con datos personales a ChatGPT gratuito.
* **El Riesgo Inminente:** Transmisión internacional de datos no autorizada, violación de confidencialidad cliente-abogado.
* **Soluciones Empresariales:** Licencias "Zero Data Retention" (Copilot Enterprise, Claude Team, Harvey). Sus datos no entrenan al modelo público.

**Notas del Mentor:** *Regla de oro para el grupo: Nunca usar herramientas gratuitas B2C con datos de clientes. Mostrar cómo verificar la política de retención de datos de una IA.*

---

## Bóveda de Privacidad (Visual)

![Bóveda de Privacidad Zero Data](Images/privacy_vault_1785900930775.png)

---

## Privacidad en Herramientas Gratuitas (Opt-Out)

**Si su equipo usa cuentas gratuitas, la IA se entrena con sus datos por defecto.** Cómo desactivarlo:

* **ChatGPT:** *Settings* $\rightarrow$ *Data Controls* $\rightarrow$ Apagar *"Improve the model for everyone"*.
* **Claude:** *Settings* $\rightarrow$ *Privacy* $\rightarrow$ Apagar *"Help improve Claude"*.
* **Gemini:** *myactivity.google.com* $\rightarrow$ *Gemini Apps Activity* $\rightarrow$ Seleccionar *"Turn off"*.

**IMPORTANTE - ADVERTENCIA LEGAL (Ley 1581/2012):** Incluso con el *Opt-Out*, subir Datos Personales o Secreto Profesional a entornos B2C gratuitos puede constituir una Transmisión Internacional de Datos no autorizada. La falta de debida diligencia conlleva severas sanciones de la SIC y violaciones a la ética profesional.

---

## Riesgos: Propiedad Intelectual y 'Alucinaciones'

* **Derechos de Autor (DNDA):** El producto de la IA no es protegible por derecho de autor sin intervención humana sustancial.
* **Human-in-the-Loop:** La IA no reemplaza la responsabilidad ética y civil del abogado. La supervisión es obligatoria.

**Notas del Mentor:** *Recordar casos famosos de abogados sancionados por presentar jurisprudencia falsa. La IA es el borrador, el abogado es la firma autorizada.* [Cierre del Día 2: Taller de políticas internas de uso de IA].

---

## Los Desafíos de la IA (Visual)

![Desafíos y Auditoría de la IA](Images/desafios_ia.png)

---

## Taller de Cierre: La Política de IA de su Firma

* **Actividad en Grupos:** Diseñar los 3 pilares de la política de uso de IA para sus equipos (Qué se permite, qué herramientas, y qué flujos de revisión).
* **Debrief & Mentoría.**
