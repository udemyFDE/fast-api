"""
For & While Loops
"""

# for loops

# for loop-1
my_list = [1,2,3,4,5]

for x in my_list:
    print(x)


# for loop-2

sum_of_for_loop = 0

for x in my_list:
    sum_of_for_loop += x
print(sum_of_for_loop)

# output -- 15


# for loop-3
# range(x) -- values until x-1
for y in range(4):
    print(y)


# OR

# y = 0
#
# for y in range(4):
#     print(y)
#     y += 1

# for loop-4
# range(x,y) -- values starting from x to y-1
for z in range(3,7):
    print(z)


# for loop-5

days_list = ["Monday", "Tuesday", "Wednesday", "Thursday"]

for x in days_list:
    print(F"Happy {x}..!!")


# while loop
# slightly different, it will continue until a condition is met

# while loop-1
i = 0

while i < 5:
    i += 1
    print(i)
 # output 1,2,3,4,5

#  OR

# while i < 5:
#     print(i)
#     i += 1

#  output 0,1,2,3,4


# while loop-2
i = 0

while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
    if i == 4:
        break
else:
    print("i is now larger or equal to 5")

# OR

# while i < 5:
#     i += 1
#     if i == 3:
#         continue
#     print(i)
# else:
#     print("i is now larger or equal to 5")


# while loop-3
i = 0

while i < 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1
else:
    print("i is now larger or equal to 5")

# OR

# while i < 5:
#     if i == 3:
#         i += 1
#         continue
#     print(i)
#     if i == 4:
#         break
#     i += 1
# else:
#     print("i is now larger or equal to 5")


















