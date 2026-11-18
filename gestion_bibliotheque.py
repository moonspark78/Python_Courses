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
            print(f"Vous avez emprunté : {self.titre}")
        else:
            print("Ce livre est déjà emprunté.")
            
    def retourner(self):
        self.disponible = True
        print(f"Livre retourné : {self.titre}")


class Bibliotheque:
    def __init__(self, nom):
        self.nom = nom
        self.livres = []