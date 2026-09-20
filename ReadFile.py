file=open("demo.txt","r")
print(file)
print(file.read())
file.close()

print("------------------------------------")
print(file.read(9)) # This will raise an error because the file is closed