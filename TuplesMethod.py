a=(1,2,4,57,87,53,239,8,52)
print(type(a))  # Output: <class 'tuple'>
a =list(a)  # Converting the tuple to a list

a.insert(2, 100)  # Inserting the value 100 at index 2
print(a)  # Output: [1, 2, 100, 4, 57, 87, 53, 239, 8, 52]

print(len(a))  # Output: 10, the length of the list after insertion


print("---------------------------")
user={"name": "John", "age": 30, "city": "New York"}