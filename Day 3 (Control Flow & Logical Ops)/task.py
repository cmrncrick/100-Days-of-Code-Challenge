# # Conditional Statements
# print("Welcome to the rollercoaster.")
# height = int(input("What is your height in cm? "))

# if height >= 120:
#     print("You can ride the rollercoaster.")
# else:
#     print("Sorry you have to grow taller before you can ride.")


# # Modulo Operator
# print(10 % 3)

# # Any even number divided my 2 with Modulo will have value of 0
# number = int(input("What number do you want to check? "))

# if (number % 2) == 0:
#     print("Your number is even.")
# else:
#     print("Your number is odd.")


# # Nested If Else Statements
# print("Welcome to the rollercoaster.")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120:
#     print("You can ride the rollercoaster.")
#     age = int(input("What is your age? "))

#     if age <= 12:
#         print("Child Ticket Price: $5")
#         bill = 5

#     elif age <= 18:
#         print("Youth Ticket Price: $7")
#         bill = 7

#     else:
#         print("Adult Ticket Price: $12")
#         bill = 12

#     wants_photo = str(input("Do you want a photo taken? Y or N ")).upper()

#     if wants_photo == "Y":
#         bill += 3

#     print(f"Your final bill is ${bill}.")


# else:
#     print("Sorry you have to grow taller before you can ride.")


# #  Pizza Program
# print("Welcome to Python Pizza Deliveries.")
# size = str(input("What size pizza do you want? S, M, or L? ")).upper()
# pepperoni = str(input("Do you want pepperoni on your pizza? Y or N? ")).upper()
# extra_cheese = str(input("Do you want extra cheese? Y or N? ")).upper()

# price = 0

# # Work out size cost
# if size == 'S':
#     price += 15

# elif size == 'M':
#     price += 20

# elif size == 'L':
#     price += 25

# else:
#     print("You typed the wrong inputs.")

# if pepperoni == "Y":
#     if size == "S":
#         price += 2
#     else:
#         price += 3

# if extra_cheese == "Y":
#     price += 1

# print(f"Final Bill: ${price}")


# # Logical Operators

# print("Welcome to the rollercoaster.")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120:
#     print("You can ride the rollercoaster.")
#     age = int(input("What is your age? "))

#     if age <= 12:
#         print("Child Ticket Price: $5")
#         bill = 5

#     elif age <= 18:
#         print("Youth Ticket Price: $7")
#         bill = 7

#     elif 45 <= age <= 55:
#         print("Free ride on us.")
#         bill = 0

#     else:
#         print("Adult Ticket Price: $12")
#         bill = 12

#     wants_photo = str(input("Do you want a photo taken? Y or N ")).upper()

#     if wants_photo == "Y":
#         bill += 3

#     print(f"Your final bill is ${bill}.")


# else:
#     print("Sorry you have to grow taller before you can ride.")
