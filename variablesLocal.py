""" 
Variable scope defines where a variable can be acces or modified within a program
"""

#Global Varible

a=56
def add():
    print("Inside add function a = ",a)
    
add()
print("Outside if the function a =",a)

#--------------------------------------

#-------Global Varible vs Local Variable
b = 10
def add1():
    x=89
    print("x = ",x)
    
add1() # x = 89
print("Outside if the fuction b =",b)
print("x = ",x)