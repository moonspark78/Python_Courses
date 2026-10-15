def calculer_moyenne(notes):
    return sum(notes) / len(notes) if notes else 0

def note_maximale(notes):
    return max(notes) if notes else 0

def note_minimale(notes):
    return min(notes) if notes else 0

def compter_reussites(notes):
    return sum(1 for note in notes if note >= 10)

def analyser_notes(notes):
    print("Moyenne :", calculer_moyenne(notes))
    print("Meilleure note :", note_maximale(notes))
    print("Note minimale :", note_minimale(notes))
    print("Nombre de réussites :", compter_reussites(notes))
    
notes = [12, 8, 15, 17, 9, 14]
analyser_notes(notes)


def main():
    saisie = input("Entrez les notes séparées par des espaces : ")
    notes = [float(note) for note in saisie.split()]
    analyser_notes(notes)
    
def test_analyser_notes():
    notes_test = [12, 8, 15, 17, 9, 14]