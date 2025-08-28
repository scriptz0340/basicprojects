## My solution:
import random

while True: 
    choice = input("Roll the dice? (y/n): ") 
    if choice.lower() == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"({die1}, {die2})")
    elif choice.lower() == 'n':
        print("Thanks for playing!")
        quit()
    else:
        print("Invalid choice!")
        

# The infinite loop allows the game to continue on forever until user decides to quit.
# At first i thought to break the loop if 'y' but that would cause the program to terminate 
# after one roll instead of allowing user to keep playing.
# I also learned about the 'random' module in python, i didnt know that existed so i 
# couldnt figure out on my own how to generate the random numbers.

# I was able to figure out everything myself except generate the random numbers 
# on my own.


## Solution from course was the same as mine.