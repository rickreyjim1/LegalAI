---
title: "Module 2: Basic Prompt Engineering"
subtitle: "Key Frameworks for EMs"
author: "Ricardo Reyes-Jimenez"
institute: "Capgemini"
---

## Session Objective

**By the end of this module, the Engagement Manager will be able to:**

1. Stop communicating with MS Copilot as if it were a search engine.
2. Structure robust prompts using the **5 Pillars Framework**.
3. Apply the **TAM Framework** (Task, Audience, Method) to draft precise stakeholder communications.

---

## 1. The Search Engine Fallacy

**AI is not Google. It does not retrieve; it reasons (statistically).**

* **Google Search:** "Capgemini change request template" (Keywords).
* **MS Copilot:** "Act as a Capgemini Delivery Executive. Draft a formal Change Request for a client who added 3 new reporting dashboards to the scope. Use a diplomatic but firm tone." (Context + Intent).

**Rule of Thumb:** If your prompt is shorter than a Tweet (280 characters), you are likely under-utilizing the AI and risking hallucinations.

---

## 2. The 5 Pillars of Prompting

A vague prompt yields a useless document. Every professional prompt requires 5 pillars:

1. **Role:** Identity of the AI (e.g., Senior Engagement Manager).
2. **Context:** Objective and concrete material facts (Project status, client mood).
3. **Instruction:** The imperative verb (Analyze, Extract, Compare).
4. **Constraints:** Business limits and rules of what NOT to do.
5. **Format:** Expected output (Table, 2-page memo, bullet points).

---

## Exercise 1: The 5 Pillars Makeover

**Context:** Your junior PM asked Copilot: *"Write an email asking for a meeting agenda."* The result was generic and unprofessional.
**Task:** Rewrite this prompt using the 5 Pillars.

* **Draft Prompt to Try:**
  *"[ROLE] Act as an IT Project Manager. [CONTEXT] We have a SteerCo meeting tomorrow with the client's CIO, but they haven't sent the agenda topics yet. [INSTRUCTION] Draft a polite email requesting the agenda. [CONSTRAINTS] Do not sound accusatory; keep it under 3 paragraphs. [FORMAT] Output the email with a clear subject line."*

---

## 3. The TAM Framework

For persuasive communication, structuring the *Why* is as important as the *What*.

* **T - Task:** What exactly needs to be done? (e.g., Explain a 2-week delay).
* **A - Audience:** Who is reading this? What is their technical level and emotional state? (e.g., Non-technical CFO, highly frustrated).
* **M - Method:** How should the information be delivered? (e.g., Executive summary followed by a mitigation plan).

---

## Exercise 2: Using TAM for Difficult Emails

**Context:** The offshore development team missed a critical deadline. You need to inform the client's VP of Engineering without damaging the relationship.
**Task:** Use the TAM framework in MS Copilot to draft the communication.

* **Draft Prompt to Try:**
I need to send an email about a missed deadline. 
**Task:** Explain that the offshore team was delayed by 3 days due to unexpected server downtime, but we are allocating weekend resources to catch up. 
**Audience:** The client's VP of Engineering (technical, results-oriented, currently frustrated). 
**Method:** A direct, professional email starting with the bad news, immediately followed by the mitigation plan, using bullet points for clarity.

---

## Recap & Next Session

**Today we learned:**
- Stop using keywords; start providing context.
- The **5 Pillars** guarantee structured, predictable outputs.
- The **TAM Framework** tailors the message to the stakeholder's reality.

**Next Session:** 
*Module 3: Statement of Work (SOW) Analysis & Review.* We will learn how to feed long documents into Copilot to extract hidden risks, ambiguous clauses, and SLA commitments.
