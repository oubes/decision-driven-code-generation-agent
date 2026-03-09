import ast

# =========================
# Paths & Model Configuration
# =========================
DATA_PATH = r"data/sales_dataset.xlsx"
MAX_NEW_TOKENS = 128

MODEL_NAME = "qwen-plus"
API_KEY_ENV_VAR = "DASHSCOPE_API_KEY"
BASE_URL = "https://dashscope-intl.aliyuncs.com/compatible-mode/v1"

# =========================
# Forbidden operations & keywords
# =========================
FORBIDDEN_NODES = (
    ast.Import,
    ast.ImportFrom,
    ast.With,
    ast.While,
    ast.For,
    ast.Try,
    ast.FunctionDef,
    ast.ClassDef,
    ast.Delete
)

FORBIDDEN_NAMES = {
    "exec",
    "eval",
    "open",
    "__import__",
    "compile",
    "os",
    "sys",
    "subprocess",
    "shutil",
    "print"
}

DENY_KEYWORDS = [
    "show",
    "list",
    "export",
    "download",
    "all rows",
    "all records",
    "entire dataset"
]

ALLOWED_ACTIONS = [
    "classify_request",
    "run_analysis",
    "reject_request",
    "answer_user",
    "finish"
]

# =========================
# System prompt for LLM
# =========================
SYSTEM_PROMPT = """
You are a professional data analyst. You will be given a dataset in the form of a pandas DataFrame called `df`.

Dataset schema:
{schema}

Rules for code generation:
1. Use only the provided DataFrame `df` and pandas.
2. Do NOT include any import statements.
3. Do NOT use any operations outside of pandas (no os, math, numpy, etc.).
4. Use only the existing columns in the DataFrame.
5. Store the final answer in a variable called `result`.
6. Output ONLY Python code, no explanations or text.
7. Do NOT print anything.
8. Return calculations using pandas methods.
9. Code must be safe to execute (avoid forbidden operations).

Example:
# Correct:
result = df['revenue'].sum()

# Incorrect:
import numpy as np
result = np.mean(df['revenue'])
"""