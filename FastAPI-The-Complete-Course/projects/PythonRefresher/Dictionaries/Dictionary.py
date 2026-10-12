"""
Dictionaries - have key-value pairs
"""

user_dictionary = {
    'username': 'codingwithroby',
    'name': 'Eric',
    'age': 32
}

print(user_dictionary)

# adding element
user_dictionary["married"] = True
print(user_dictionary)

# find the length of dictionary
print(len(user_dictionary))

# calling an element using the key (not index)
print(user_dictionary.get("username"))
print(user_dictionary.get("username"), user_dictionary.get("name"))

# if the key doesn't exist then get() will return 'None' if no value is specified
print(user_dictionary.get("location"))
# output -- None

# if the key doesn't exist then get() will return the specified value.
print(user_dictionary.get("location", "hyderabad"))
# output -- hyderabad


# copy the dictionary to another variable
user_dictionary2 = user_dictionary.copy()
# remove the element using the key (not index)
user_dictionary2.pop("age")
print(user_dictionary2)


#  loop though the dictionary

for x in user_dictionary:
    print(x)
# this will print only the keys

# print only keys
for x in user_dictionary.keys():
    print(x)

# print only values
for x in user_dictionary.values():
    print(x)

for x, y in user_dictionary.items():
    # print(x, y)
    print(F"{x}: {y}")
# print the keys and values




# clear the dictionary
user_dictionary.clear()
print(user_dictionary)

# delete the dictionary
del user_dictionary
# after deleting the print will give error as the dictionary do not exist
# print(user_dictionary)





















