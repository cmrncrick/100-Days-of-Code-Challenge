import random

# Password Options
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Start Generator
print("Welcome to the PyPassword Generator!")

# User Inputs
letters_inp = int(input("How many letters would you like in your password?\n"))

symbols_inp = int(input("How many symbols would you like?\n"))

numbers_inp = int(input("How many numbers would you like?\n"))

# List to store the password
password = []

# Iterations of user inputs
for number in range(0, letters_inp):

    password.append(random.choice(letters))

for number in range(0, numbers_inp):

    password.append(random.choice(numbers))

for number in range(0, symbols_inp):

    password.append(random.choice(symbols))

# Final Password (Easy Method)
# print(password)

# Final Password (Hard Method)
random.shuffle(password)

final_password = ""

for i in password:
    final_password += i

print(f"Your password is: {final_password}")
