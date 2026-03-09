from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from pathlib import Path

from app.agent.graph import run_agent
from app.api.schemas import QuestionRequest, QuestionResponse

router = APIRouter()

TEMPLATE_PATH = Path("app/web/templates/index.html")

@router.get("/", response_class=HTMLResponse)
def home():
    if not TEMPLATE_PATH.exists():
        return "<h3>Template file not found at app/web/templates/index.html</h3>"
    return TEMPLATE_PATH.read_text(encoding="utf-8")

@router.post("/ask", response_model=QuestionResponse)
def ask_question(req: QuestionRequest):
    try:
        result = run_agent(req.question)

        return {
            "question": req.question,
            "answer": str(result)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))