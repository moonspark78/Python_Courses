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

def ma_fonction():
    return "résultat"

# Liste regroupant la majorité des types courants
elements = [
    42,                      # int
    3.14,                    # float
    "chaine",                # str
    True,                    # bool
    None,                    # NoneType
    [1, 2],                  # list (imbriquée)
    (3, 4),                  # tuple
    {"nom": "Alice"},        # dict
    {5, 6},                  # set
    ma_fonction              # function
]

# Accès et exécution selon le type :
print(elements[2].upper())   # -> "CHAINE" (méthode str)
print(elements[5][0])        # -> 1 (élément de la sous-liste)
print(elements[7]["nom"])    # -> "Alice" (valeur du dict)
print(elements[9]())         # -> "résultat" (appel de la fonction)


#     0   1   2   3     4
a1 = [12, 56, 88, 6756, 710]
print(a1[0], a1[4]) 

fruits = ["pomme", "banane", "cerise"]
# Accès aux éléments de la liste