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
        "total_files": len(files),
        "extensions": analyze_extensions(files),
        "largest_files": largest_files(files),
        "total_size_mb": round(sum(f.stat().st_size for f in files) / 1_048_576, 2),        
    }
    
if __name__ == "__main__":
    report = generate_report("./")