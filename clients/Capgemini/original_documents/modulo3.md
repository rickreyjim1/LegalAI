---
title: "Module 3: SOW Analysis & EM PromptLibrary"
subtitle: "Risk Extraction & Scaling Knowledge for EMs"
author: "Ricardo Reyes-Jimenez"
institute: "Capgemini"
---
## Session Objective

**By the end of this module, the Engagement Manager will be able to:**

1. Understand the value of an EM-specific PromptLibrary to scale knowledge.
2. Use MS Copilot to audit lengthy Statements of Work (SOWs) efficiently using reusable "Blueprints".
3. Extract commercial risks, hidden penalties, and ambiguous commitments.
4. Clarify vague Service Level Agreements (SLAs) into measurable  metrics.

---

## 1. The Challenge of SOWs & Manual Review

**SOWs are the baseline of profitability, but they are often dense and ambiguous.**

* **The EM's Reality:** Inheriting an SOW drafted by Sales that contains unrealistic technical promises or hidden liabilities.
* **The Manual Cost:** EMs spend hours reading hundreds of pages of legal and technical jargon just to establish a baseline.
* **The AI Advantage:** Copilot can process dozens of pages in seconds, flagging contradictions between the *Pricing Schedule* and the *Technical Deliverables* [@sowAI2025].

---

## 2. The Solution: An EM PromptLibrary

* **What is it?** A centralized, tested, and categorized repository of AI instructions (prompts) ready to be used by any Engagement Manager.
* **The "Prompt Blindness" Problem:** An EM spends 40 minutes tweaking a prompt until Copilot perfectly extracts SOW risks. When the project starts, that perfect prompt is forgotten.
* **Scaling Efficiency:** If that EM documents their successful prompt in a PromptLibrary, 50 other EMs can use it tomorrow, saving hundreds of hours across the practice.

---

## 3. The "Blueprint" Concept

* A *Blueprint* is a parameterized prompt. It is not a static text, but a formula that allows you to substitute variables for different clients or projects.
* **Static Prompt (Bad):** *"Summarize the Acme Corp SOW and find risks."*
* **Blueprint (Good):** *"Act as a strict Capgemini Delivery Director. Review the attached [DOCUMENT TYPE] for [CLIENT INDUSTRY]. Extract any clause where we assume financial liability for [SPECIFIC RISK]. SOW Text: [TEXT]"*

---

## 4. Anatomy of a Reusable EM Prompt

Every good *Blueprint* in your library should have:

1. **Name & Role:** e.g., *EM Risk Assessor*.
2. **Base Context:** The immutable instruction (tone and format).
3. **Variables (Brackets):** The spaces the user must fill (e.g., `[SOW TEXT]`, `[INDUSTRY]`).
4. **Constraints:** What the AI must *never* do (e.g., *"Do not include general technical risks, focus ONLY on commercial penalties"*).

---

## 5. Security & Confidentiality

* **Crucial Reminder:** When using Blueprints for SOW analysis, ensure you are using your **Capgemini Enterprise Copilot license**.
* Real SOWs contain highly confidential client data, pricing, and strategic information.
* Enterprise licenses ensure your data is not used to train public models.

---

## 6. Risk Extraction Prompting

When uploading a document to Copilot, your instruction must be highly specific about *what* constitutes a risk.

* **Bad Prompt:** "Summarize this SOW and tell me the risks." (Yields generic, unhelpful answers).
* **Good Blueprint:** *"Review the attached SOW. Extract any clause where Capgemini assumes financial liability for third-party software failures. List them in a table with columns: Clause, Page, and Mitigation Strategy."*

---

## Exercise 1: Building your SOW Risk Blueprint

**Context:** You are taking over a new Cloud Migration project. The SOW is 40 pages long.
**Task:** Use Copilot to identify the top commercial risks and save your prompt as a Blueprint.

* **Draft Blueprint to Try:**
  *"Act as a Capgemini Commercial Director. Review the attached SOW text [Paste Extract]. Identify the top 3 commercial risks related to [SPECIFIC CONCERN: e.g., timeline penalties, out-of-scope assumptions]. Present your findings in a markdown table with columns: 'Risk Description', 'SOW Section', and 'Suggested Mitigation'."*

---

## 7. Ambiguity in SLAs

**"The system must be fast and reliable." -> This is an unmanageable SLA.**

* As an EM, you must translate subjective adjectives into objective metrics before project kickoff.
* AI can help identify "weasel words" (e.g., *reasonable, prompt, seamless*) and propose measurable alternatives.
* Adding a "SLA Clarification Blueprint" to your library ensures all EMs standardize their approach to vague requirements.

---

## Exercise 2: SLA Clarification Blueprint

**Context:** The client drafted an SLA clause that states: *"Capgemini will resolve all critical bugs promptly to ensure seamless business continuity."*
**Task:** Use Copilot to rewrite this subjective clause into a measurable metric and save the Blueprint.

* **Draft Blueprint to Try:**
  *"Analyze this SLA clause: '[INSERT SLA CLAUSE]'. Identify the subjective terms that pose an operational risk for delivery. Rewrite the clause using standard ITIL metrics (e.g., Response Time, Resolution Time in hours) so it is objective and measurable for our delivery team."*

---

## 8. Starting your PromptLibrary Today

**You don't need complex software to start.**

* **Phase 1:** Start with a simple shared Excel or Word document in your team's Teams channel.
* **Columns needed:** Prompt Name, Use Case, Blueprint (with brackets), Author, and Effectiveness Rating.
* **The Goal:** Build a habit of documenting successful interactions with Copilot.

---

## Recap & Next Session

**Today we learned:**

- The immense value of creating an EM PromptLibrary to scale knowledge.
- How to structure reusable Blueprints with variables and constraints.
- How to direct Copilot to find specific liabilities in dense contracts.
- Using AI to eliminate "weasel words" and define objective SLAs.

**Next Session:**
*Module 4: Scope Creep & Budget Control.* We will focus on detecting out-of-scope requests and drafting formal Change Requests (CRs) using the CARE framework.
