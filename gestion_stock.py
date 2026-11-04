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
            
    def valeur_totale(self):
        return sum(p.prix * p.quantite for p in self.produits.values())
    
stock = GestionStock()
stock.ajouter(Produit("Clavier", 49.99, 15))
stock.ajouter(Produit("Souris", 24.99, 30))
stock.ajouter(Produit("Écran", 199.99, 8))
stock.rechercher("Clavier").vendre(3)
stock.afficher_stock()