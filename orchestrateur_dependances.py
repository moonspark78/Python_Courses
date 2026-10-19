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
        niveaux[tache] = 1 + max(
            (niveaux[p] for p in dependances[tache]), default=-1)
    groupes = defaultdict(list)
    for tache, niveau in niveaux.items():
        groupes[niveau].append(tache)
    return ordre, dict(sorted(groupes.items()))

if __name__ == "__main__":
    projet = {
        "maquette": [], "base_de_donnees": [],
    }