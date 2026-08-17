""" 
Variable scope defines where a variable can be acces or modified within a program
"""

a=56
def add():
    print("Inside add function a = ",a)
    
add()
print("Outside if the function a =",a)