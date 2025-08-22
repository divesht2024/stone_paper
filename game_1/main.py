'''
We assign numeric values to each choice:
stone   ->  1
paper   -> -1
scissor ->  0
'''
import random

# Computer randomly selects one option from stone (1), paper (-1), or scissor (0)
computer = random.choice([-1, 0, 1])

# Take input from the user (they must type "stone", "paper", or "scissor")
youStr = input("Enter choice between stone, paper, scissor: ")

# Dictionary to map user input strings to numeric values
youDict = {"stone": 1, "paper": -1, "scissor": 0}

# Reverse dictionary to map numeric values back to strings (for displaying results)
reverseDict = {1: "stone", -1: "paper", 0: "scissor"}

# Convert user's input into numeric form
you = youDict[youStr]

# Print choices of user and computer in words
print("Your choice is", reverseDict[you])
print("Computer choice is", reverseDict[computer])

# Check game result
if computer == you:
    # Same choice = draw
    print("Its a draw")
else:
    # Corrected win/lose conditions
    if (computer == 1 and you == -1):   # Stone vs Paper -> Paper wins
        print("You won")
    elif (computer == 1 and you == 0):  # Stone vs Scissor -> Stone wins
        print("You lose")
    elif (computer == -1 and you == 1): # Paper vs Stone -> Paper wins
        print("You lose")
    elif (computer == -1 and you == 0): # Paper vs Scissor -> Scissor wins
        print("You won")
    elif (computer == 0 and you == 1):  # Scissor vs Stone -> Stone wins
        print("You won")
    elif (computer == 0 and you == -1): # Scissor vs Paper -> Scissor wins
        print("You lose")
    else:
        print("Something is wrong")  # Just in case of invalid state
