## Solution from course (My first idea could have work if i used try/except):
import random 

number_to_guess = random.randint(1, 100)

while True:
    try:
        guess = int(input("Guess the number. (1-100): "))
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number.")
            break
    except ValueError:
        print("Please enter a valid number.")