import heapq
from pathlib import Path
from collections import Counter

def scan_directory(directory: str) -> list[Path]:
    return [p for p in Path(directory).rglob("*") if p.is_file()]

def analyze_extensions(files: list[Path]) -> Counter:
    return Counter(file.suffix.lower() or "[sans extension]" for file in files)


def largest_files(files: list[Path], limit: int = 5) -> list[tuple[int, Path]]:
    return heapq.nlargest(limit, ((f.stat().st_size, f) for f in files))

def generate_report(directory: str) -> dict:
    files = scan_directory(directory)
    return {
        
    }