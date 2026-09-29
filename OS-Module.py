import os

print(os.getcwd())
print(os.listdir())
print(os.listdir()[3])


print("-----------------------------")
for i in os.listdir():
    print(i)