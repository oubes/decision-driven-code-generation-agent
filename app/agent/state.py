from typing import TypedDict, Any

class AgentState(TypedDict):
    request_received: bool
    request_classified: bool
    authorized: bool | None
    analysis_done: bool
    result: Any | None
    answered: bool
    rejection_reason: str | None
    question: str

state_template: AgentState = {
    "request_received": False,
    "request_classified": False,
    "authorized": None,
    "analysis_done": False,
    "result": None,
    "answered": False,
    "rejection_reason": None,
    "question": ""
}