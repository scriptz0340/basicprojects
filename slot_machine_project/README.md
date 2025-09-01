# Slot Machine Game (Python CLI)

## Project Description

**Guided Project**

This is a command-line based Slot Machine game written in Python. The game simulates a 3x3 slot machine with customizable symbols, payouts, and betting mechanics. Players can deposit funds, place bets on horizontal lines, spin the slot machine, and win based on matching symbols across the rows.

This project was developed to practice fundamental Python concepts including loops, functions, user input validation, data structures, and randomization.

---

## Key Concepts Used

- **Randomization with `random` module**: Symbols are selected randomly for each spin, ensuring each game has unique results.
- **Data structures (Dictionaries and Lists)**:  
  - Dictionaries are used to define symbol frequency and payouts.  
  - Lists are used to build and display the 2D structure of the slot machine.
- **Modular Programming**: The code is broken into reusable and logically separated functions for clarity and maintainability.
- **Input Validation & Loops**: Repetitive prompting ensures robust user input handling and continuous gameplay.

---

## Example Inputs and Outputs

Below is a sample game interaction to demonstrate how the program works:

### Starting the Game

How much would you like to deposit?
$ 100
Deposit received.
Get 3 in a row horizontally to win!

### Placing a Bet

Current balance: $100
Press enter to play, 'q' to cash out, 'd' to deposit more money:

How many lines do you want to bet on? (1-3)?

    2

How much would you like to bet?
$ 10
Bet received.
You are betting $10 on 2 lines.
Total bet: $20

### Slot Machine Output

| @ | * | # |
| * | * | * |
| $ | # | $ |

You won $20!
You won on line(s): 2

### Game Flow Continues

Current balance: $100
Press enter to play, 'q' to cash out, 'd' to deposit more money:

### Ending the Game

You cashed out $80.


---

## Reflection

- I got some experience with nested loops and lists as well as some more prasctice with arguments. Also i learned 
print("Some text", *variable_name) whch will output multiple values or instances for the specified variable separated by a space.
- the program asked for the number of lines without checking the balance first so you could choose to bet on 3 lines even 
though you only had a $1 balance and the minimum bet is 1$ per line. This would cause you to get trapped inside the block that asks for bet amount.
- Some things i may add in the future: Vertical and diagonal wins, print what symbol you won with and its multiplyer, learn how to improve the odds 
( i tried to mess with the symbol count to change them but i honestly dont know how to manipulate the odds effectively.), print a list of symbols and their multiplyers along with jackpot combos, 
Add more ways to win.

> - Challenges I faced:
- General game logic troubleshooting 
- trying to add vertical and diagonal win patterns
- trying to manipulate the odds by changing symbol_count{}




---

## File Structure

slot_machine.py # Main game code
README.md # Project documentation (this file)


---

## Requirements

- Python 3.7 or higher
- import random

---

## License

This project is open-source and free to use under the [MIT License](https://opensource.org/licenses/MIT).

