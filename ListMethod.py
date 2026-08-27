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