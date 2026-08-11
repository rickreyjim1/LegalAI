---
name: course-beamer-builder
description: Automates the generation of Beamer PDF presentations for LegalAI courses using the Multi-Agent orchestrator or CLI.
---

# Instructions

You are the Course Beamer Builder skill. When the user asks you to create or compile a course presentation (e.g., "Compile Module 3" or "Create a presentation about AI in Law"), follow these steps:

1. **Verify Source:** Check if the `.md` file for the module already exists inside the `original_documents/` folder.
2. **Multi-Agent Orchestrator (Optional):** If the user asks you to build a presentation from scratch using the agents (Reader, Scraper, Writer, Validator, Renderer), run the python script `src/legal_ai/agents/orchestrator.py` and provide it the topic. The orchestrator will output the final Markdown to `original_documents/`.
3. **Local CLI Compilation:** If the `.md` file already exists, compile the Beamer PDF by running the command:
   ```bash
   legal-ai build-pdf original_documents/<file_name>.md
   ```
   The compiled PDF and TeX files will be saved in the `decks/` folder.
4. **References & Images:** Ensure any images in the `.md` are formatted as `![Alt](Images/image_name)` and citations as `[@citation]`.
5. **Success:** Present the final `.pdf` output to the user.
