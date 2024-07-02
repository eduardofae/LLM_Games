import numpy as np

# Create the game board
board = np.zeros((10, 10))

# Define the player symbols
player1_symbol = "X"
player2_symbol = "O"

# Define the current player
current_player = player1_symbol

# Define the winning combinations
winning_combinations = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)],
]

# Define the error handling function
def handle_error(move):
    if move < 0 or move > 9:
        return "Column is out of bounds."
    elif board[0, move] != 0:
        return "Column is already full."
    else:
        return None

# Define the function to print the game board
def print_board():
    print(board)

# Define the function to get player input
def get_player_input():
    column = int(input("Choose a column (0-9): "))
    return column

# Define the game loop
while True:
    # Get the player's move
    print(f"It's {current_player}'s turn.")
    column = get_player_input()

    # Check if the move is valid
    error_message = handle_error(column)
    if error_message:
        print(error_message)
        continue

    # Place the player's piece on the board
    for i in range(9, -1, -1):
        if board[i, column] == 0:
            board[i, column] = current_player
            break

    # Check if the player has won
    for winning_combination in winning_combinations:
        if all(board[i, j] == current_player for i, j in winning_combination):
            print(f"{current_player} wins!")
            break

    # Check if the game is a draw
    if np.all(board != 0):
        print("It's a draw!")
        break

    # Switch the current player
    if current_player == player1_symbol:
        current_player = player2_symbol
    else:
        current_player = player1_symbol

    # Print the game board
    print_board()
