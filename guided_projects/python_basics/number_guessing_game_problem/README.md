
# Project Overview

For this project I built a number guessing game. The computer will randomly select a number and you will have infinite opportunities to guess the number. After every guess the program will print either 'Too High!' or 'Too Low!' and after guessing the number successfully, a congrats message is printed and the program terminates. 

## Reflection on my solution

- I figured out everything except how to allow the user to input letters OR numbers without a traceback.
- I was trying to convert 'guess' to int by doing 'guess = int(input(...))' so that i could use '<,>,==', but that prohibits the user from entering any str. Something like this could have worked inside of a try/except block because if the user enters a string that will trigger the ValueError and print an error message. The teacher's solution used something like this.
- I learned '.isdigit()' this will be super useful.
- I also implemented the 'random' module that i learned from the dice roll project.