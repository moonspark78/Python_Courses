num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("1) is for Addition")
print("2) is for Subtraction")
print("3) is for Multiplication")
print("4) is for Division")

choice = (input("Enter your choice: "))


def add(a, b):
    print("The sum is: ", a + b)


if choice == "1":
    add(num1, num2)