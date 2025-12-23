# PromptCraft AI

## Overview
PromptCraft AI is a local, modular prompt-engineering framework designed to build intent-aware, persona-driven AI systems using local Large Language Models (LLMs) via Ollama.
The project demonstrates how modern AI systems can be architected by separating intent detection, persona control, prompt construction, and model execution into clean, maintainable layers.

This project focuses on prompt orchestration as an engineering discipline, not simple prompt writing.

## Key Objectives
- Design a structured prompt-engineering pipeline
- Enforce strict persona isolation
- Route user queries based on detected intent
- Run entirely on local LLMs (no cloud APIs)
- Provide both CLI and Streamlit UI interfaces
- Maintain extensibility for future personas and models

## System Architecture
PromptCraft AI follows a four-stage pipeline:
1. User Input
2. Intent Classification
3. Persona Selection
4. Final Prompt Construction → LLM Execution

Each stage is implemented as a separate module to ensure clarity, testability, and scalability.

## Supported Intents
- LEARN – Educational explanations and concept breakdowns
- CAREER – Career guidance, skills, and professional advice
- PROMPT – Prompt writing, optimization, and analysis
- TRAVEL – Travel recommendations and destination guidance

Intent detection is performed using a dedicated intent-classifier prompt, not hard-coded rules.

## Persona Isolation
Each intent maps to a strict persona definition stored as a text file.
Personas enforce role boundaries, allowed and disallowed behaviors, and domain-specific tone.

## Project Structure
PromptCraft-AI/
├── app.py
├── main.py
├── intent_router.py
├── persona_selector.py
├── prompt_builder.py
├── chat_memory.json
├── prompts/
│   ├── intent_classifier.txt
│   ├── persona_edumentor.txt
│   ├── persona_careerguide.txt
│   ├── persona_prompt_engineer.txt
│   └── persona_travelguide.txt
├── requirements.txt
└── README.md

## LLM Backend
PromptCraft AI runs entirely on local LLMs using Ollama.
Supported models include llama3, mistral, and phi3.

## Running the Project
pip install -r requirements.txt
ollama serve
python main.py
streamlit run app.py

## License
Educational and portfolio use only.
