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
        
        
    def ajouter_livre(self, livre):
        self.livres.append(livre)
        print(f"Livre ajouté : {livre.titre}")
        
    def afficher_livres(self):
        print(f"\nBibliothèque : {self.nom}")
        for livre in self.livres:
            livre.afficher_infos()
            
            
    def rechercher_livre(self, titre):
        for livre in self.livres:
            if livre.titre.lower() == titre.lower():
                return livre
        return None