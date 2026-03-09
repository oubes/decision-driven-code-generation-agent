from app.agent.graph import run_agent
from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Decision Driven Analytics Agent",
    version="1.0.0"
)

app.include_router(router)


# test_questions = [
#     "What is the total revenue?",
#     "What is the average revenue per region?",
#     "Revenue by product_category (top 3 categories)?",
#     "Revenue per region per product_category?",
#     "Show all sales rows.",
# ]

# for q in test_questions:
#     print(f"\nQuestion: {q}")
#     result = run_agent(q)
#     print("Answer:", result)
#     print("-"*60)