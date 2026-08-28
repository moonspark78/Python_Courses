fruits=["apple", "banana", "cherry", "kiwi"]
fruits.append("orange")
print(fruits)
print("---------")
print("---------")
print("---------")
fruits.insert(1, "grape")
print(fruits)
print("---------")
fruits.remove("kiwi")
print(fruits)
print("---------")
print("---------")
fruits.pop()
print(fruits)
# Si maintenant on veux supprimer ave cun index,

prenoms=["John", "Jane", "Jim", "Jill"]
#Si je veux supprimer le prénom "Jim" qui est à l'index 2, je peux utiliser la méthode pop() avec l'index correspondant.
prenoms.pop(2)
print(prenoms)

#Pour vider la liste, on peut utiliser la méthode clear().
fruits.clear()
print(fruits)

prenoms.index("Jane")  # Renvoie l'index de "Jane" dans la liste prenoms
print(prenoms.index("Jane"))  # Affiche l'index de "Jane"

prenoms.count("John")  # Compte combien de fois "John" apparaît dans la liste prenoms
print(prenoms.count("John"))  # Affiche le nombre d'occurrences de "

#-------------------------------------------------------
legumes=["carotte", "brocoli", "épinard", "poivron"]
legumesCopy=legumes.copy()  # Crée une copie de la liste legumes
print(legumesCopy)  # Affiche la copie de la liste legumes

#-------------------------------------------------------
legumes.sort()  # Trie la liste legumes par ordre alphabétique
print(legumes)  # Affiche la liste legumes triée
#-------------------------------------------------------
number=[12,4,8,8,75,9,82,4,73,89]
number.sort()  # Trie la liste number par ordre croissant
print(number)  # Affiche la liste number triée