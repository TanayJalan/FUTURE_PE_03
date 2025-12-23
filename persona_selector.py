def select_persona(intent: str) -> str:
    mapping = {
        "LEARN": "persona_edumentor.txt",
        "CAREER": "persona_careerguide.txt",
        "PROMPT": "persona_prompt_engineer.txt",
        "TRAVEL": "persona_travelguide.txt",
    }

    return mapping.get(intent, "persona_edumentor.txt")
