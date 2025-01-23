import random as r

from art import *

user_choice = int(
    input("What do you choose? 0 for Rock, 1 for Paper, 2 for Scissors. "))

computer_choice = r.randint(0, 2)

# User picks rock
if user_choice == 0:
    print(rock)

    if computer_choice == 1:
        print(f"Computer chose:\n{paper}")
        print("You win.")
    else:
        print("You lose.")

# User picks paper
elif user_choice == 1:
    print(paper)

    if computer_choice == 2:
        print(f"Computer chose:\n{scissors}")
        print("You win.")
    else:
        print("You lose.")

# User picks scissors
elif user_choice == 2:
    print(scissors)

    if computer_choice == 1:
        print(f"Computer chose:\n{rock}")
        print("You win.")
    else:
        print("You lose.")

# Both choose the same
elif user_choice == computer_choice:
    print("It's a draw!")

# User picks invalid number
else:
    print("You typed an invalid number. You lose!")
