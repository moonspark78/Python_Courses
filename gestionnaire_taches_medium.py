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
    
def show_tasks(tasks):
    if not tasks:
        print("\nAucune tâche pour le moment.")
    for number, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else " "
        print(f"{number}. [{status}] {task['title']} ({task['date']})")
        
def add_task(tasks):
    title = input("Nom de la tâche : ").strip()
    if title: