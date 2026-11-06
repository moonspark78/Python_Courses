import os
import json
import datetime
import random

tasks = []

def add_task():
    task = input("Nouvelle tâche : ")
    tasks.append(task)
    print("Tâche ajoutée !")