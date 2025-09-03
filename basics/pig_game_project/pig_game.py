import random  # Importing the 'random' module to use for generating random numbers (dice rolls)

# Define a function that simulates rolling a 6-sided die
def roll(): 
    roll = random.randint(1, 6)  # Randomly choose an integer between 1 and 6 (inclusive)
    return roll  # Return the rolled value

# Loop until the user inputs a valid number of players (between 2 and 4)
while True:
    players = input("Enter number of players: (2-4) \n> ")  # Ask user for number of players
    if players.isdigit():  # Check if input is numeric
        players = int(players)  # Convert input string to integer
        if 2 <= players <= 4:  # Ensure the number of players is within allowed range
            break  # Exit loop if valid
        else:
            print("Oops! 2 - 4 players per game.")  # Prompt if number is out of bounds
    else:
        print("Oops! Please enter a number.")  # Prompt if input is not numeric

# Set the maximum score to win the game
max_score = 50

# Initialize all players' scores to 0 using a list comprehension
player_scores = [0 for _ in range(players)]

# Continue the game until at least one player's score reaches or exceeds 50
while max(player_scores) < 50:

    # Loop through each player's turn
    for player_index in range(players):
        print("\nPlayer", player_index + 1, ", it's your turn!")
        print("Your total score is:", player_scores[player_index])
        current_score = 0  # Temporary score for this turn only
        
        # Player chooses to roll or hold
        while True:
            should_roll = input("\nWould you like to roll? (y/n)\n> ")  # Ask if the player wants to roll
            if should_roll.lower() != 'y':  # If player chooses not to roll
                player_scores[player_index] += current_score  # Add current turn's score to total score
                break  # End player's turn
            
            value = roll()  # Simulate rolling the die
            if value == 1:
                print("\nYou rolled a 1! Next player's turn.")  # If 1 is rolled, turn ends and score resets
                current_score = 0  # Reset turn score
                break  # End player's turn
            else:
                current_score += value  # Add rolled value to current turn's score
                print("\nYou rolled a(n):", value)
                print("Score for this turn:", current_score)

# Once someone reaches 50, determine the winner
max_score = max(player_scores)  # Get the highest score
winning_index = player_scores.index(max_score)  # Get index of the winning player
winner = winning_index + 1  # Player numbers start at 1, so add 1
print("Congratulations player number", winner, "! You won with a score of", max_score, "!")
