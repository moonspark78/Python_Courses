def calculer_moyenne(notes):
    return sum(notes) / len(notes) if notes else 0

def note_maximale(notes):
    return max(notes) if notes else 0

def note_minimale(notes):
    return min(notes) if notes else 0

def compter_reussites(notes):
    return sum(1 for note in notes if note >= 10)

def analyser_notes(notes):