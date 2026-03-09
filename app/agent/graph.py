import os
from langgraph.graph import StateGraph, END, START
from app.agent.state import AgentState
from app.agent.actions import classify_request, run_analysis, answer_user, reject_request

def decide_next_node(state: AgentState) -> str:
    if not state["request_classified"]:
        return "classify"
    if state["authorized"] is False:
        return "reject"
    if not state["analysis_done"]:
        return "analyze"
    if not state["answered"]:
        return "answer"
    return END

def build_graph():
    workflow = StateGraph(AgentState)

    workflow.add_node("classify", classify_request)
    workflow.add_node("analyze", run_analysis)
    workflow.add_node("answer", answer_user)
    workflow.add_node("reject", reject_request)

    workflow.add_edge(START, "classify")

    workflow.add_conditional_edges(
        "classify",
        decide_next_node,
        {
            "analyze": "analyze",
            "reject": "reject"
        }
    )

    workflow.add_edge("analyze", "answer")
    workflow.add_edge("answer", END)
    workflow.add_edge("reject", END)

    return workflow.compile()

def save_graph_image(app, filename="graph_flow.png"):
    try:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        full_path = os.path.join(current_dir, filename)
        
        img_data = app.get_graph().draw_mermaid_png()
        with open(full_path, "wb") as f:
            f.write(img_data)
    except Exception:
        pass

def run_agent(question: str):
    app = build_graph()
    save_graph_image(app)
    
    initial_state: AgentState = {
        "question": question,
        "request_received": True,
        "request_classified": False,
        "authorized": None,
        "analysis_done": False,
        "answered": False,
        "rejection_reason": None,
        "result": None
    }
    
    final_state = app.invoke(initial_state)
    return final_state["result"]