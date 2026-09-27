try:
    print(12/2)
except:
    print("cannot divide by zero")
finally:
    print("Code continues ....")
    
    
print("----------------------------------------------------------   ")
print("----------------------------------------------------------   ")

""" 
Real world exceptions can be handled using the try-except-finally block.
The finally block is always executed, regardless of whether an exception occurred or not.
It is typically used for cleanup actions that must be executed under all circumstances, such as closing a file or releasing resources.
"""

a= int(input("Enter the first number: "))
b= int(input("Enter the second number: "))