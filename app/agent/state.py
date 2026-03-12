from typing import TypedDict, Any

class AgentState(TypedDict):
    request_received: bool
    request_classified: bool
    authorized: bool | None
    analysis_done: bool
    result: Any | None
    answered: bool
    valid_code: bool | None
    rejection_reason: str | None
    question: str
    prompt: str | None
    raw_code: str | None
    explained_result: Any | None
    extracted_code: str | None