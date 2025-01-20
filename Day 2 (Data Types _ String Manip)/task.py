#################################################
# Primitive Data Types
#################################################

# # Print the index (Subscripting)
# print("Hello"[0])  # Will print H

# # Integers
# print(123+345)

# # Large Integers (Underscore in place of comma)
# print(123_345_678)

# # Float
# print(3141.59)

# # Boolean
# print(True)
# print(False)

#################################################
# Type Error, Type Checking, and Type Conversion
#################################################
# # Type Error
# len(123) # Provides error
# len("Hello") # No error

# # Type Checking
# print(type("Hello"))
# print(type(123))
# print(type(1.238))
# print(type(True))

# # Type Conversion
# print(int("123") + int("456"))

# name = input("Enter your name: ")
# length = len(name)
# print("Number of letters in your name: " + str(length))

#################################################
# Mathematical Operations
#################################################

# print(1 + 3)  # Addition
# print(7 - 3)  # Subtraction
# print(3 * 2)  # Multiplication
# print(6 / 3)  # Division
# # Division will always return a float. Use // instead for int.
# print(6 // 3)
# print(3 ** 2)  # Exponent

# PEDMAS
# ()
# **
# * OR /
# + OR -
# print(3*3+3/3-3)  # Outputs 7.0
# # 3*3 first, 3/3 second, -3 last

# # How to output 3?
# print(3 * (3 + 3) / 3 - 3)

# # BMI
# height = 1.65
# weight = 84

# # Calculate the bmi using weight and height.
# bmi = (weight / (height**2))

# print(bmi)  # Provides many decimal places
# print(round(bmi, 3))

# # Number Manipulation
# score = 0
# score += 1
# print(score)

# # f String
# print(f"Your score is", score)
# print(f"Your score is {score}")
