from app.agent.state import AgentState
from app.utils.dataframe_loader import load_dataframe
from app.security.authorization import check_authorization
from app.analysis.prompt_builder import build_code_prompt
from app.llm.llm_client import ask_llm
from app.analysis.code_extractor import extract_code
from app.analysis.code_runner import run_generated_code
from app.utils.result_formatter import explain_result
from app.analysis.code_validator import validate_code_safety
import app.config as config

df = load_dataframe()

# --- Nodes --- #

def get_question_node(state: AgentState) -> AgentState:
    state["request_received"] = True
    return state

def check_authorization_node(state: AgentState) -> AgentState:
    auth, reason = check_authorization(state["question"])
    if auth is None:
        auth = True  # Default update
    state["authorized"] = auth
    state["rejection_reason"] = reason if not auth else None
    state["request_classified"] = True
    return state

def build_prompt_node(state: AgentState) -> AgentState:
    state["prompt"] = build_code_prompt(state["question"], df)
    return state

def ask_llm_node(state: AgentState) -> AgentState:
    state["raw_code"] = ask_llm(state["prompt"], config.MAX_NEW_TOKENS)
    return state

def validate_code_node(state: AgentState) -> AgentState:
    try:
        validate_code_safety(state["raw_code"])
        state["valid_code"] = True
    except ValueError as e:
        state["valid_code"] = False
        state["rejection_reason"] = str(e)
    return state

def extract_code_node(state: AgentState) -> AgentState:
    state["extracted_code"] = extract_code(state["raw_code"])
    return state

def run_code_node(state: AgentState) -> AgentState:
    state["result"] = run_generated_code(state["extracted_code"], df)
    state["analysis_done"] = True
    return state

def explain_result_node(state: AgentState) -> AgentState:
    state["explained_result"] = explain_result(state["question"], state["result"])
    return state

def update_answer_node(state: AgentState) -> AgentState:
    state["result"] = state["explained_result"]
    state["answered"] = True
    return state

def update_reject_node(state: AgentState) -> AgentState:
    state["result"] = f"Request rejected: {state['rejection_reason']}"
    state["answered"] = True
    return state

# --- Routing --- #

def route_after_check(state: AgentState) -> str:
    if state["authorized"] is False:
        return "reject"
    return "build_prompt"

def route_after_run_code(state: AgentState) -> str:
    if state.get("valid_code") is False or state["result"] is None:
        return "reject"
    return "explain"

def route_after_validate(state: AgentState) -> str:
    if state["valid_code"] is True:
        return "extract_code"
    return "reject"