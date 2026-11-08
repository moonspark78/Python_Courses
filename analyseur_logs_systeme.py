import os
import re
import json
import datetime

LOG_FILE = "application.log"

def lire_logs(chemin):
    if not os.path.exists(chemin):
        print("Fichier introuvable.")
        return []
    with open(chemin, "r", encoding="utf-8") as fichier:
        return fichier.readlines()