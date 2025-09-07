# Pig Game (Python Console Game)

A simple console-based multiplayer dice game designed for 2-4 players built in Python! 

---

## Features

- Supports 2 to 4 players
- Turn-based dice rolling
- Strategy: roll or hold
- Automatic score tracking
- First to 50 points wins 

---

## How to Play

Each player takes turns rolling a 6-sided die:

- Rolling a **1** ends your turn and resets your turn score.
- Rolling **2 to 6** adds that number to your turn score.
- You can choose to **"hold"** at any time to keep your turn score.
- The first player to reach **50 points** wins the game (but if more than one player scores more than 50, the player with the most wins).
  Each player will get the same number of turns so the game allows the other players to roll even if player 1 hits 50 points.

---

## How to Run

1. Make sure you have Python 3 installed.

2. Clone this repository or download the Python file.

    ```bash
    git clone https://github.com/yourusername/dice-game.git
3. Navigate into the project folder and run the script:
   pig_game.py

---
## This game demonstrates:

Random number generation (random.randint())

Input validation and loops

Lists and scoring logic

Control flow with nested loops

Simple turn based game structure

---

## Example Game Output:

    Enter number of players: (2-4) 
    > 3
    
    Player 1, it's your turn!
    Your total score is: 0
    
    Would you like to roll? (y/n)
    > y
    You rolled a(n): 4
    Score for this turn: 4
    
    Would you like to roll? (y/n)
    > y
    You rolled a(n): 1
    You rolled a 1! Next player's turn.

---

## License

This project is open-source under the MIT License. You are free to use, modify, and share it.

---

## Contributing

Pull requests are welcome! If you find a bug or want to add features, feel free to open an issue or submit a PR.

