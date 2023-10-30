import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print("")
playerChoice = input("Enter...\n1 for Rock\n2 for Paper, or \n3 for Scissors: \n\n")

playerInt = int(playerChoice)

if playerInt < 1 or playerInt > 3:
    sys.exit("You must enter 1, 2, or 3.")


computerChoice = random.choice("123")

computerInt = int(computerChoice)

print("")
print("You chose " + str(RPS(playerInt)).replace("RPS.", "").lower() + ".")
print("The computer chose " + str(RPS(computerInt)).replace("RPS.", "").lower() + ".")
print("")

if playerInt == 1 and computerInt == 3:
    print("🎉You win!")
elif playerInt == 2 and computerInt == 1:
    print("🎉You win!")
elif playerInt == 3 and computerInt == 2:
    print("🎉You win!")
elif playerInt == computerInt:
    print("😲It's a tie!")
else:
    print("💻The computer wins!")