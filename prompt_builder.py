def load_prompt(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read().strip()


def build_final_prompt(system_prompt: str, persona_prompt: str, memory: list, user_input: str) -> str:
    memory_block = ""
    if memory:
        memory_block = "\n".join(
            [f"{m['role'].upper()}: {m['content']}" for m in memory]
        )

    return f"""
SYSTEM:
{system_prompt}

PERSONA:
{persona_prompt}

MEMORY:
{memory_block}

USER:
{user_input}

ASSISTANT:
"""
