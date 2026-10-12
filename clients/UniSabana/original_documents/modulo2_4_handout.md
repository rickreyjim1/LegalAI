# Handout - Ejercicios Prácticos (Módulo 2.4)

Este documento contiene los hechos, contextos simulados y requisitos para resolver los ejercicios propuestos en el Módulo 2.4. Úsalo como material de insumo (Grounding) para tus prompts.

---

## Ejercicio 1: Los 5 Pilares (Civil - Revisión de Contrato)

**Contexto del Caso (Hechos para tu Prompt):**
Tu cliente, "Inversiones ABC", firmó un contrato civil de compraventa de un lote comercial con "Constructora XYZ". El contrato establecía el pago en 3 cuotas. La segunda cuota se retrasó 5 días por un problema bancario. La Constructora XYZ ha enviado una notificación de resolución automática del contrato basándose en la Cláusula 8.

**Cláusula 8 del Contrato:** "El retraso superior a 3 días calendario en el pago de cualquier cuota dará derecho al vendedor a resolver de plano este contrato sin necesidad de requerimiento judicial previo."

**Tu Misión:** 
Redactar un prompt utilizando los 5 Pilares (Rol, Contexto, Instrucción, Restricciones, Formato) para que la IA evalúe si la cláusula 8 es aplicable o si constituye abuso del derecho según la jurisprudencia civil colombiana. 

---

## Ejercicio 2: 5 Pilares + CoT + Few-Shot + CARE (Laboral)

**Contexto del Caso (Hechos para tu Prompt):**
El empleado "Juan Pérez", que lleva 3 años en la empresa, fue despedido alegando "justa causa" debido a ausencias reiteradas. Sin embargo, Juan afirma que las ausencias fueron por calamidad doméstica comprobada, pero el departamento de RRHH nunca revisó sus soportes médicos y no se hizo un proceso disciplinario previo. 

**Tu Misión:**
Usando el esquema CARE (Contexto, Acción, Resultado, Evaluación), redacta un prompt que obligue a la IA a realizar un análisis secuencial (Chain-of-Thought) antes de dar el veredicto sobre si el despido fue legal. Además, incluye al menos un ejemplo (Few-Shot) de cómo quieres que redacte la respuesta final (ej. "En nuestra firma, siempre concluimos con un subtítulo de Recomendación Estratégica: ...").

---

## Ejercicio 3: 5 Pilares + CoT + ADP + Red Team (Contratación)

**Contexto del Caso (Hechos para tu Prompt):**
Representas al "Proveedor P" (una PYME de tecnología). Le están pidiendo firmar un contrato de servicios con "Megacorporación S.A.". 

**Cláusula 12 (Indemnidad):** "El Proveedor se obliga a mantener indemne a Megacorporación S.A. por cualquier daño directo, indirecto, lucro cesante o daño reputacional derivado de cualquier interrupción del servicio de software, sin límite de cuantía."

**Tu Misión:**
1. **Fase 1 (ADP):** Usa el framework ADP (Actor, Documento, Propósito) y CoT para auditar la Cláusula 12, indicando por qué es desproporcionada y proponiendo una nueva redacción con un límite de responsabilidad (cap).
2. **Fase 2 (Red Teaming):** Una vez que la IA proponga la nueva redacción mitigada, envíale un segundo prompt ordenándole actuar como el abogado de Megacorporación S.A., pidiéndole que ataque tu nueva redacción y encuentre 3 razones para rechazarla.

---

## Ejercicio 4 (Para llevar): Framework TAM (Comunicación / Comercial)

**Contexto del Caso (Hechos para tu Prompt):**
Tu firma de abogados debe enviar un requerimiento de pago a "Distribuidora El Sol", un cliente histórico de tu representado "Fábrica La Luna". La deuda es de \$50,000,000 COP y tiene 60 días de mora. El objetivo es cobrar el dinero rápidamente pero **sin destruir la relación comercial de 10 años**.

**Tu Misión:**
Aplica el framework TAM (Tarea, Audiencia, Método) dentro de un prompt para que la IA redacte el correo electrónico perfecto.
- **Tarea:** Solicitar el pago de la deuda.
- **Audiencia:** El Gerente General de "Distribuidora El Sol" (relación amistosa pero profesional).
- **Método:** Correo electrónico persuasivo, conciliador pero firme, proponiendo un acuerdo de pago.
