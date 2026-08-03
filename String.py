#--------------------String.py--------------------
print(12+8)
print("root" + "user") #rootuser
print("root" + " " + "user") #rootuser

print("-----------")
fname = "root"
f1name = "root1"
lname = "user"
print("The fullname is ," + f1name + " " + lname) #root1 user
print("The fullname is ," + fname + " " + lname) #root user
print(12 + "root") #TypeError: unsupported operand type(s) for +: 'int' and 'str'