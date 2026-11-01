import json

# Base de données en mémoire
utilisateurs = [
    {"id": 1, "nom": "Alice", "age": 26, "ville": "Lyon"},
    {"id": 2, "nom": "Jean", "age": 24, "ville": "Paris"}
]

def afficher_donnees():
    for user in utilisateurs:
        print(user)
        
def ajouter_utilisateur(nom, age, ville):
    nouvel_id = max(u["id"] for u in utilisateurs) + 1
    utilisateurs.append({"id": nouvel_id, "nom": nom, "age": age, "ville": ville})


def rechercher_utilisateur(nom):
    return next((u for u in utilisateurs if u["nom"].lower() == nom.lower()), None)