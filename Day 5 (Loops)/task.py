# # For Loop
# fruits = ['apple', 'peach', 'pear']

# for fruit in fruits:
#     print(fruit)
#     print(fruit + " pie")

# print(fruits)

# # Highest Score
# scores = [150, 231, 125, 78, 56, 21, 64]

# total_score = sum(scores)
# print(total_score)

# # Highest score using for loop
# sum = 0
# for score in scores:
#     sum += score

# print(sum)

# # Max For Loop
# scores = [150, 231, 125, 78, 56, 21, 64]

# m = 0

# for score in scores:
#     if score > m:
#         m = score

# print(m)

# # Range
# # Starting Number, Ending Number (NOT Inclusive), Step Range
# sum_range = range(1, 11, 2)

# print(sum_range)

# for number in sum_range:
#     print(number)

# total = 0

# for number in range(1, 101):
#     total += number

# print(total)

# Fizz Buzz Game

# You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:
# Your program should print each number from 1 to 100 in turn and include number 100.
# But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
