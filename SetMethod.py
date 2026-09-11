a = {12,4,56,232,8,777,1}
a.add(99)  # Adding an element to the set
print(a) 
""" il ajoute l'élément 99 à l'ensemble a.
L'ordre des éléments dans l'ensemble peut varier car les ensembles sont non ordonnés. """

#pour ajouter plusieurs éléments à la fois, vous pouvez utiliser la méthode update()
# 
# avec un autre ensemble ou un itérable (comme une liste ou un tuple) comme argument. Par exemple :

a.update({100, 200, 300})  # Adding multiple elements to the set
print(a)


print("-------------------------------------------")
print("-------------------------------------------")

a.clear()  # Removing all elements from the set
print(a)  # Output: set(), the set is now empty

b = {11, 3, 5, 7, 9}
b.remove(5)  # Removing an element from the set
print(b)  # Output: {11, 3, 7, 9},