from app.utils.graph_utils import save_graph_image
from langgraph.graph import StateGraph, START, END
from app.agent.state import AgentState
from app.agent.nodes import (
    get_question_node,
    check_authorization_node,
    build_prompt_node,
    ask_llm_node,
    validate_code_node,
    extract_code_node,
    run_code_node,
    explain_result_node,
    update_answer_node,
    update_reject_node,
    route_after_check,
    route_after_run_code,
    route_after_validate
)

def build_graph() -> StateGraph:
    workflow = StateGraph(AgentState)

    # --- Nodes --- #
    workflow.add_node("get_question", get_question_node)
    workflow.add_node("check_auth", check_authorization_node)
    workflow.add_node("build_prompt", build_prompt_node)
    workflow.add_node("ask_llm", ask_llm_node)
    workflow.add_node("validate_code", validate_code_node)
    workflow.add_node("extract_code", extract_code_node)
    workflow.add_node("run_code", run_code_node)
    workflow.add_node("explain", explain_result_node)
    workflow.add_node("answer", update_answer_node)
    workflow.add_node("reject", update_reject_node)

    # --- Edges --- #
    workflow.add_edge(START, "get_question")
    workflow.add_edge("get_question", "check_auth")

    workflow.add_conditional_edges(
        "check_auth",
        route_after_check,
        {
            "reject": "reject",
            "build_prompt": "build_prompt"
        }
    )

    workflow.add_edge("build_prompt", "ask_llm")
    workflow.add_edge("ask_llm", "validate_code")

    workflow.add_conditional_edges(
        "validate_code",
        route_after_validate,
        {
            "reject": "reject",
            "extract_code": "extract_code"
        }
    )

    workflow.add_edge("validate_code", "extract_code")
    workflow.add_edge("extract_code", "run_code")

    workflow.add_conditional_edges(
        "run_code",
        route_after_run_code,
        {
            "explain": "explain",
            "reject": "reject"
        }
    )

    workflow.add_edge("explain", "answer")
    workflow.add_edge("answer", END)
    workflow.add_edge("reject", END)

    return workflow.compile()

# --- Runner --- #
def run_agent(question: str):
    graph = build_graph()
    save_graph_image(graph)

    initial_state: AgentState = {
        "question": question,
        "request_received": False,
        "request_classified": False,
        "authorized": None,
        "analysis_done": False,
        "result": None,
        "answered": False,
        "valid_code": None,
        "rejection_reason": None,
        "prompt": None,
        "raw_code": None,
        "explained_result": None,
        "extracted_code": None
    }

    final_state = graph.invoke(initial_state)
    return final_state["result"]