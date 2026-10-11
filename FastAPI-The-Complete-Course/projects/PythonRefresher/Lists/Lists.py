"""
Lists are a collection of data
"""

my_list = [80, 96, 72, 100, 8]
people_list = ["john", "robert", "albert"]

print(my_list)
print(my_list[0])

print(people_list)

# replace the value in a list by using index
people_list[1] = "anthony"
print(people_list)

# find the length of a list
print(len(people_list))

# add/append a value to a list, will add the value as the last element
my_list.append(1000)
print(my_list)

# insert/add a value to a list at specific index
my_list.insert(2, 1000)
# my_list.insert(2, 1000)
print(my_list)

# remove a value from the list by giving the value
my_list.remove(8)
print(my_list)

# remove the value from a list using the index
# my_list.pop(0)
removed_item = my_list.pop(0)
print(removed_item)
# remove the value in the given index and update the list without that value
print(my_list)

# order the list
my_list.sort()
print(my_list)
people_list.sort()
print(people_list)

# slicing -- to print only the specific data of list
# x:y -->
# x denotes the starting index
# y denotes the count from index 'x' or ending index as y-1
print(people_list[0:2])
print(my_list[2:4])








