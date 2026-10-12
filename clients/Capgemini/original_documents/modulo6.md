---
title: "Module 6: Advanced Prompting"
subtitle: "Few-Shot and Chain-of-Thought"
author: "Ricardo Reyes-Jimenez"
institute: "Capgemini"
---

## Session Objective

**By the end of this module, the Engagement Manager will be able to:**

1. Clone their personal or corporate writing style using **Few-Shot Prompting**.
2. Force the AI to reason sequentially using **Chain-of-Thought (CoT)**.
3. Apply these advanced techniques to generate complex SteerCo (Steering Committee) reports.

---

## 1. Cloning Your Style (Few-Shot Prompting)

**The AI should write like you, not like a generic robot.**

* **Zero-Shot:** No examples provided. Good for simple tasks (e.g., summarizing).
* **One-Shot:** Providing one example to define the format.
* **Few-Shot:** Providing 2 to 3 examples of input/output to teach the AI your tone, vocabulary, and preferred corporate phrasing.

> **Why it matters:** EMs spend hours editing AI drafts because they sound "too enthusiastic" or "robotic". Few-Shot eliminates this editing time [@fewshot2025].

---

## Exercise 1: Few-Shot Style Cloning

**Context:** You need to announce a new Lead Architect joining the project. You want the email to sound exactly like your previous announcements.
**Task:** Use Copilot to write the email based on your past examples.

* **Draft Prompt to Try:**
  *"I need to announce that Sarah Connor is joining as our new Lead Architect on Monday. Write the email using the exact same tone and structure as these two previous examples I wrote:
  [Example 1: 'Team, please welcome John...']
  [Example 2: 'Hi everyone, starting tomorrow, David will be...']"*

---

## 2. Chain-of-Thought (CoT)

**Do not ask for the conclusion in Step 1.**

* **The Concept:** Forcing the AI to "think step-by-step" before giving the final answer.
* **The Benefit:** It drastically reduces hallucinations and logical errors in complex analytical tasks [@cot2026].
* **The Method:** Divide the prompt into sequential instructions: *Extract -> Analyze -> Format*.

---

## Exercise 2: CoT for SteerCo Reports

**Context:** You have 3 pages of messy, bulleted meeting notes from a chaotic weekly sync. You need a clean, 1-page executive summary for the SteerCo.
**Task:** Use CoT to force the AI to categorize the notes before summarizing them.

* **Draft Prompt to Try:**
  *"Process the following raw meeting notes [Paste Notes]. Do not give me the final summary immediately. Follow these steps sequentially:
  **Step 1:** Extract all mentions of budget issues.
  **Step 2:** Extract all mentions of timeline delays.
  **Step 3:** Based ONLY on the findings in Step 1 and 2, generate a 3-bullet executive summary suitable for a C-level Steering Committee."*

---

## Recap & Next Session

**Today we learned:**
- How to use **Few-Shot** prompting to eliminate "AI-sounding" text and save editing time.
- How **Chain-of-Thought (CoT)** forces the AI to reason sequentially, yielding highly accurate executive summaries from messy data.

**Next Session:** 
*Module 7: MS Learn & Information Retrieval.* We will explore how to use Copilot to query official Microsoft documentation and governance policies securely.
