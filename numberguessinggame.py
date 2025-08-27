import random

number_to_guess = random.randint(1, 100)

while True:
    guess = input("Guess the number. (1-100): ")
    if guess.isdigit():
        guess = int(guess)
        if guess == number_to_guess:
            print("Congratulations! You guessed the number.")
            break
        elif guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
    else:
        print("Please choose a valid number.")


# I figured out everything except how to allow the user to input letters OR numbers without a traceback.
# I was trying to convert 'guess' to int by doing 'guess = int(input(...))' so that i could use '<,>,==', but that prohibits the user from entering any str.
# I learned '.isdigit()' this will be super useful.
# I also implemented the 'random' module that i learned from the last project.


## try and except could have worked with the method i tried at first (I realized this when i watched the solution to this problem.)

# import random 

# number_to_guess = random.randint(1, 100)

# while True:
#     try:
#         guess = int(input("Guess the number. (1-100): "))
#         if guess < number_to_guess:
#             print("Too low!")
#         elif guess > number_to_guess:
#             print("Too high!")
#         else:
#             print("Congratulations! You guessed the number.")
#             break
#     except ValueError:
#         print("Please enter a valid number.")