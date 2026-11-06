import os
import json
import datetime
import random

tasks = []

def add_task():
    task = input("Nouvelle tâche : ")
    tasks.append(task)
    print("Tâche ajoutée !")
    
def show_tasks():
    if not tasks:
        print("Aucune tâche pour le moment.")
    else:
        for index, task in enumerate(tasks, 1):
            print(f"{index}. {task}")
            
def delete_task():
    show_tasks()
    try:
        number = int(input("Numéro à supprimer : "))
        tasks.pop(number - 1)
        print("Tâche supprimée !")
    except (ValueError, IndexError):
        print("Numéro invalide.")
        
def random_task():
    if tasks:
        print("Tâche suggérée :", random.choice(tasks))
    else:
        print("Aucune tâche disponible.")

def main():
    while True:
        print("\n--- GESTIONNAIRE DE TÂCHES ---")
        print("1. Ajouter une tâche")
        print("2. Voir les tâches")
        print("3. Supprimer une tâche")
        print("4. Suggestion aléatoire")
        print("5. Quitter")
        choice = input("Votre choix : ")