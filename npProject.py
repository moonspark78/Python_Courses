import numpy as np

products = np.array(["Laptop", "Phone", "Tablet", "Laptop", "Phone"])
prices = np.array([1200, 800, 500, 1500, 900])
quantities = np.array([2, 5, 3, 1, 4])

# Calcul du chiffre d'affaires par produit
revenue = prices * quantities


print("Products:", products)
print("Prices:", prices)
print("Quantities:", quantities)
print("Revenue:", revenue)

# Prix moyen
print("Average price:", prices.mean())

# Quantité totale vendue
print("Total quantity:", quantities.sum())

# Produit avec le plus gros chiffre d'affaires
print("Max revenue:", revenue.max())