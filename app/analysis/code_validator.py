from app.config import FORBIDDEN_NODES, FORBIDDEN_NAMES
import ast

def validate_code_safety(code: str):
    tree = ast.parse(code)
    for node in ast.walk(tree):
        if isinstance(node, FORBIDDEN_NODES):
            raise ValueError(f"Forbidden operation: {type(node).__name__}")
        if isinstance(node, ast.Name) and node.id in FORBIDDEN_NAMES:
            raise ValueError(f"Forbidden name used: {node.id}")