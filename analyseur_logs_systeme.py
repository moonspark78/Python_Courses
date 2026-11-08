import os
import re
import json
import datetime

LOG_FILE = "application.log"

def lire_logs(chemin):
    if not os.path.exists(chemin):
        print("Fichier introuvable.")
        return []
    with open(chemin, "r", encoding="utf-8") as fichier:
        return fichier.readlines()
    
def analyser_logs(logs):
    statistiques = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    erreurs = []
    for ligne in logs:
        for niveau in statistiques:
            if niveau in ligne:
                statistiques[niveau] += 1
                if niveau == "ERROR":