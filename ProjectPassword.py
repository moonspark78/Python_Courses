import random

def pass_gen(plen):
    password = ""
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
    
    for i in range(1, plen+1):
        password += random.choice(characters)