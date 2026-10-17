import heapq
from pathlib import Path
from collections import Counter

def scan_directory(directory: str) -> list[Path]:
    return [p for p in Path(directory).rglob("*") if p.is_file()]

def analyze_extensions(files: list[Path]) -> Counter:
    return Counter(file.suffix.lower() or "[sans extension]" for file in files)
