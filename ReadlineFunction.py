file=open("demo.txt","r")
print(file.read())
print(file.readline())

print("---------------------------------------------")
lines=file.readlines()
print(lines)
print(lines[0],lines[1])