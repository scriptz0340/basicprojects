## Modularized solution from course: (Refactoring by modularization practice)
import random

emojis ={ 'r': 'ROCK', 's': 'SCISSORS', 'p': 'PAPER' } 
choices = ('r', 'p', 's') 

def get_user_choice():
    while True:
        user_choice = input("Rock, paper, or scissors? (r/p/s): ").lower() 
        if user_choice in choices:  
            return user_choice
        else:
            print("Invalid choice.")  

def display_choices(user_choice, computer_choice):
    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Tie!")
    elif (
        (user_choice == 'r' and computer_choice == 's') or 
        (user_choice == 's' and computer_choice == 'p') or 
        (user_choice == 'p' and computer_choice == 'r')):
        print("You win") 
    else:
        print("You lose")

def play_game():
   while True:
    user_choice = get_user_choice()
    
    computer_choice = random.choice(choices)

    display_choices(user_choice, computer_choice)
    
    determine_winner(user_choice, computer_choice)

    should_continue = input("Continue? (y/n): ").lower()
    if should_continue == 'n':
        print("Thanks for playing!")
        break


play_game()



## Reflection on modularized solution:
#  I had to add 2 arguments to each of the functions that relied on user input because 
#  the user input is recieved inside of play_game(). In other words, the user_choice
#  and computer_choice variables are defined outside of the 2 other functions that rely 
#  on their values so they need to be passed in as arguments.