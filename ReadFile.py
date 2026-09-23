file=open("demo.txt","r")
print(file)
print(file.read())
file.close()

print("------------------------------------")
print(file.read(9)) # This will raise an error because the file is closed

print("------------------------------------")
print(file.readline()) # This will also raise an error because the file is closed
print(file.readline()) # This will also raise an error because the file is closed
print(file.readline()) # This will also raise an error because the file is closed
print(file.readline()) # This will also raise an error because the file is closed
print(file.readline()) # This will also raise an error because the file is closed


print("------------------------------------")
for i in range(5):
    print(file.readline()) # This will also raise an error because the file is closed
file.close()