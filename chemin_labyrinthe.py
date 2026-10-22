import random

def generer_grille(n, obstacles):
    grille = [[0] * n for _ in range(n)]
    for _ in range(obstacles):
        x, y = random.randrange(n), random.randrange(n)
        grille[x][y] = 1
    return grille

def afficher(grille):
    for ligne in grille: