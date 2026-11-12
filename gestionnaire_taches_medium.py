import json
from pathlib import Path
from datetime import datetime

FILE = Path("tasks.json")

def load_tasks():
    if FILE.exists():
        return json.loads(FILE.read_text(encoding="utf-8"))
    return []

def save_tasks(tasks):
    FILE.write_text(json.dumps(tasks, indent=2, ensure_ascii=False), encoding="utf-8")