import csv
from pathlib import Path
from statistics import mean
from collections import Counter

depenses = [
    {"categorie": "Alimentation", "montant": 45.50},
    {"categorie": "Transport", "montant": 25.00},
    {"categorie": "Logement", "montant": 650.00},
    {"categorie": "Alimentation", "montant": 32.90},
    {"categorie": "Loisirs", "montant": 60.00},
    {"categorie": "Transport", "montant": 18.50},
    {"categorie": "Restaurants", "montant": 35.00},
    {"categorie": "Alimentation", "montant": 72.00},
    {"categorie": "Loisirs", "montant": 25.00},
]

def calculer_total(data):
    return sum(item["montant"] for item in data)

def calculer_moyenne(data):
    return mean(item["montant"] for item in data)