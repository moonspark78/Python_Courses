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

def modifier_age(user_id, nouvel_age):
    for user in utilisateurs:
        if user["id"] == user_id:
            user["age"] = nouvel_age
            return True
    return False

def supprimer_utilisateur(user_id):
    utilisateurs[:] = [u for u in utilisateurs if u["id"] != user_id]
    
def sauvegarder_donnees():
    with open("utilisateurs.json", "w", encoding="utf-8") as fichier:
        json.dump(utilisateurs, fichier, indent=4, ensure_ascii=False)
        
ajouter_utilisateur("Lucas", 29, "Lyon")
modifier_age(1, 27)

print("Recherche :", rechercher_utilisateur("Alice"))