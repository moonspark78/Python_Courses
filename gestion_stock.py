class Produit:
    def __init__(self, nom, prix, quantite):
        self.nom = nom
        self.prix = prix
        self.quantite = quantite
        
    def afficher(self):
        print(f"{self.nom} | {self.prix}€ | Stock : {self.quantite}")
        
    def vendre(self, quantite):
        if quantite <= 0:
            raise ValueError("Quantité invalide")
        if quantite > self.quantite:
            print(f"Stock insuffisant pour {self.nom}")
            return False
        self.quantite -= quantite
        print(f"{quantite} unités vendues")
        return True
    
class GestionStock:
    def __init__(self):
        self.produits = {}
        
    def ajouter(self, produit):
        self.produits[produit.nom] = produit
        
    def afficher_stock(self):
        for produit in self.produits.values():
            produit.afficher()