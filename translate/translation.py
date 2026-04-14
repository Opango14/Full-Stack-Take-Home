# Eng - Swa
TRANSLATION_DICT = {
    "buy maize": "nunua mahindi",
    "hello": "habari",
    "good morning": "habari za asubuhi",
    "water": "maji",
    "food": "chakula",
    "house": "nyumba",
    "car": "gari",
    "book": "kitabu",
    "school": "shule",
    "teacher": "mwalimu",
}

# Swa - Eng
REVERSE_DICT = {v.lower(): k for k, v in TRANSLATION_DICT.items()}

def translate_text(text: str, target_language: str) -> str:
    if not text:
        return ""

    text_lower = text.strip().lower()
    if target_language == "sw":
        return TRANSLATION_DICT.get(text_lower, text)
    elif target_language == "en":
        return REVERSE_DICT.get(text_lower, text)
    return text