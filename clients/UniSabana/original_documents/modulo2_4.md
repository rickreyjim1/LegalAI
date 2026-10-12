---
title: "Módulo 2.4: Integración Práctica y Ejercicios"
format: revealjs
---
# Módulo 2.4: Integración Práctica y Ejercicios

## Portada

**Título:** Legal Prompting: Integración y Ejercicios Prácticos
**Subtítulo:** Llevando la teoría a la práctica en el entorno legal
**Notas del Mentor:** *¡Bienvenidos a la sesión de consolidación! Hoy pondremos en práctica todo lo aprendido en los módulos 1 y 2 a través de ejercicios intensivos.*

---

## Recap 1: IA y Derecho (Módulo 1)

**La IA no es un oráculo, es un motor probabilístico.**

* **No es Google:** No busca en una base de datos de jurisprudencia; genera la palabra más probable.
* **Orquestación:** Plataformas como Harvey usan sistemas multi-modelo y RAG (Recuperación Aumentada) para no alucinar.
* **Privacidad (Ley 1581):** Usar modelos B2C gratuitos con datos de clientes viola el deber de confidencialidad [@ley1581]. Siempre exige "Zero Data Retention".

---

## Recap 2: El Peligro de la Confianza Ciega

**Mata v. Avianca y las Alucinaciones**

* Abogados sancionados por delegar la investigación sin verificar [@matavavianca].
* **Límites de la IA:** No conoce la ley de ayer ni los hechos no contados.
* **Grounding:** Siempre proporciona a la IA los documentos (ej. el contrato) sobre los cuales basar su respuesta, no dejes que adivine.

---

## Recap 3: Ética y Verificación Legal

**Tu firma es la responsable final.**

* **Protocolo de Verificación:** 1. Subir PDF. 2. Prompt restrictivo. 3. Verificación humana cruzada.
* **Formatos Estructurados:** Pide respuestas en el formato que más les sea de utilidad para evitar ambigüedades.
* **Regla de Oro:** La IA redacta el borrador, el abogado firma la responsabilidad.

---

## Fundamentos del Prompt Legal: Los 5 Pilares (Módulo 2)

Un prompt vago = documento inútil. Todo prompt requiere 5 pilares:

1. **Rol:** Identidad de la IA (Ej. Socio de Litigio en Colombia).
2. **Contexto:** Hechos materiales objetivos y concretos.
3. **Instrucción:** El verbo imperativo (Analiza, Extrae, Compara).
4. **Restricciones:** Límites legales y reglas de qué NO hacer.
5. **Formato:** Salida esperada (Tabla, memo de 2 hojas).

---

## Chain-of-Thought (CoT): Razonamiento Secuencial

**No le pidas la conclusión en el paso 1.**

* Forzar a la IA a "pensar paso a paso" reduce alucinaciones drásticamente [@openai2023].
* **Instrucción:** "Antes de dar tu veredicto, califica las pruebas, luego analiza la norma, y finalmente concluye."
* **Break the Task Down:** Divide la tarea en Extracción -> Análisis -> Redacción.

---

## Clonando tu Estilo (Few-Shot Prompting)

**La IA debe escribir como tu firma, no como un robot genérico.**

* **Zero-Shot:** Cero ejemplos. Tareas simples (ej. traducir idioma).
* **One-Shot:** Un ejemplo para definir formato.
* **Few-Shot:** 3 a 5 ejemplos de entrada y salida para imitar tu tono, estilo y terminología legal.
* "Aquí tienes un ejemplo de cómo redactamos los conceptos en la firma..."

---

## Frameworks de Estandarización: CARE y ADP

Sistemas para que toda la firma use IA con el mismo rigor.

* **CARE (Conceptos):** Contexto, Acción, Resultado, Evaluación.
* **ADP (Auditoría):** Actor, Documento, Propósito.
* Útil para redactar memorandos y revisar cláusulas contractuales sistemáticamente.

---

## Red Teaming Legal: El Blindaje

**La auditoría cruzada de los argumentos.**

* Una vez que la IA redacte tu documento, no asumas que es perfecto.
* **Prompt de Red Teaming:** "Ahora actúa como el abogado de la contraparte. Encuentra 3 puntos débiles en tu propia respuesta y dime cómo los atacarías."
* Permite anticipar riesgos antes de enviar el documento.

---

## Ejercicio 1: Los 5 Pilares (Civil)

**Revisión de Contrato Civil**
*Encuentren los hechos completos en el Handout (Caso 1).*

**Tu Reto:** Construye un prompt usando estrictamente los 5 Pilares (Rol, Contexto, Instrucción, Restricciones, Formato).
**Objetivo:** Pedir a la IA que identifique si existe un riesgo de resolución contractual por el incumplimiento de una cláusula específica.

---

## Ejercicio 2: 5 Pilares + CoT + Few-Shot + CARE (Laboral)

**Concepto de Despido Injustificado**
*Encuentren los hechos completos en el Handout (Caso 2).*

**Tu Reto:** Usando el Framework CARE, diseña un prompt que:

1. Obligue a la IA a usar Chain-of-Thought (pensar paso a paso).
2. Incluya ejemplos de tono (Few-Shot).
   **Objetivo:** Determinar la probabilidad de éxito de una demanda laboral.

---

## Ejercicio 3: 5 Pilares + CoT + ADP + Red Team (Contratación)

**Auditoría de Cláusula de Indemnidad**
*Encuentren los hechos completos en el Handout (Caso 3).*

**Tu Reto:** Usando el Framework ADP y CoT, diseña un prompt para auditar el contrato. Una vez que la IA responda, aplica un segundo prompt de Red Teaming.
**Objetivo:** Identificar penalidades unilaterales y luego atacar la propia respuesta como la contraparte.

---

## Ejercicio 4 (Para llevar): Framework TAM

**Requerimiento Extrajudicial (Técnica TAM)**
*Encuentren los detalles en el Handout (Caso 4).*

**Tu Reto:** Este ejercicio explora la técnica TAM (Tarea, Audiencia, Método), ideal para redacción y comunicación.
Diseña un prompt combinando los 5 Pilares con TAM para redactar un correo persuasivo de cobro comercial que conserve la relación con el cliente.

---

## ¡Sigamos en Contacto!

La Inteligencia Artificial avanza todos los días. ¡No duden en escribirme para compartir ideas, resolver dudas o seguir conversando sobre cómo la IA puede transformar su práctica jurídica!

* **WhatsApp:** (57) 3012726157
* **Email:** [rareyesj@gmail.com](mailto:rareyesj@gmail.com)

**Recursos Adicionales:**

* **Carpeta Compartida Google Drive:** https://drive.google.com/drive/folders/1qvTiL9MJnudELF89Zx9FbQrBMV0nDXa-?usp=sharing
* **Página (Dr. Rodolfo Meza):**

  * [d2poah66c6bwvj.cloudfront.net/](https://d2poah66c6bwvj.cloudfront.net/legal-prompting/anatomia-prompt)

    * Usuario: unisabana
    * Contraseña: leg4la1

**¡Muchas gracias por su participación!**
