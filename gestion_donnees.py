import json

# Base de données en mémoire
utilisateurs = [
    {"id": 1, "nom": "Alice", "age": 26, "ville": "Lyon"},
    {"id": 2, "nom": "Jean", "age": 24, "ville": "Paris"}
]

def afficher_donnees():
    for user in utilisateurs:
        print(user)