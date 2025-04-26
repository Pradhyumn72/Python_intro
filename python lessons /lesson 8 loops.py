# while loop 
# Python While Loop is used to execute a block of statements repeatedly until a given condition is satisfied. When the condition becomes false, the line immediately after the loop in the program is executed.

value = 1
# while value <= 10:
#     print(value)
#     if value == 5:
#         break
#     value += 1 

# while value <= 10:
#     value += 1 
#     if value == 5:
#       continue
#     print(value)
# else:
#     print("Value is now equal to " + str(value)) 

# The For Loops in Python are a special type of loop statement that is used for sequential traversal

names = ["Dave", "Shiv", "Aadhya"]
# for x in names:
#     print(x)

# for x in "Mississippi" :
#     print(x)
# for x in names:
#     if x == "Shiv":
#         break
#     print(x)

# for x in names:
#     if x == "Shiv":
#         continue
#     print(x)

# for x in range (4):
#  print(x)

# for x in range (1,4):
#  print(x)
# for x in range (5,100,5):
#  print(x)

# Nested Loops : A nested loop is a (inner) loop that appears in the loop body of another (outer) loop.

names = ["Dave", "Shiv", "Aadhya"]
actions = ["Eats", "Exercises", "Sleeps"]
#  outer loop is name as it is written above hence will distribute its element equally 
# for name in names :
#   inner loop is action
#   for action in actions:
#    print(name + " " + action + "." )

#  here vice versa as outer loop is action and ineer loop is name 
for actions in actions :

  for name in names:
   print(name + " " + actions + "." )
