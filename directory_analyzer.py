import heapq
from pathlib import Path
from collections import Counter

def scan_directory(directory: str) -> list[Path]:
    return [p for p in Path(directory).rglob("*") if p.is_file()]
