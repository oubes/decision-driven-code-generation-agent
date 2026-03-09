from app.agent.actions import classify_request, run_analysis, answer_user, reject_request
from app.agent.state import AgentState

ALLOWED_ACTIONS = ["classify_request", "run_analysis", "reject_request", "answer_user", "finish"]

def decide_action(state: AgentState) -> str:
    if not state["request_classified"]:
        return "classify_request"
    if state["authorized"] and not state["analysis_done"]:
        return "run_analysis"
    if state["analysis_done"] and not state["answered"]:
        return "answer_user"
    if state["answered"]:
        return "finish"
    return "reject_request"

def run_agent(question: str):
    state: AgentState = {
        "question": question,
        "request_received": True,
        "request_classified": False,
        "authorized": None,
        "analysis_done": False,
        "answered": False,
        "rejection_reason": None,
        "result": None
    }

    for step in range(10):
        action = decide_action(state)
        if state["authorized"] is False and action == "run_analysis":
            action = "reject_request"

        if action == "classify_request":
            state = classify_request(state)
        elif action == "run_analysis":
            state = run_analysis(state)
        elif action == "answer_user":
            state = answer_user(state)
        elif action == "reject_request":
            state = reject_request(state)
        elif action == "finish":
            break

    return state["result"]