# Write a simple number guessing game: 
# Computer picks random (1-20), user guesses until correct.

import random


computers_number = random.randint(1, 20)

while True:
    
    guess = int(input("Guess the number (1-20):\n> "))
    if guess > 20:
        print("Pick a number 1-20.")
    elif guess > computers_number:
        print("Too high!\n")
    elif guess < computers_number:
        print("Too low!\n")
    else:
        print("Congratulations! you guessed the number.")
        break