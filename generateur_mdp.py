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
    parser.add_argument("-n", "--nombre", type=int, default=1)
    parser.add_argument("--sans-symboles", action="store_true")
    args = parser.parse_args()
    if args.nombre < 1:
        parser.error("Le nombre doit etre positif.")
    try:
        for i in range(args.nombre):
            print(f"{i + 1}: {generer(args.longueur, not args.sans_symboles)}")
    except ValueError as erreur:
        parser.error(str(erreur))
        
        
if __name__ == "__main__":