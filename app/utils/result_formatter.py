import pandas as pd

def explain_result(question, result):
    if isinstance(result, pd.Series):
        result = result.to_dict()
    if isinstance(result, pd.DataFrame):
        result = result.to_dict(orient="records") if len(result) <= 50 else f"DataFrame with shape {result.shape}"
    return f"Answer to '{question}': {result}"