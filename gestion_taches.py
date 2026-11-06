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