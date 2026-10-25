import re
from collections import Counter

def analyser_texte(texte):
    mots = re.findall(r"\b[a-zA-ZÀ-ÿ]+\b", texte.lower())
    frequences = Counter(mots)
    return frequences

def afficher_resultats(frequences):
    if not frequences:
        print("Aucun mot trouvé.")
        return
    print("Nombre total de mots :", sum(frequences.values()))
    print("Nombre de mots uniques :", len(frequences))