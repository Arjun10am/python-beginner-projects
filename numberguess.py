# number guessing game

import random

computer_guess = random.randint(0, 100)


user_guess = int(input("Guess any number between 0 to 100 - "))

if user_guess > computer_guess:
    print("Too high")

elif user_guess < computer_guess:
    print("Too low")


elif user_guess == computer_guess:
    print("congratulation you guessed the correct number  ")
