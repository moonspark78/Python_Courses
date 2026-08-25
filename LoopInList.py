files = ["backup.txt", "document.txt", "demo.txt"]

for i in files:
    print(i)
    
for i in files:
    if i == "document.txt":
        print("Found the document!")
        break