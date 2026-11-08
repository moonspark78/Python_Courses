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
                    erreurs.append(ligne.strip())
    return statistiques, erreurs


def generer_rapport(statistiques, erreurs):
    rapport = {
        "date": datetime.datetime.now().isoformat(),
        "statistiques": statistiques,
        "erreurs": erreurs
    }
    with open("rapport.json", "w", encoding="utf-8") as fichier:
        json.dump(rapport, fichier, indent=4)
    return rapport    


def main():
    print("=== ANALYSEUR DE LOGS SYSTEME ===")
    logs = lire_logs(LOG_FILE)