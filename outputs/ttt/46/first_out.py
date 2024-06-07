import numpy as np

# Create the game board
board = np.zeros((3, 3))

# Create a list of the possible winning combinations
winning_combinations = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]

# Define the players
players = ["X", "O"]

# Start the game
player_turn = 0
while True:
    # Get the player's move
    move = int(input(f"Player {players[player_turn]}, enter your move (1-9): ")) - 1

    # Check if the move is valid
    if move < 0 or move > 8 or board[move] != 0:
        print("Invalid move. Please try again.")
        continue

    # Place the player's piece on the board
    board[move] = players[player_turn]

    # Check if the player has won
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] != 0:
            print(f"Player {players[player_turn]} wins!")
            break

    # Check if the game is a draw
    if np.all(board != 0):
        print("The game is a draw.")
        break

    # Switch to the other player's turn
    player_turn = (player_turn + 1) % 2
