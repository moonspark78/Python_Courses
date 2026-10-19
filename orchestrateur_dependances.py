from graphlib import TopologicalSorter, CycleError
from collections import defaultdict

def planifier(taches):
    dependances = {nom: set(p) for nom, p in taches.items()}
    try:
        ordre = tuple(TopologicalSorter(dependances).static_order())
    except CycleError as erreur:
        raise ValueError(f"Cycle détecté : {erreur.args[1]}") from erreur
    niveaux = {}
    for tache in ordre: