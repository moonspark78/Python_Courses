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