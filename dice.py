# Dice roller simulator

import random


while True:
    user = input("Do you wish to roll the dice (y/n)")
    if user == "y":
        dice_number = random.randint(1, 6)
        print(dice_number)

    elif user == "n":
        print("Goodbye")
        break

    else:
        print("Invalid input")
