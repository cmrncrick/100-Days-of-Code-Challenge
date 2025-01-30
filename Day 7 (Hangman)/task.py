# Flow Chart Programming to help break down complex problem

import random

word_list = ["aardvark", "baboon", "camel"]

# Randomly choose a word from the word list and assign it to a variable
# called chosen_word then print it
chosen_word = random.choice(word_list)
print(chosen_word)

# Ask user to guess a letter and assign their answer to a variable called
# guess. Make guess lowercase.
guess = str(input("Choose a letter: ")).lower()


# Check if the letter the user guessed (guess) is one of the letters in the
# chosen_word. Print "right" if it is, "wrong" if it's not.
