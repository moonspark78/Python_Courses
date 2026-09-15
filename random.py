import random

print(random.randint(1, 10))  # Output: A random integer between 1 and 10
print(random.randrange(1,10)) # Output: A random integer between 1 and 9

print("---------------------------")
print("---------------------------")
print("---------------------------")

a=[12,2,15,32,87,66]
random.shuffle(a)
print(a)  # Output: The list 'a' shuffled in random order


chars= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
print(random.choice(chars))  # Output: A random character from the string 'chars'