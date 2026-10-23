import argparse
import secrets
import string

def generer(longueur, symboles=True):
    groupes = [string.ascii_lowercase, string.ascii_uppercase, string.digits]
    if symboles:
        groupes.append("!@#$%&*+-_=?")
    if longueur < len(groupes):
        raise ValueError("Longueur trop courte.")
    alphabet = "".join(groupes)
    resultat = [secrets.choice(g) for g in groupes]
    resultat += [secrets.choice(alphabet) for _ in range(longueur - len(resultat))]
    secrets.SystemRandom().shuffle(resultat)
    return "".join(resultat)


def main():
    parser = argparse.ArgumentParser(description="Generateur securise")
    parser.add_argument("-l", "--longueur", type=int, default=20)