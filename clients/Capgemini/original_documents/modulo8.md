---
title: "Module 8: Final Integration"
title_slide_scale: 0.8
subtitle: "The EM Crisis Simulation"
author: "Ricardo Reyes-Jimenez"
institute: "Capgemini"
---

## Session Objective

**By the end of this module, the Engagement Manager will be able to:**

1. Integrate all previously learned frameworks (5 Pillars, TAM, CARE, CoT).
2. Execute a multi-step Copilot workflow to resolve a simulated project crisis [@cot2026].
3. Defend Capgemini's commercial interests while maintaining client trust.

---

## 1. The Scenario: The Perfect Storm

**The Context:**
You are managing the "Horizon" project. Yesterday, the client's Project Sponsor sent a furious email:
1. They are withholding the Phase 2 payment, claiming the team missed the *Response Time SLA* during a minor outage.
2. They are demanding a new "Automated Backup Dashboard", claiming it was implicitly included in the original scope.

**Your Goal:** Protect the revenue, reject the scope creep, and de-escalate the anger.

---

## Exercise 1: Step 1 - SLA Defense

**Task:** Analyze the SOW to prove Capgemini is compliant.

* **Provide Copilot with the SOW snippet:** *(Assume the SOW states: "Capgemini will respond to Sev-3 minor outages within 4 business hours.")*
* **Draft Prompt to Try:**
  *"Act as a Contract Analyst. Review this SLA snippet: [Paste Snippet]. The client claims we missed the SLA because we took 3 hours to respond to a minor outage on a Saturday. Based strictly on the text, did Capgemini breach the SLA? Explain why using Chain-of-Thought reasoning."*

---

## Exercise 2: Step 2 - The Change Request

**Task:** Draft the CR for the new dashboard using the CARE framework.

* **Draft Prompt to Try:**
  *"Draft the internal justification for a Change Request using the CARE framework. 
  **Context:** The SOW only covers manual backup scripts. 
  **Action:** Client is demanding an automated visual dashboard. 
  **Result:** It requires 40 hours of effort (\$4,000). 
  **Evaluation:** We can deliver it in Phase 3 if they sign the CR this week."*

---

## Exercise 3: Step 3 - The Diplomatic Email

**Task:** Combine the SLA defense and the CR into one email using the TAM framework.

* **Draft Prompt to Try:**
  *"Now, draft the email to the frustrated Project Sponsor. 
  **Task:** Politely inform them that the SLA was not breached (explain the business hours rule gently) and attach the drafted Change Request for the dashboard they requested. 
  **Audience:** A tense executive who feels ignored. 
  **Method:** Highly empathetic, professional, firm on the commercial boundaries. Use the 5 Pillars of prompting to structure your output."*

---

## Course Conclusion

**Congratulations!** 

You have completed the LegalAI for Engagement Managers course. You are now equipped to:
- Write robust prompts (5 Pillars).
- Structure difficult communications (TAM).
- Audit contracts and negotiate scope (CARE & CoT).
- Manage your team effectively using AI-assisted objectivity.

**Final Reminder:** You are the Human in the Loop. The AI drafts, but *you* deliver the value.
