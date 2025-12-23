# PromptCraft AI

PromptCraft AI is a **local LLM-powered prompt engineering playground** built using **Streamlit** and **Ollama**.

It allows users to:
- Chat with local LLMs (LLaMA 3, Mistral, Phi-3)
- Switch models dynamically
- Maintain conversation memory
- Build and test prompt workflows

---

## Why PromptCraft AI?

Unlike basic chat apps, PromptCraft AI focuses on:
- Prompt structure
- Context handling
- Model behavior comparison
- Real-world LLM system design

This makes it ideal for:
- Prompt Engineers
- AI Engineers
- Students exploring LLM systems

---

## Tech Stack

- Python
- Streamlit
- Ollama (Local LLM runtime)
- LLaMA 3 / Mistral / Phi-3

---

## How to Run

### 1- Install dependencies
```bash
pip install -r requirements.txt

2- Start Ollama
ollama serve

3- Run the app
streamlit run app.py

Supported Models

llama3
mistral
phi3

(Download via ollama pull model_name)

Future Improvements
-Persona-based routing
-Prompt templates
-Memory optimization
-Token control

Author

Tanay Jalan
AI Engineer aspirant |Gen AI Learner | Prompt Engineering Enthusiast