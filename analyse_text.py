import re

def nettoyer_texte(texte):
    return re.sub(r"[^\w\s]", "", texte.lower())