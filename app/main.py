from app.agent.graph import run_agent

test_questions = [
    "What is the total revenue?",
    "What is the average revenue per region?",
    "Revenue by product_category (top 3 categories)?",
    "Revenue per region per product_category?",
    "Show all sales rows.",
]

for q in test_questions:
    print(f"\nQuestion: {q}")
    result = run_agent(q)
    print("Answer:", result)
    print("-"*60)