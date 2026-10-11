"""
Sets are similar to lists but are unordered and cannot contain duplications
Use curly brackets
"""

my_set = {1, 2, 3, 4, 5, 1, 2}
print(my_set)
print(len(my_set))


# Python sets are unordered collections
# Sets cannot be called using index , values of set in python can be in any location of memory
# print(my_set[0])  # will give error

# To call the values using index, we need to either loop through the set or type cast the set

# for x in my_set:
#     print(x)
#

# my_list = list(my_set)
# print(my_list[0])

# remove any value from set
my_set.discard(3)
print(my_set)

# To remove all elements from the set
my_set.clear()
print(my_set)

# add a value to set
my_set.add(6)
print(my_set)

# add more than one value to a set
my_set.update([7, 8])
print(my_set)
# even if we add values in order the output need not be in order as the sets are unordered


'''
Tuples are similar to list but are immutable meaning cannot be changed/modified after created
'''
my_tuple = (1, 2, 3, 4, 5, 1, 2)
print(my_tuple)
print(my_tuple[1])
# my_tuple[1] = 100   # item assignment not supported



tuple2 = (1, [1,2], 3, 4)
print(tuple2)

# since the 2nd element is a list within tuple can be modified as this do not change the tuple elements
tuple2[1].append(5)
print(tuple2)

# append the list
tuple2[1].append([6,7])
print(tuple2)
# output --> (1, [1,2,5,[6,7]], 3, 4)

# extend the list
tuple2[1].extend([6,7])
print(tuple2)
# output --> (1, [1,2,5,[6,7], 6, 7], 3, 4)





















