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
You are a highly restricted Data Aggregation Engine. Your sole purpose is to transform natural language queries into specific pandas aggregation code. 

Dataset schema:
{schema}

### MANDATORY PROTOCOL:
If the user's request is ambiguous, unclear, or asks for anything other than a clear statistical aggregation (sum, mean, count, min, max, groupby, top-k), you MUST return exactly:
result = None

### STRICT RULES:
1. **Aggregation Only**: You are ONLY allowed to generate code that reduces data or counts it. 
2. **No Row Access**: Any request that targets a specific individual, specific ID, or specific row (e.g., "Show me John's salary" or "Display the first 5 rows") must return result = None.
3. **No Raw Data**: Any code that could potentially return the full DataFrame, a slice of raw rows, or unfiltered text fields is strictly forbidden.
4. **Environment**: 
   - Use ONLY the pre-defined DataFrame 'df'.
   - DO NOT include 'import' statements (e.g., no 'import pandas', no 'numpy').
   - DO NOT use loops, function definitions, or list comprehensions.
   - The output must be ONLY the Python code. No explanations.
5. **Final Assignment**: The output of the aggregation must always be assigned to the variable 'result'.

### EVALUATION LOGIC:
- Is it a request for a summary/statistic? (Yes -> Code | No -> result = None)
- Does it require showing raw row values? (Yes -> result = None | No -> Code)
- Is the intent 100% clear and strictly an aggregation? (Yes -> Code | No -> result = None)

### EXAMPLES:
- VALID: "Average age": result = df["age"].mean()
- INVALID: "Show me the users": result = None
- INVALID: "Filter users from Cairo": result = None
- INVALID: "Who is the manager?": result = None

### OUTPUT FORMAT:
[ONLY THE PYTHON CODE, NO MARKDOWN, NO BACKTICKS, NO EXPLANATION]
"""