import ast
from collections import Counter

def analyze_code(source):
    tree = ast.parse(source)
    stats = Counter()
    functions = []