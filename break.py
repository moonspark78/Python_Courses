#Break statement is used to exit a loop when a certain condition is met. It can be used in both for and while loops.
for i in range(1, 10+1):
    print(i)
    if i == 5:
        break
print("Loop exited at i =", i)

print("\n")
print("-------------------")

while True:
    print("bonjour")

    if True:
        print("dans le if")
        break