---
title: "Módulo 3: PromptLibrary Jurídica"
format: revealjs
background_image: Images/UniSabana.jpg
---

# Módulo 3: Sesión 1

## Portada
**Título:** PromptLibrary Jurídica (Sesión 1)
**Subtítulo:** Qué es y por qué es la herramienta que más tiempo te va a ahorrar
**Notas del Mentor:** *¡Bienvenidos al Módulo 3! Ya aprendimos a usar la IA, ahora vamos a convertir ese conocimiento individual en un activo para toda la organización. Empezaremos a construir infraestructura.*

---

## Objetivos de la Sesión 1
* Entender qué es una PromptLibrary corporativa.
* Reconocer cómo soluciona los "silos de conocimiento".
* Aprender la anatomía de un "Blueprint" o plantilla reutilizable.
* Diseñar colaborativamente nuestros primeros prompts prácticos según nuestro rol (Litigio, Asesoría, Sector Público).
* Ejecutar y guardar nuestros primeros Blueprints en vivo.

---

## La cruda realidad del trabajo manual
* Cada día, decenas de abogados en una firma realizan las mismas tareas: revisar cláusulas de indemnidad, resumir contestaciones de demanda, buscar jurisprudencia.
* **El costo:** Horas repetitivas que el cliente ya no quiere pagar.
* **El riesgo:** Errores humanos por fatiga en tareas mecánicas.

---

## ¿Qué es una PromptLibrary?
* **Definición:** Un repositorio centralizado, probado, documentado y categorizado de instrucciones (prompts) listas para usar por cualquier miembro del equipo.
* **Analogía Legal:** Es el equivalente al "banco de modelos y minutas" de la firma, pero para comunicarse con la Inteligencia Artificial.

---

## El Problema: "Ceguera del Prompt"
* Un asociado junior gasta 40 minutos experimentando hasta lograr que ChatGPT o Gemini genere un resumen perfecto de un expediente de 500 páginas.
* Logra su objetivo, cierra la pestaña y vuelve al trabajo.
* **Resultado:** Ese conocimiento (el prompt perfecto) se evaporó. Mañana, otro abogado empezará desde cero.

---

## La Solución: Escalar el Conocimiento
* Si el asociado documenta ese prompt exitoso en la PromptLibrary...
* Los otros 50 abogados de la firma lo usarán mañana, reduciendo los 40 minutos de ensayo y error a 10 segundos.
* **El verdadero ROI de la IA no está en el uso individual, sino en el uso institucional.**

---

## El Concepto de "Blueprint" (Plantilla)
* Un *Blueprint* es un prompt parametrizado. No es un texto estático, sino un esqueleto o fórmula que permite sustituir variables.
* **Ejemplo Estático (Malo):** *"Resume este contrato de arrendamiento de la calle 45."*
* **Ejemplo Blueprint (Bueno):** *"Actúa como abogado senior. Resume el siguiente [TIPO DE CONTRATO] enfocándote en [PUNTOS CLAVE A BUSCAR]. Contrato: [TEXTO]"*

---

## Anatomía de un Prompt Reutilizable
Todo buen *Blueprint* en su biblioteca debe tener al menos 4 elementos documentados:
1. **Nombre y Rol:** Ej. *Analista de Due Diligence M&A*.
2. **Contexto Base:** La instrucción inmutable (instrucciones de tono y formato).
3. **Variables (Corchetes):** Los espacios que el usuario final debe rellenar.
4. **Restricciones:** Lo que la IA *nunca* debe hacer en este caso.

---

## Variables Clave (El poder de los corchetes)
El secreto de la PromptLibrary es usar corchetes `[ ]` para guiar al abogado usuario:
* `[TIPO DE DOCUMENTO]`
* `[JURISDICCIÓN]`
* `[ROL DEL CLIENTE: Arrendador/Arrendatario]`
* `[TEXTO DEL EXPEDIENTE A PEGAR]`

---

## Diferenciando por Rol: Litigio
**Casos de uso para Blueprints en Litigio:**
* **Extracción de Hechos:** Extraer cronologías exactas a partir de correos cruzados.
* **Identificación de Inconsistencias:** Cruzar el interrogatorio del testigo con su declaración juramentada previa.
* **Borradores:** Esquematizar la estructura de una contestación de demanda basándose en los hechos alegados.

---

## Diferenciando por Rol: Asesoría Corporativa
**Casos de uso para Blueprints en Asesoría (Corporate/M&A):**
* **Red-Flagging:** Búsqueda rápida de cláusulas de cambio de control, exclusividad o penalidades en un *Data Room*.
* **Resúmenes Ejecutivos:** Transformar un documento técnico de 40 páginas en un memo de 2 páginas para la junta directiva.
* **Traducción Legal:** Adaptar un contrato con jerga de Common Law a conceptos del derecho civil local.

---

## Diferenciando por Rol: Sector Público
**Casos de uso para Blueprints en Sector Público:**
* **Derechos de Petición:** Analizar las pretensiones del ciudadano y compararlas con las plantillas de respuesta de la entidad.
* **Licitaciones:** Verificación cruzada (checklist) de cumplimiento de requisitos habilitantes en propuestas de miles de páginas.
* **Proyección de Fallos:** Estructuración de los antecedentes y consideraciones iniciales.

---

## Herramientas para empezar HOY
**No necesitas software de $10,000 USD para arrancar (Fase 1)**
* La fricción mata la innovación. Si el sistema es complejo, nadie lo usará.
* **Recomendación:** Empezar hoy mismo con un documento colaborativo (Word Online, Excel, Google Sheets o Notion).
* Lo importante no es la plataforma, es la disciplina de documentar el *Blueprint*.

---

## Demo: Así se ve una Versión 1.0
*(El Mentor muestra un Excel en pantalla)*
* **Columna A:** Nombre del Prompt.
* **Columna B:** Caso de uso.
* **Columna C:** Blueprint (con variables en negrita).
* **Columna D:** Autor / Fecha.
* **Columna E:** Eficacia estimada (Del 1 al 5).

---

## Taller Práctico (Fase 1): Identificación
**Trabajo en grupos por roles (15 minutos)**
1. Reúnanse con colegas de áreas de práctica similares.
2. Identifiquen **UNA** tarea repetitiva, aburrida y de bajo valor estratégico que realicen todas las semanas.
3. Definan el objetivo exacto que quieren que la IA logre.

---

## Taller Práctico (Fase 2): Redacción del Blueprint
**Redacción (20 minutos)**
1. Utilizando los frameworks del Módulo 2 (CARE/TAM), escriban el *Blueprint* maestro.
2. Asegúrense de usar corchetes `[ ]` para las partes que cambian caso a caso.
3. Incluyan restricciones claras (ej. "Usa viñetas, no uses lenguaje poético, omite saludos").

---

## Taller Práctico (Fase 3): Pruebas de Fuego
**Ejecución en Vivo (20 minutos)**
1. Abran su asistente de IA (ChatGPT, Gemini, Claude).
2. Copien su *Blueprint*, llenen los corchetes con un caso real (anonimizado) y ejecútenlo.
3. ¿El resultado fue perfecto a la primera? (Spoiler: Casi nunca lo es). Anoten qué falló.

---

## Cierre de Sesión 1
* Hoy pasamos del conocimiento tácito al conocimiento documentado.
* Ya tienen en sus manos su primer activo institucional: un Blueprint funcional.
* **Para la próxima sesión:** Veremos cómo refinar estos prompts que fallaron, cómo compartirlos y cómo escalar este Excel a un sistema institucional a prueba del tiempo. ¡Guarden sus archivos!
