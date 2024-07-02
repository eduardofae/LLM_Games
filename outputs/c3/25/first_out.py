
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

# Define the game loop
while True:
    # Get the player's move
    print(f"It's {current_player}'s turn.")
    column = int(input("Choose a column (0-9): "))

    # Check if the move is valid
    if column < 0 or column > 9 or board[0, column] != 0:
        print("Invalid move. Please choose a different column.")
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
    print(board)
