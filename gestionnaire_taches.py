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
        statut = "Terminée" if tache["terminee"] else "En cours"
        print(f"{i}. {tache['nom']} - {statut}")

def ajouter_tache(taches):
    nom = input("Nom de la tâche : ")
    taches.append({"nom": nom, "terminee": False})
    
def terminer_tache(taches):
    afficher_taches(taches)
    numero = int(input("Numéro à terminer : "))
    if 1 <= numero <= len(taches):
        taches[numero - 1]["terminee"] = True

def main():
    taches = charger_taches()
    while True:
        print("\n1. Ajouter  2. Afficher  3. Terminer  4. Quitter")
        choix = input("Votre choix : ")
        if choix == "1": ajouter_tache(taches)
        elif choix == "2": afficher_taches(taches)
        elif choix == "3": terminer_tache(taches)
        elif choix == "4": sauvegarder_taches(taches); break
        sauvegarder_taches(taches)