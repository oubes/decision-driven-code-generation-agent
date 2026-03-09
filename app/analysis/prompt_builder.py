from app.config import SYSTEM_PROMPT

def build_code_prompt(question, df):
    schema = {
        "columns": list(df.columns),
        "dtypes": {col: str(df[col].dtype) for col in df.columns}
    }

    system_content = SYSTEM_PROMPT.format(schema=schema)

    return [
        {"role": "system", "content": system_content},
        {"role": "user", "content": question}
    ]