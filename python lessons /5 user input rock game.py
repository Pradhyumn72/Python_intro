import sys 
import random
from enum import Enum
# An enumeration is a set of symbolic names (members) bound to unique values
# we use \n for leaving a line 
class RPS(Enum):
    Rock = 1
    Paper = 2
    Scissors = 3 
print("")
playerchoice = input("Enter...\n1 for rock,\n2 for paper,or \n3 for scissor:\n\n\n")
3
player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("You must enter 1, 2, or 3.")
    
computerchoice = random.choice("123")
computer = int(computerchoice)
print("")
print("You chose" + str(RPS(player)).replace('RPS.', "") + ".")
print("Python chose" + str(RPS(computer)).replace('RPS.', "") + ".")
print("")

#  we cannot use multiple if else in a single line hence we use elif s
if player == 1 and computer == 3:
    print("You win")
elif player == 2 and computer == 1:
    print("You win")   
elif player == 3 and computer == 2 :
    print("You win")
else :
    print("Python wins")