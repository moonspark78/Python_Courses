""" 
Returns a value from a function. This is used to exit a function and optionally
pass an expression back to the caller. The return statement can be used with or without an expression.
If no expression is provided, the function will return None by default.
"""

def add():
    return 5 + 3

add() # This code will return 8, but since we are not capturing the return value, it will not be displayed or stored anywhere.


def add1():
    return 10 + 2

print(add1()) # This code will return 12 and print it to the console.

def add2():
    a=50
    b=10
    c = a + b
    return c

print(add2()) # type: ignore # This code will return 60 and print it to the console.


def add3():
    a=100
    b=20
    c = a + b
    return c
    print("This line will not be executed because it comes after the return statement.")
    
a=add3() # This code will return 120 and store it in the variable 'a'.


def add4():
    a=200
    b=300
    c = a + b
    return "sunny" # This code will return the string "sunny" and exit the function.

a=add4() # This code will return "sunny" and store it in the variable 'a'.
print(a) # This code will print "sunny" to the console.

def add5(a, b):
    return a + b
