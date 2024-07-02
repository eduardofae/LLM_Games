import numpy as np

# Define the game board
board = np.zeros((3, 3))

# Define the players
players = ["X", "O"]

# Keep track of the current player
current_player = 0

# Main game loop
while True:
    # Get the player's move
    move = input(f"Player {players[current_player]}, please enter your move (row, column): ")
    row, column = map(int, move.split(","))

    # Check if the move is valid
    if board[row, column] != 0:
        print("Invalid move. Please try again.")
        continue

    # Place the player's piece on the board
    board[row, column] = players[current_player]

    # Check if the player has won
    if np.any(np.all(board == players[current_player], axis=0)) or \
       np.any(np.all(board == players[current_player], axis=1)) or \
       np.all(board.diagonal() == players[current_player]) or \
       np.all(np.flip(board).diagonal() == players[current_player]):
        print(f"Player {players[current_player]} wins!")
        break

    # Check if the game is a draw
    if np.all(board != 0):
        print("Draw!")
        break

    # Switch to the other player
    current_player = (current_player + 1) % 2
