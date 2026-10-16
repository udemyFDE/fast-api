'''
String Assignment we will do together:

Ask the user how many days until their birthday
and print an approx number of weeks until their birthday

Weeks is = 7 days

decimals within the return is allowed..
'''


days = int(input("How many days until your birthday? "))
# days = input("How many days until your birthday? ")
# print(round(days/7, 2))
print(f"Number of days left for your birthday: {days}")
print(F"Number of weeks left for your birthday: {round(days/7, 2)}")

# weeks = int(input("How many days until your birthday? "))
# print(F"Number of weeks left for your birthday: {round(weeks/7, 2)}")