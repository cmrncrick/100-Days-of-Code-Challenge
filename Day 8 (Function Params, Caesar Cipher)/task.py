# def greet():
#     print("Hello")
#     print("How are you?")
#     print("Great, me as well!")


# greet()


# def greet_with_name(name: str):
#     print("Hello", name)
#     print(f"How are you {name}?")


# greet_with_name("Jack")


# def greet_with(name: str, location: str):
#     print(f"Hello {name}.")
#     print(f"What is it like in {location}?")


# greet_with(name="Julie", location="Nowhere")

def calculate_love_score(name1: str, name2: str):
    """
You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 

1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   

2. Then check for the number of times the letters in the word LOVE occurs.   

3. Then combine these numbers to make a 2 digit number and print it out. 

e.g.

name1 = "Angela Yu" name2 = "Jack Bauer"

T occurs 0 times 

R occurs 1 time 

U occurs 2 times 

E occurs 2 times 

Total = 5 

L occurs 1 time 

O occurs 0 times 

V occurs 0 times 

E occurs 2 times 

Total = 3 

Love Score = 53
    """
    names = name1 + name2
    names = names.lower()

    t = names.count("t")
    r = names.count("r")
    u = names.count("u")
    e = names.count("e")

    first_digit = t + r + u + e

    l = names.count("l")
    o = names.count("o")
    v = names.count("v")
    e = names.count("e")

    second_digit = l + o + v + e

    score = int(str(first_digit) + str(second_digit))

    print(score)


calculate_love_score("Kanye West", "Kim Kardashian")
