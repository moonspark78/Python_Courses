""" 
List is a special data structure in Python that allows you to store multiple items in a single variable.
Lists are ordered, changeable, and allow duplicate values. They are defined by enclosing elements in square brackets [].
"""

a= [1, 2, 3, 4, 5]  # A list of integers
print(a)  # Output: [1, 2, 3, 4, 5]
print(type(a))  # Output: <class 'list'>

print(a[0])  # Output: 1 (Accessing the first element)
a[0] = 10  # Modifying the first element
print(a)  # Output: [10, 2, 3, 4,

""" 
Création & accès : l = [1, 2, 3] — accès par index l[0] (premier) et l[-1] (dernier).
Slicing : l[début:fin:pas] extrait une sous-liste (ex. l[1:3]).
Ajout : l.append(x) (fin), l.insert(i, x) (index i), l.extend(l2) (concaténation).
Suppression : l.pop(i) (par index), l.remove(x) (par valeur), del l[i].
Fonctions clés : len(l) (taille), l.sort() (tri en place), x in l (test de présence).
Compréhension : [x**2 for x in l if x > 0] (création et filtrage concis).
Nature : Structure mutable (modifiable en place), ordonnée et multi-type.
"""