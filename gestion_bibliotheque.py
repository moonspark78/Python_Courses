class Livre:
    def __init__(self, titre, auteur, disponible=True):
        self.titre = titre
        self.auteur = auteur
        self.disponible = disponible

    def afficher_infos(self):
        statut = "Disponible" if self.disponible else "Emprunté"
        print(f"{self.titre} - {self.auteur} ({statut})")
        
    def emprunter(self):
        if self.disponible:
            self.disponible = False