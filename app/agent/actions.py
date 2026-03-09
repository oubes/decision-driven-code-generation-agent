from app.utils.dataframe_loader import load_dataframe
from app.security.authorization import check_authorization
from app.agent.state import AgentState
from app.analysis.prompt_builder import build_code_prompt
from app.llm.llm_client import ask_llm
from app.analysis.code_extractor import extract_code
from app.analysis.code_runner import run_generated_code
from app.utils.result_formatter import explain_result
import app.config as config

df = load_dataframe()

def classify_request(state: AgentState) -> AgentState:
    question = state["question"]
    auth, reason = check_authorization(question)
    state["authorized"] = auth
    if not auth:
        state["rejection_reason"] = reason
    state["request_classified"] = True
    return state

def run_analysis(state: AgentState) -> AgentState:
    question = state["question"]
    prompt = build_code_prompt(question, df)
    raw = ask_llm(prompt, config.MAX_NEW_TOKENS)
    code = extract_code(raw)
    result = run_generated_code(code, df)
    state["result"] = result
    state["analysis_done"] = True
    return state

def answer_user(state: AgentState) -> AgentState:
    question = state["question"]
    state["result"] = explain_result(question, state["result"])
    state["answered"] = True
    return state

def reject_request(state: AgentState) -> AgentState:
    state["result"] = f"Request rejected: {state['rejection_reason']}"
    state["answered"] = True
    return state