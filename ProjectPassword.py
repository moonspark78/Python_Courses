import random

def pass_gen(plen):
    password = ""
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
    
    for i in range(1, plen+1):
        password += random.choice(characters)
        print(password)        

plen = int(input("Enter the length of the password: "))
if plen < 8:

print("Your password is: " + pass_gen(plen))