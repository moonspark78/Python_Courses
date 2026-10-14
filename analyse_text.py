import re

def nettoyer_texte(texte):
    return re.sub(r"[^\w\s]", "", texte.lower())

def compter_mots(texte):
    return len(texte.split())


def compter_occurrences(texte, mot):
    mots = nettoyer_texte(texte).split()
    return mots.count(mot.lower())


def trouver_mots_longs(texte):
    return [mot for mot in texte.split() if len(mot) > 5]