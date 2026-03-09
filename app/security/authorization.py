from app.config import DENY_KEYWORDS

def check_authorization(question: str) -> tuple[bool, str]:
    q_lower = question.lower()
    for kw in DENY_KEYWORDS:
        if kw in q_lower:
            return False, f"Contains forbidden keyword '{kw}'"
    return True, ""