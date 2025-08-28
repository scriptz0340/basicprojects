## My solution:
import random

def r_p_s():
    options = ["Rock", "Paper", "Scissors"]
    while True:
        user_choice = input("Rock, paper, or scissors? (r/p/s): ")
        if user_choice.lower() == 'r':
            print("You chose: Rock")
            computer_choice = random.choice(options)
            print(f"Computer chose: {computer_choice}")
            if computer_choice.title() == 'Rock':
                print("It's a tie...")
                break
            elif computer_choice.title() == 'Paper':
                print("You lose.")
                break
            else:
                print("You win!")
                break
        elif user_choice.lower() == 'p':
            print("You chose: Paper")
            computer_choice = random.choice(options)
            print(f"Computer chose: {computer_choice}")
            if computer_choice.title() == 'Rock':
                print("You win!")
                break
            elif computer_choice.title() == 'Paper':
                print("It's a tie...")
                break
            else:
                print("You lose.")
                break
        elif user_choice.lower() == 's':
            print("You chose: Scissors")
            computer_choice = random.choice(options)
            print(f"Computer chose: {computer_choice}")
            if computer_choice.title() == 'Rock':
                print("You lose.")
                break
            elif computer_choice.title() == 'Paper':
                print("You win!")
                break
            else:
                print("It's a tie...")
                break
        else:
            print("Invalid choice!")

def main():
    r_p_s()
    playing = True
    while playing:
        play_again = input("Keep playing? (y/n): ")
        if play_again == 'y':
            main()
        elif play_again == 'n':
            print("Thanks for playing!")
            playing = False
        else:
            print("Invalid choice!")
            continue


main()



## Reflection on my solution:
# I was able to figure out everything on my own for this project except for 2 things:
#     1. I knew i had to use the random module again but I wasn't sure exactly which function to use so i asked copilot and it returned 'random.choice()'
#     2. I had a problem with the play again loop that made it ask if i wanted to play again 3 times before quitting even if i said no every time.
#     I asked copilot and it told me to use 'playing = True, while playing:' instead of 'while True' and a break statement.
# Pretty fun project overall. I found this one interesting.