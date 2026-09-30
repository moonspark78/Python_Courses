import os

print(os.getcwd())
print(os.listdir())
print(os.listdir()[3])


print("-----------------------------")
for i in os.listdir():
    print(i)
    
print("-----------------------------")
print(os.listdir("c:"))

""" 
os module provides a way of using operating system dependent functionality.
The os and os.path modules include many functions to interact with the file system.
"""

print(os.rmdir("test"))  # Remove a directory
print(os.rmdir("files")) 

print(os.path.exists("hello.py"))   
print(os.system("dir"))  # Execute a command in the system shell