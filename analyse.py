from rich.console import Console
from rich.table import Table


console = Console()

def calculer_moyenne(notes):
    return sum(notes) / len(notes) if notes else 0


def trouver_meilleure_note(notes):
    return max(notes) if notes else 0


def afficher_resultats(nom, notes):
    table = Table(title=f"Résultats de {nom}")
    table.add_column("Indicateur")
    table.add_column("Valeur")
    table.add_row("Notes", str(notes))
    table.add_row("Moyenne", f"{calculer_moyenne(notes):.2f}")
    table.add_row("Meilleure note", str(trouver_meilleure_note(notes)))
    console.print(table)
    
def main():