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
        tasks.append({"title": title, "done": False, "date": datetime.now().strftime("%d/%m/%Y")})
        save_tasks(tasks)
        print("Tâche ajoutée.")
        
def complete_task(tasks):
    show_tasks(tasks)
    try:
        number = int(input("Numéro à terminer : "))
        tasks[number - 1]["done"] = True
        save_tasks(tasks)
        print("Tâche terminée.")
    except (ValueError, IndexError):
        print("Numéro invalide.")
        

def main():
    tasks = load_tasks()
    while True:
        print("\n--- GESTIONNAIRE DE TÂCHES ---")
        print("1. Voir  2. Ajouter  3. Terminer  4. Quitter")
        choice = input("Choix : ")