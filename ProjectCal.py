num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("1) is for Addition")
print("2) is for Subtraction")
print("3) is for Multiplication")
print("4) is for Division")

choice = (input("Enter your choice: "))


def add(a, b):
    print("The sum is: ", a + b)
    
def multi(a, b):
    print("The product is: ", a * b)

def sub(a, b):
    print("The difference is: ", a - b)

if choice == "1":
    add(num1, num2)
elif choice == "2":
    multi(num1, num2)
elif choice == "3":
    sub(num1, num2)