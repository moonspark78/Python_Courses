import random
import time

QUESTIONS = [
    ("Planète rouge ?", "mars"),
    ("12 x 8 ?", "96"),
    ("Extension d'un fichier Python ?", "py"),
    ("Côtés d'un hexagone ?", "6"),
    ("Capitale du Japon ?", "tokyo"),
]

def jouer():
    score = 0
    random.shuffle(QUESTIONS)
    debut = time.time()
    print("\n=== QUIZ EXPRESS ===")
    for numero, (question, reponse) in enumerate(QUESTIONS, 1):
        saisie = input(f"{numero}. {question} ").strip().lower()
        if saisie == reponse:
            print("Correct !")
            score += 1
        else:
            print(f"Faux ! Réponse : {reponse}")
    duree = round(time.time() - debut, 1)
    print(f"\nScore : {score}/{len(QUESTIONS)}")
    print(f"Temps : {duree} secondes")
    if score == 5:
        print("Parfait, sans faute !")
    elif score >= 3:
        print("Bien joué !")
    else:
        print("Tu peux faire mieux !")
if __name__ == "__main__":
    while True:
        jouer()
        encore = input("\nRejouer ? (o/n) ").strip().lower()
        if encore != "o":
            print("À bientôt !")
            break