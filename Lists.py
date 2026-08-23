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