PromptCraft AI
Overview

PromptCraft AI is a local, modular prompt-engineering framework designed to build intent-aware, persona-driven AI systems using local LLMs via Ollama.
It demonstrates how modern AI products separate intent detection, persona control, prompt construction, and model execution into clean, maintainable layers.

The project focuses on prompt orchestration as an engineering discipline, not just prompt writing.

Key Objectives
-Design a structured prompt-engineering pipeline
-Enforce strict persona isolation
-Route user queries based on detected intent
-Run entirely on local LLMs (no cloud APIs)
-Provide both CLI and UI (Streamlit) interfaces
-Maintain extensibility for future personas and models
-Architecture Overview
-The system follows a four-stage pipeline:

User Input
-Intent Classification
-Persona Selection
-Final Prompt Construction → LLM Execution
-Each stage is implemented as a separate module to ensure clarity, testability, and scalability.
-Intent Taxonomy


The system currently supports the following intents:

Intent	Description:
LEARN	Educational explanations and concept breakdowns
CAREER	Career guidance, skills, and professional advice
PROMPT	Prompt writing, optimization, and analysis
TRAVEL	Travel recommendations and destination guidance

Intent detection is performed using a dedicated intent-classifier prompt, not hard-coded rules.

Persona Isolation
-Each intent is mapped to a strict persona definition stored as a text file.

Personas:
persona_edumentor.txt
persona_careerguide.txt
persona_prompt_engineer.txt
persona_travelguide.txt
Each persona enforces:


Role boundaries
-Allowed and disallowed behaviors
-Domain-specific tone and constraints
-The system guarantees that:
-Personas never mix
-The LLM cannot override its assigned role
-Responses remain domain-consistent


Project Structure
PromptCraft-AI/
│
├── app.py                  # Streamlit UI application
├── main.py                 # CLI entry point
├── intent_router.py        # Routes input to intent classifier
├── persona_selector.py     # Maps intent to persona file
├── prompt_builder.py       # Builds final system prompt
├── chat_memory.json        # Optional conversation memory
│
├── prompts/
│   ├── intent_classifier.txt
│   ├── persona_edumentor.txt
│   ├── persona_careerguide.txt
│   ├── persona_prompt_engineer.txt
│   └── persona_travelguide.txt
│
├── requirements.txt
└── README.md

LLM Backend

PromptCraft AI runs entirely on local LLMs using Ollama.

Supported models:

-llama3
-mistral
-phi3

Model switching is supported at runtime via CLI or UI controls.
-No external APIs or internet access are required.
-CLI Usage
-Start the CLI interface:
python main.py


Available commands:

/model show        Show current model
/model llama3     Switch to llama3
/model mistral    Switch to mistral
/model phi3       Switch to phi3
exit              Exit the application


Any other input is treated as a user query and routed through the prompt pipeline.

-Streamlit UI
Run the UI application:
streamlit run app.py


Features:

-Interactive chat interface
-Model selection from sidebar
-Persistent session memory
-Real-time prompt execution
-Prompt Engineering Principles Demonstrated
-This project demonstrates production-level prompt engineering, including:
-Intent-aware prompting
-Persona enforcement through system prompts
-Prompt modularization
-Instruction hierarchy (system > persona > user)
-LLM behavior control without fine-tuning
-Model-agnostic prompt execution
-Why This Project Matters

Most AI demos stop at prompt writing.
PromptCraft AI treats prompting as software architecture, showing how real AI products are built.

This approach mirrors how prompt systems are designed in:

-AI platforms
-Agent frameworks
-LLM orchestration layers
-Enterprise AI tooling

Requirements
-Python 3.10+
-Ollama installed and running
-At least one supported local model pulled
-Install dependencies:

pip install -r requirements.txt

Future Enhancements
-Multi-intent detection
-Memory-aware reasoning
-Agent chaining
-Prompt evaluation metrics
-Tool calling support

Author

Tanay Jalan
Prompt Engineering | AI Systems | LLM Orchestration