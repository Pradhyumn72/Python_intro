#literal assignment
from statistics import multimode


first= "Ashwin"
last= "Raikhere"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))
# isinstance function is used for checking the type 
# It verifies if an object is of a specified type, returning True if it is, and False otherwise

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))


#constructor function 
# The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created. 
# burger = str("italian")
# print(type(burger))
# print(type(burger) == str)
# print(isinstance(burger , str))

#Concatenation -----> joining of two strings to form a laregr string
# fullname = first + " " + last
# print(fullname)

# fullname += "hi my name is "
# print(fullname)

# # Casting a number into  a string
# decade = str(2005)
# # print(type(decade))
# # print(decade)

# statement = "I like choco from my birth " + decade + " onwards. "
# print(statement)

# # Multiple line
 
# multiline = '''
# Hey, how are you ashwin?

# I was just asking .
#                                All good?

# '''
# print(multiline)

# #Esacaping special Characters
# sentence = 'I\'m back at work!\tHey!\n\nwhere\'s this at\\located?'
# print(sentence)

# String Methods
# print(first)
# print(first.lower())
# print(first.upper())
# print(first)

# print(multiline.title())
# print(multiline.replace("was" , "am"))
# print(multiline)

# print(len(multiline))
# multiline += " "
# multiline = "                    " + multiline
# print(len(multiline))

# steps to remove extra wide spaces  (strip fucntion)
# print(len(multiline.strip()))
# print(len(multiline.lstrip()))
# print(len(multiline.rstrip()))


# Building a menu 
# title = "menu".upper()
# print(title.center(20 , "=") )
# print("coffee".ljust(10 , "-") + ">" + "$3".rjust(4))
# print("cake.".ljust(16, "-") + ">" + "$4".rjust(5))

# String index values

# print(first[1])
# print(first[-1])
# # print(first[1 :,-1])
# print(first[1:])

# Some methods return boolean data
# print(first.startswith("A"))
# print(first.startswith("Z"))

# Boolean Data
# myvalue =  True
# x = bool(False)
# print(type(x))
# print(isinstance(myvalue, bool))

# numeric data type
# Integer type

# price = 6000
# best_price = int(5500)
# print(type(price))
# print(isinstance(best_price, int))

#  Float type
# gpa = 8.56
# y= float(8.43)
# print(type(gpa))

# Complex value
# comp_value = 5+3j
# print(type(comp_value))
# print(comp_value.real)
# print(comp_value.imag)

# Bulit in functions
# print(abs(gpa))
# print(round(gpa))
# print(round(gpa, 1))
# print(abs(gpa * -1))

import math

# print(math.pi)
# print(math.sqrt(90))
# ceil function rounds off to next integer
# print(math.ceil(gpa))
# floor function rounds off to previous integer
# print(math.floor(gpa))

# Casting a string to number
# pincode = "462039"
# pin_value = int(pincode)
# pincode = print((type(pin_value)))
 





