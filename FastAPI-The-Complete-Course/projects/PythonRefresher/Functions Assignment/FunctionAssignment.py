"""
Function Assignment
- Create a function that takes in 3 parameters(firstname, lastname, age) and
returns a dictionary based on those values
"""


def user_dictionary(firstname, lastname, age):
    created_user_dictionary = {
        "firstname": firstname,
        "lastname": lastname,
        "age": age
    }
    return created_user_dictionary

# static input
solution_dictionary = user_dictionary(firstname="Eric", lastname="Roby", age=32)
print(solution_dictionary)

# dynamic input
first_name = input("enter your first name: ")
last_name = input("enter your last name: ")
age = int(input("enter your age: "))

solution_dictionary2 = user_dictionary(firstname=first_name, lastname=last_name, age=age)
print(solution_dictionary2)









