# Flow Chart Programming to help break down complex problem

import random

word_list = ["aardvark", "baboon", "camel"]

placeholder = ""

# Randomly choose a word from the word list and assign it to a variable
# called chosen_word then print it
chosen_word = random.choice(word_list)
print(chosen_word)

# Finding length of chosen word
length = len(chosen_word)

for position in range(length):
    placeholder += "_"

game_over = False

correct_letters = []

print(placeholder)

while not game_over:

    display = ""
    # Making placehold the length of the chosen word
    # placeholder = ("_" * length)

    # Ask user to guess a letter and assign their answer to a variable called
    # guess. Make guess lowercase.
    guess = str(input("Choose a letter: ")).lower()

    # Check if the letter the user guessed (guess) is one of the letters in the
    # chosen_word. Print "right" if it is, "wrong" if it's not.

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(letter)

        elif letter in correct_letters:
            display += letter

        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True

        print("You win!")
