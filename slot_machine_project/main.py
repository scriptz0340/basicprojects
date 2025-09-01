import random  # Used for random symbol selection in the slot machine

# Game configuration constants
MAX_LINES = 3          # Maximum number of horizontal lines the player can bet on
MAX_BET = 1000000      # Maximum bet allowed per line
MIN_BET = 1            # Minimum bet allowed per line
ROWS = 3               # Number of rows in the slot machine
COLS = 3               # Number of columns in the slot machine

# How many times each symbol should appear (controls rarity)
symbol_count = {
    "$": 50000,
    "@": 100000,
    "#": 500000,
    "&": 900000,
    "*": 1000000
}

# The payout value for each symbol
symbol_value = {
    "$": 100,
    "@": 8,
    "#": 6,
    "&": 4,
    "*": 2
}

# Checks if any horizontal lines contain all matching symbols
def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):  # For each line the player bet on
        symbol = columns[0][line]  # Take the symbol in the first column for this line
        for column in columns:
            if column[line] != symbol:  # If any symbol in the line doesn't match
                break
        else:
            # All symbols in this line match
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

# Simulates a slot machine spin and returns the symbols in columns
def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    # Create a flat list of all symbols based on their frequency
    for symbol, count in symbols.items():
        all_symbols.extend([symbol] * count)

    columns = []
    for _ in range(cols):
        current_symbols = all_symbols[:]  # Copy to avoid affecting the original list
        column = []
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)  # Prevent duplicates in the same column
            column.append(value)
        columns.append(column)

    return columns

# Nicely prints the slot machine results in rows
def print_slot_machine_results(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(" |", column[row], end="")
            else:
                print(" |", column[row], end=" | ")
        print()

# Prompts the user to deposit money into their balance
def deposit():
    while True:
        amount = input("How much would you like to deposit?\n$ ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                print("Deposit received.")
                return amount
            else:
                print("Amount must be greater than 0.00!")
        else:
            print("Please enter a number.")

# Asks how many lines the user wants to bet on
def get_number_of_lines(balance):
    while True:
        lines = input(f"How many lines do you want to bet on? (1-{MAX_LINES})?\n> ")
        if lines.isdigit():
            lines = int(lines)
            if lines > balance:
                print("Insufficient funds for that many lines!")
            elif 1 <= lines <= MAX_LINES:
                return lines
            else:
                print(f"Maximum allowed lines: {MAX_LINES}")
        else:
            print("Please enter a number.")

# Prompts user for a bet amount per line
def get_bet():
    while True:
        bet = input("How much would you like to bet?\n$ ")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                print("Bet received.")
                return bet
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number.")

# Manages the full process of placing a bet and spinning the machine
def spin(balance):
    lines = get_number_of_lines(balance)

    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"Insufficient funds.\nCurrent balance: ${balance}\nAttempted bet: ${total_bet}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines.\nTotal bet: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine_results(slots)

    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}!")
    print("You won on line(s):", *winning_lines)
    return winnings - total_bet  # Net gain/loss from this spin

# Main game loop
def main():
    balance = deposit()
    print("Get 3 in a row horizontally to win!")

    while True:
        print(f"Current balance: ${balance}")
        to_spin = input("Press enter to play, 'q' to cash out, 'd' to deposit more money: ")

        if to_spin.lower() == 'q':
            break
        elif to_spin.lower() == 'd':
            balance += deposit()
        else:
            balance += spin(balance)

        if balance <= 0:
            ask = input("Would you like to deposit? (y/n) ")
            if ask.lower() == 'y':
                balance += deposit()
            else:
                break

    print(f"You cashed out ${balance}.")

# Entry point of the program
main()
