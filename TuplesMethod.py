a=(1,2,4,57,87,53,239,8,52)
print(type(a))  # Output: <class 'tuple'>
a =list(a)  # Converting the tuple to a list

a.insert(2, 100)  # Inserting the value 100 at index 2
print(a)  # Output: [1, 2, 100, 4, 57, 87, 53, 239, 8, 52]

print(len(a))  # Output: 10, the length of the list after insertion


print("---------------------------")
user={"name": "John", "age": 30, "city": "New York"}
user.clear()  # Clearing all items from the dictionary

user_backup = user.copy()  # Creating a copy of the cleared dictionary
print(user_backup)  # Output: {}, the copied dictionary is also empty

print(user.keys())
print(user.values())
print(user.items())

""" Maintenant pour rajouter des éléments à un dictionnaire, vous pouvez utiliser la méthode update()
ou simplement assigner de nouvelles paires clé-valeur. Voici un exemple : """

user.update({"Address": "23 Street no 7", "Job": "Engineer"})  # Adding new key-value pairs to the dictionary
print(user)  # Output: {'Address': '23 Street no 7'}

print(len(user))  # Output: 2, the length of the dictionary after adding new items

#Pour supprimer le dernier élément d'un dictionnaire, vous pouvez utiliser la méthode popitem(). Voici un exemple :
user.popitem()  # Removing the last inserted item from the dictionary
print(user)  # Output: {'Address': '23 Street no 7'}, the dictionary


#-----------------------------------------------

#Loop in dictionary
pearson = {"name": "Alice", "age": 25, "city": "Los Angeles"}
for i in user.keys():
    print(i)  # Output: Address, Job
    
for i in user.values():
    print(i)  # Output: 23 Street no 7, Engineer
    
for key, value in user.items():
