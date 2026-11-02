import json
import os

FICHIER = "taches.json"

def charger_taches():
    if os.path.exists(FICHIER):
        with open(FICHIER, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def sauvegarder_taches(taches):
    with open(FICHIER, "w", encoding="utf-8") as f:
        json.dump(taches, f, indent=4, ensure_ascii=False)
        
def afficher_taches(taches):
    for i, tache in enumerate(taches, 1):