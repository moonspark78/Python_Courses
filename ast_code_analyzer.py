import ast
from collections import Counter

def analyze_code(source):
    tree = ast.parse(source)
    stats = Counter()
    functions = []
    for node in ast.walk(tree):
        stats[type(node).__name__] += 1
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            functions.append({
                "name": node.name,
                "args": len(node.args.args),
                "async": isinstance(node, ast.AsyncFunctionDef)
            })
    return {
        "lines": len(source.splitlines()),
        "functions": functions,
        "complexity": stats["If"] + stats["For"]
        + stats["While"] + stats["Try"],
        "node_types": stats.most_common(5)
    }