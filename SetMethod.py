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

b.remove(15)  # Attempting to remove an element that does not exist in the set
print(b)  # Output: {11, 3, 7, 9}, the set remains unchanged

# discard() method can be used to remove an element from the set without raising an error if the element does not exist. For example:
b.discard(7)  # Removing an element from the set
print(b)  # Output: {11, 3, 9}, the element

b.discard(20)  # Attempting to discard an element that does not exist in the set

print("-------------------------------------------")
print("-------------------------------------------")

s = {12, 4,56,120}
t = {12, 4,6,100}
c = s.intersection(t)  # Finding the intersection of two sets
print(c)  # Output: {12, 4}, the common elements in both sets

