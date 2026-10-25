import re
from collections import Counter

def analyser_texte(texte):
    mots = re.findall(r"\b[a-zA-ZÀ-ÿ]+\b", texte.lower())
    frequences = Counter(mots)