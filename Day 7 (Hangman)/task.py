# Flow Chart Programming to help break down complex problem

import random
from hangman_art import stages, logo
from hangman_words import word_list

lives = 6

placeholder = ""

print(logo)

# Randomly choose a word from the word list and assign it to a variable
# called chosen_word then print it
chosen_word = random.choice(word_list)
# print(chosen_word)

# Finding length of chosen word
length = len(chosen_word)

for position in range(length):
    placeholder += "_"

game_over = False

correct_letters = []

print(placeholder)

while not game_over:

    print(f"You have {lives} lives left.")

    # Starting with blank display
    display = ""

    # Making placehold the length of the chosen word
    # placeholder = ("_" * length)

    # Ask user to guess a letter and assign their answer to a variable called
    # guess. Make guess lowercase.

    # User letter guess
    guess = str(input("Choose a letter: ")).lower()

    # Check if the letter the user guessed (guess) is one of the letters in the
    # chosen_word. Print "right" if it is, "wrong" if it's not.

    if guess in correct_letters:
        print("\nYou have already chosen that letter.")
        print("Please choose another.\n")

    # Iterating over the chosen word
    for letter in chosen_word:

        # If the iteration is equal to user guess
        if letter == guess:
            display += letter
            correct_letters.append(letter)

        # If the iteration is in the list then show it
        elif letter in correct_letters:
            display += letter

        # If the iteration is not in word show _
        else:
            display += "_"

    # If the user guess is not in chosen word
    if guess not in correct_letters:
        lives -= 1

        if lives == 0:
            game_over = True

            print("\nYou Lose!")

            print(f"The word was {chosen_word}.\n")

    print(display)

    if "_" not in display:
        game_over = True

        print("You win!")

    print(stages[lives])
