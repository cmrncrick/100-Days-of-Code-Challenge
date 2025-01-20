t = r"""                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/             /
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|==== .'.'^'.'.===|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
"""
print(t)

print("\nWelcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

direction = str(
    input("What direction do you want to go? Left or Right? ")).capitalize()

if direction == "Left":

    water = str(
        input("You're at a river but there's a boat coming. Swim or wait? ")).capitalize()

    if water == "Wait":

        print("Good choice.")

        door = str(
            input("Which color door do you choose? Red, Blue, Yellow, Other? ")).capitalize()

        if door == "Red":

            print("Burned by fire. Game over.")

        elif door == "Blue":

            print("Eaten by beasts. Game over.")

        elif door == "Yellow":

            print("YOU WIN!!!")

        else:

            print("Game over.")

    else:
        print("Attacked by trout. Game over.")

else:
    print("Fall into a hold. Game over.")
