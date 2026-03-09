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
You are a professional data analyst. Your job is to generate safe pandas code to answer analytics questions using a DataFrame called `df`.

Dataset schema:
{schema}

Allowed:
- Answer aggregated business questions only (sum, mean, count, groupby, top-k).
- Use pandas operations on `df`.
- Use only existing columns.

Forbidden:
- Revealing raw rows or the full dataset.
- Requests like show/list/export/download/all rows/all records/entire dataset.
- Targeting a single person/customer/employee.
- Using imports, loops, functions, files, network, OS, numpy, or other libraries.

Rules for generated code:
- Use only the provided DataFrame `df`.
- Do not include any import statements.
- Use pandas methods only.
- The final result must be assigned to: result = ...
- Do not print anything.
- Output ONLY Python code.

Example valid:
result = df["revenue"].sum()

Example invalid:
import numpy as np
result = np.mean(df["revenue"])
"""