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
print(f"My name is {apeydo} and  {34*34}")
print(f"My name is {apeydo} and  {34/46:.2f}") # Por avoir 2 chiffre apres la virgule
print(f"My name is {apeydo} and  {34/46:.4f}") # Por avoir 4 chiffre apres la virgule

nom = "root"
id = 1005
print("My name is {}".format(nom)) #Result = My name is root
print("My name is {} and id is {}".format(nom, id)) #Result = My name is root and id is 1005



#------------------Introduction Operators----------------------------------
print("Addition is ", 45+56)
print("Multiplication is ", 56*867)
print("Subtraction is ", 56 - 867)
print("Remainder is : ", 45%5)
print("Division is ", 45/5)

#on peut stocker les valeurs dans des variables 
print("--------------------")
a=50
b=2
print("Addition is ", a+b)
print("Multiplication is ", a*b)
print("Subtraction is ", a - b)
print("Remainder is : ", a % b)
print(f"Division is , {a / b:.4f}")

#---------------------BOOLEAN DATA TYPES-------------------------------
print("--------------------")
print("--------------------")
print("--------------------")
print("---------BOOLEAN DATA TYPES-----------")
          #True 1
          #False 0
print(12>6)  #True

t=True
s=False
print(s) #False
print(type("t")) # <class 'str'>



#-----------Input User----------------
#x = input('Entrer any number : ')
#name = input("Entrer your name ")
#print("Your number is : ",x, "hello ", name)


#------------Type Casting---------------------------
#allows us to convert one data type into another for example , turning a string into an integer
print("--------Type Casting--------")
e= 45.56
print(e, type(e)) #<class 'float'>
e=int(e) #Convert float to int
print(e, type(e)) #<class 'int'>


print("------")
print("------")
print("------")

t= 45
print(t, type(t)) #<class 'int'>
t=float(t) #Convert int to float
print(t, type(t)) #<class 'float'>

print("------")
print("------")

r = input("Enter any number : ") #Parce que input() retourne une string, on doit convertir la valeur en int pour pouvoir faire des operations mathematiques
a = int(r) #Convert string to int
print(a+7)

print("------")
o1 = input("Enter any number : ")
o2 = input("Enter any number : ")
print(int(o1) + int(o2))

print("------")
r1 = int(input("Enter any number : "))
r2 = int(input("Enter any number : "))
print(r1 + r2)
