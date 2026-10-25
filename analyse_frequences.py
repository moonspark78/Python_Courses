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
    print("\nLes 5 mots les plus fréquents :")
    for mot, nombre in frequences.most_common(5):
        print(f"{mot} : {nombre} fois")
        
def rechercher_mot(frequences, mot):
    mot = mot.lower()
    nombre = frequences.get(mot, 0)
    print(f"Le mot '{mot}' apparaît {nombre} fois.")