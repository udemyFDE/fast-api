"""
String Formatting
"""


first_name = "Eric"
print("Hi " + first_name)
print(f"Hi {first_name}")

sentence = "Hi {}"
print(sentence.format(first_name))

sentence = "Hi {} {}"
last_name = "Roby"
# print(sentence.format(first_name, last_name))
print(sentence.format(first_name, last_name))

print(f"Hi {first_name} {last_name} I hope you are learning")





