import ast
from collections import Counter

def analyze_code(source):
    tree = ast.parse(source)
    stats = Counter()
    functions = []
    for node in ast.walk(tree):
        stats[type(node).__name__] += 1