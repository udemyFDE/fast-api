"""
Functions
"""

# example-1
def my_function():
    print("Inside my_function")

my_function()


# example-2
def print_my_name(name):
    print(f"Hello {name}..!")  # can be f or F.... prefer to use f

print_my_name("yeswanth")


# example-3
def print_my_name(first_name, last_name):
    print(f"Hello {first_name} {last_name}..!")  # can be f or F.... prefer to use f

print_my_name("Steve", "Jobs")


# example-4
def print_dynamic_name(dynamic_name):
    dynamic_name = input("Enter your name: ")
    print(f"Hello, the name provided is : {dynamic_name}")

print_dynamic_name("name")



'''
# Scope - to define global variables vs internal variables
# internal variables also called as local variables -- available only for function
# global variables accessible by the entire application
'''
# example-5
def print_color_red():
    color = "Red"   # local variable for function
    print(color)

color = "Blue"  # global variable
print(color)
print_color_red()



# example-6
def print_numbers(highest_number, lowest_number):
    print(highest_number)
    print(lowest_number)

# passing just the numbers, 1st is treated as highest and 2nd one as lowest
# as in the order defined in function
print_numbers(10, 3)
print_numbers(3, 10)
# explicitly passing as highest and lowest numbers
print_numbers(lowest_number=3, highest_number=10)



# example-7
def multiply_numbers(a, b):
    return a * b

solution = multiply_numbers(2,3)
print(solution)


# example-8
def print_list(list_of_numbers):
    for x in list_of_numbers:
        print(x)

numbers_list = [1,2,3,4,5,6]
print_list(numbers_list)

# example-9
# function calling another function
def buy_item(cost_of_item):
    return cost_of_item + add_tax_to_item(cost_of_item)


def add_tax_to_item(cost_of_item):
    current_tax_rate = .03
    return cost_of_item * current_tax_rate


final_cost = buy_item(50)
print(final_cost)














