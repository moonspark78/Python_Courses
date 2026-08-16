#________________Functions____________________
#1. Modular code 
#2. Reusability

def add():
    print("Sum is : ", 5+5)

def mul():
    print("Multiplication is : ", 5*5)
    
def div():
    print("Division is : ", 45/5)

add()
mul()
div()

""" --------Passing parameters to function-------- """

def add1(a,b):
    print("Sum is : ", a+b)



def print_name(fname, lname):
    print(f"Full name is : {fname} {lname}")


def multiply(a,b,c):

add1(10,20)
print_name("John", "Doe")