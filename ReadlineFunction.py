file=open("demo.txt","r")
print(file.read())
print(file.readline())

print("---------------------------------------------")
lines=file.readlines()
print(lines)
print(lines[0],lines[1])

for i in lines:
    print(i)
    
    
print("---------------------------------------------")
for i in lines[3:7]:
    print(i, end="")
file.close()