import math

# # # String Data Type

# # # Literal Assignment
# first = "Opemipo"
# last = "Babalola"

# # # print(type(first))
# # # print(type(first) == str)
# # # print(isinstance(first, str))

# # # Constructor Function
# # # pizza = str("Pepperoni")
# # # print(type(pizza))
# # # print(type(pizza) == str)
# # # print(isinstance(pizza, str))

# # # Concatenation
# # fullname = first + " " + last
# # print(fullname)

# # fullname += "!"
# # print(fullname)

# # # Casting a number to a string
# # decade = str(1980)
# # print(type(decade))
# # print(decade)

# # statement = "I like rock music from the " + decade + "s."
# # print(statement)

# # # Multuple Lines
# multiline = """
# Hey, how are you?

# I was just checking in.

#                       All good?

# """

# # print(multiline)

# # # Escaping Special Characters
# # sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
# # print(sentence)

# #  String Methods

# print(first)
# print(first.lower())
# print(first.upper())
# print(first)

# print(multiline.title())
# print(multiline.replace("good", "ok"))
# print(multiline)

# print(len(multiline))
# multiline += "                                         "
# multiline = "                                     " + multiline
# print(len(multiline))

# print(len(multiline.strip()))
# print(len(multiline.lstrip()))
# print(len(multiline.rstrip()))

print("")

# Build a menu
# title = "menu".upper()
# print(title.center(20, "="))
# print("Coffee".ljust(16, ".") + "$1".rjust(4))
# print("Muffin".ljust(16, ".") + "$2".rjust(4))
# print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

# String Index Values
first = "Opemipo"
last = "Babalola"

print(first[1])
print(first[-1])
print(first[1:-1])
print(first[1:])

# Some methods return boolean data
print(first.startswith("O"))
print(first.endswith("Z"))

# Boolean Data Type
myValue = True
x = bool(False)
print(type(x))
print(isinstance(myValue, bool))

# Numeric Data Types

# Integer Type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# Float Type
gpa = 3.28
y = float(1.14)
print(type(gpa))

# Complex Type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built-in functions for numbers

print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))

print(math.pi)
print(round(math.sqrt(64)))
print(math.ceil(gpa))
print(math.floor(gpa))

#  Casting a string to a number
zipcode = "10001"
zip_value = int(zipcode)
print(type(zip_value))

# Error
# zip_value = int("New York")