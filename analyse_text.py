import re

def nettoyer_texte(texte):
    return re.sub(r"[^\w\s]", "", texte.lower())

def compter_mots(texte):
    return len(texte.split())


def compter_occurrences(texte, mot):