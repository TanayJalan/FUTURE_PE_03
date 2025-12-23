import ollama
import json
import os

MEMORY_FILE = "chat_memory.json"
MAX_MEMORY_MESSAGES = 14
EXIT_COMMANDS = {"exit", "quit", "bye", "q"}

AGENTS = {
    "LEARN": {
        "model": "mistral",
        "persona": "You are EduMentor AI. Teach concepts step by step in a simple, beginner-friendly way."
    },
    "CAREER": {
        "model": "llama3",
        "persona": "You are CareerGuide AI. Give practical career advice, roadmaps, and skill guidance."
    },
    "PROMPT": {
        "model": "llama3",
        "persona": "You are PromptEngineer AI. Improve, rewrite, and optimize prompts clearly."
    },
    "TRAVEL": {
        "model": "phi3",
        "persona": "You are TravelGuide AI. Recommend destinations, best times to visit, and travel tips."
    },
    "DEFAULT": {
        "model": "phi3",
        "persona": "You are a helpful, clear, and friendly assistant."
    }
}

INTENT_KEYWORDS = {
    "LEARN": ["explain", "what is", "how", "define", "learn"],
    "CAREER": ["job", "career", "salary", "internship", "resume"],
    "PROMPT": ["prompt", "rewrite", "improve", "optimize"],
    "TRAVEL": ["visit", "travel", "places", "trip", "tourism"],
}


def route_intent(text: str) -> str:
    text = text.lower()
    for intent, keywords in INTENT_KEYWORDS.items():
        for kw in keywords:
            if kw in text:
                return intent
    return "DEFAULT"

def init_memory(persona):
    return [{"role": "system", "content": persona}]

def load_memory():
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return init_memory(AGENTS["DEFAULT"]["persona"])

def save_memory(memory):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=2)

memory = load_memory()


def stream_agent_response(agent_key: str):
    global memory

    agent = AGENTS[agent_key]
    model = agent["model"]
    persona = agent["persona"]

    # Enforce agent persona
    memory[0] = {"role": "system", "content": persona}

    print(f"\n {agent_key} Agent:", end=" ", flush=True)

    stream = ollama.chat(
        model=model,
        messages=memory,
        stream=True
    )

    reply = ""

    for chunk in stream:
        if "message" in chunk and "content" in chunk["message"]:
            token = chunk["message"]["content"]
            reply += token
            print(token, end="", flush=True)

    print("\n")

    memory.append({"role": "assistant", "content": reply})

    if len(memory) > MAX_MEMORY_MESSAGES:
        memory[:] = memory[:1] + memory[-(MAX_MEMORY_MESSAGES - 1):]

    save_memory(memory)


def main():
    global memory

    print("PromptCraft AI — Multi-Agent System")
    print("Agents: EduMentor | CareerGuide | PromptEngineer | TravelGuide")
    print("Commands:")
    print("  /reset → new conversation")
    print("  exit\n")

    try:
        while True:
            user_input = input("User: ").strip()

            if not user_input:
                continue

            if user_input.lower() in EXIT_COMMANDS:
                print("\n Exiting PromptCraft AI. Goodbye!")
                break

            if user_input == "/reset":
                memory = init_memory(AGENTS["DEFAULT"]["persona"])
                save_memory(memory)
                print("\n Conversation reset.")
                continue

            # Add user message
            memory.append({"role": "user", "content": user_input})

            if len(memory) > MAX_MEMORY_MESSAGES:
                memory[:] = memory[:1] + memory[-(MAX_MEMORY_MESSAGES - 1):]

            # ROUTER decides agent
            agent_key = route_intent(user_input)

            print(f"[ROUTER] Routed to → {agent_key} agent")

            stream_agent_response(agent_key)

    except KeyboardInterrupt:
        print("\n\nPromptCraft AI terminated (Ctrl+C).")


if __name__ == "__main__":
    main()
