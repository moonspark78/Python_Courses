# Methods for String
name= "root admin Root"
print(name.lower())

#First letter of the string
print(name.capitalize())

#First oh each word
print(name.title())

#Replace a word
replaced = name.replace("root", "messi")
print(replaced)


# --------------- String slicing--------------
url = "https://google.com"
print(url[8:])  # google.com
print(url[4:])  # s://google.com
print(url[5:])  # ://google.com
print(url[8:-4]) # google



#-----------------Count how many time a sub-strings---------------------------
name1 = "root user root admin"
print(name1.count("root"))

#-----------------Len()----------------------
name2= " root user root admin root "
print("the len of the strings before applying stripfunc", len(name2)) #27
name2 = name2.strip()
print("the len of the strings before applying stripfunc", len(name2)) #25 parce que ca retire les espaces devant et deriere

t= " lo"
t.lstrip() # ici ca retire l'espace a gauche
t.rstrip() # ici ca retire l'espace a droite


#---------------------String Formating----------------------

apeydo = "admin"
id = 105
print(f"My name is {apeydo} and my id is {id}")