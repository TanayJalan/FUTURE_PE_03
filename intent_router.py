def route_intent(llm, user_input: str, intent_prompt: str) -> str:
    """
    Returns ONE intent word only:
    LEARN | CAREER | PROMPT | TRAVEL
    """

    final_prompt = f"""
{intent_prompt}

User Input:
{user_input}

Output:
"""

    raw_output = llm(final_prompt).strip().upper()

    # Safety cleanup (VERY IMPORTANT)
    valid_intents = {"LEARN", "CAREER", "PROMPT", "TRAVEL"}

    for intent in valid_intents:
        if intent in raw_output:
            print(f"[DEBUG] Intent detected: {intent}")
            return intent

    print("[DEBUG] Intent fallback → LEARN")
    return "LEARN"
