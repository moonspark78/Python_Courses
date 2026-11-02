import json
import os

FICHIER = "taches.json"

def charger_taches():
    if os.path.exists(FICHIER):
        with open(FICHIER, "r", encoding="utf-8") as f:
            return json.load(f)