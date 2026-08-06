username="root"
passwd="admin"

name=input("Enter your username: ")
password=input("Enter your password: ")

if name==username and password==passwd:
    print("Access granted.")
else:
    print("Access denied.")
    
    
    
print("---------------")
char=input("Enter a character: ")
if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
    print("The character is a vowel.")
else: