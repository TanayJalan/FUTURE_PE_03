# PromptCraft AI

## Overview
PromptCraft AI is a local, modular prompt-engineering framework designed to build intent-aware, persona-driven AI systems using local Large Language Models (LLMs) via Ollama.

The project demonstrates how modern AI systems can be architected by separating intent detection, persona control, prompt construction, and model execution into clean, maintainable layers. It treats prompt engineering as a **system design problem**, not simple prompt writing.

The entire system runs locally with no dependency on cloud APIs.

---

## Key Objectives
- Design a structured prompt-engineering pipeline
- Enforce strict persona isolation and role boundaries
- Route user queries dynamically based on detected intent
- Run entirely on local LLMs (no cloud APIs)
- Provide both CLI and Streamlit UI interfaces
- Maintain extensibility for new personas and domains

---

## Architecture Diagram

```text
ARCHITECTURE DIAGRAM — PROMPTCRAFT AI

+------------------+
|     User Input   |
| (CLI / Streamlit)|
+---------+--------+
          |
          v
+------------------+
| Intent Classifier|
| (Prompt-based)   |
+---------+--------+
          |
          v
+------------------+
| Persona Selector |
| (Strict Mapping) |
+---------+--------+
          |
          v
+---------------------------+
| Prompt Builder            |
| - System Rules            |
| - Persona Constraints     |
| - User Input              |
| - Optional Memory         |
+-------------+-------------+
              |
              v
+---------------------------+
| Local LLM (Ollama)        |
| llama3 / mistral / phi3  |
+-------------+-------------+
              |
              v
+---------------------------+
| Response Output           |
| CLI / Streamlit UI        |
+---------------------------+

DATA FLOW SUMMARY
-----------------
User Input
→ Intent Classification
→ Persona Enforcement
→ Prompt Construction
→ Local LLM Execution
→ Response Returned
```

---

## System Architecture Explanation

1. **User Input**  
   The system accepts user queries through either a command-line interface or a Streamlit-based web UI.

2. **Intent Classification**  
   A dedicated intent-classifier prompt determines the intent of the user query (LEARN, CAREER, PROMPT, TRAVEL).

3. **Persona Selection**  
   Each intent maps to a strictly defined persona that controls tone, scope, and allowed behavior.

4. **Prompt Construction**  
   The final system prompt is assembled using system rules, persona constraints, optional conversation memory, and user input.

5. **LLM Execution**  
   The constructed prompt is executed on a local LLM using Ollama, ensuring full data privacy.

---

## Supported Intents

- **LEARN** – Educational explanations and concept breakdowns  
- **CAREER** – Career guidance, skills, and professional advice  
- **PROMPT** – Prompt writing, optimization, and analysis  
- **TRAVEL** – Travel recommendations and destination guidance  

Intent detection is prompt-driven rather than hard-coded, making the system model-agnostic.

---

## Persona Isolation

Each intent is mapped to a dedicated persona defined in a text file.

Personas enforce:
- Strict role boundaries
- Allowed and disallowed behaviors
- Domain-specific tone and constraints

System guarantees:
- Personas never mix across intents
- The LLM cannot override its assigned role
- Responses remain domain-consistent

---

## Project Structure

```text
PromptCraft-AI/
├── app.py                     # Streamlit UI application
├── main.py                    # CLI entry point
├── intent_router.py           # Routes input to intent classifier
├── persona_selector.py        # Maps intent to persona file
├── prompt_builder.py          # Builds final system prompt
├── chat_memory.json           # Optional conversation memory
├── prompts/
│   ├── intent_classifier.txt
│   ├── persona_edumentor.txt
│   ├── persona_careerguide.txt
│   ├── persona_prompt_engineer.txt
│   └── persona_travelguide.txt
├── requirements.txt
└── README.md
```

---

## LLM Backend

PromptCraft AI runs entirely on local LLMs using Ollama.

Supported models include:
- llama3
- mistral
- phi3

Models can be switched dynamically without changing application logic.

---

## Running the Project

### Prerequisites
- Python 3.10 or higher
- Ollama installed and running

### Install dependencies
```bash
pip install -r requirements.txt
```

### Start Ollama
```bash
ollama serve
```

### Run CLI
```bash
python main.py
```

### Run Streamlit UI
```bash
streamlit run app.py
```

---

## Why This Project Matters

PromptCraft AI demonstrates real-world prompt engineering practices used in production systems:
- Intent-aware routing
- Persona safety enforcement
- Prompt modularization
- Local-first AI deployment

The design is intentionally extensible and mirrors how modern AI products structure LLM interactions.

---

## License

This project is intended for educational and portfolio use.
