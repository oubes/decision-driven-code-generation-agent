from app.analysis.code_validator import validate_code_safety

def run_generated_code(code, df):
    validate_code_safety(code)
    safe_globals = {"__builtins__": {}, "df": df}
    safe_locals = {}
    exec(code, safe_globals, safe_locals)
    if "result" not in safe_locals:
        raise ValueError("Code must assign 'result' variable")
    return safe_locals["result"]