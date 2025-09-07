## Solution from course:
import random

# I dont currently have emojis on my computer so i just paired 'r' > 'ROCK'
emojis ={ 'r': 'ROCK', 's': 'SCISSORS', 'p': 'PAPER' } # Uses a dictionary to map key > value allowing us to assign emoji to choices. we can map str to int or whatever we want with dictionaries.
choices = ('r', 'p', 's') # Uses a tupple to prevent accidental changes

while True:
    # I like this method of input validation. Feels cleaner.
    user_choice = input("Rock, paper, or scissors? (r/p/s): ").lower() 
    if user_choice not in choices: 
        print('Invalid choice.')
        continue
    
    computer_choice = random.choice(choices)

    # I like how clean the dictionary method is
    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")

    if user_choice == computer_choice:
        print("Tie!")
    elif (
        (user_choice == 'r' and computer_choice == 's') or 
        (user_choice == 's' and computer_choice == 'p') or 
        (user_choice == 'p' and computer_choice == 'r')):
        print("You win") 
        # I didnt know you could do multi-line statements with '\' after the 'or'. 
        # Much cleaner. Even cleaner still is using () to represent a long expression. 
        # Im learning alot from this one.
    else:
        print("You lose")

    should_continue = input("Continue? (y/n): ").lower()
    if should_continue == 'n':
        print("Thanks for playing!")
        break



## Reflection on solution:
#  Learned alot about dictionaries and tuples for cleaner code,
#  as well as better input validation techniques. Learned how to use parentheses and
#  back slashes for multi-line statements to improve readability.