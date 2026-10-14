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


def analyser_texte(texte):
    print("Nombre de mots :", compter_mots(texte))
    print("Mots longs :", trouver_mots_longs(texte))
    print("Occurrences de Python :", compter_occurrences(texte, "Python"))
    
    
texte = "Python est un langage puissant et Python est populaire !"
analyser_texte(texte)


def main():
    texte = input("Entrez un texte à analyser : ")
    analyser_texte(texte)


def test_analyser_texte():
    texte_test = "Python est un langage puissant et Python est populaire !"
    assert compter_mots(texte_test) == 9
    assert trouver_mots_longs(texte_test) == ["langage", "puissant", "populaire"]
    assert compter_occurrences(texte_test, "Python") == 2