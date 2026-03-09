def extract_code(text):
    text = text.replace("```python","").replace("```","")
    lines = []
    for line in text.splitlines():
        line = line.strip()
        if line and not line.startswith("#") and not line.startswith("print"):
            lines.append(line)
    return "\n".join(lines)