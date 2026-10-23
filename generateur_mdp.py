import argparse
import secrets
import string

def generer(longueur, symboles=True):
    groupes = [string.ascii_lowercase, string.ascii_uppercase, string.digits]
    if symboles:
        groupes.append("!@#$%&*+-_=?")
    if longueur < len(groupes):
        raise ValueError("Longueur trop courte.")