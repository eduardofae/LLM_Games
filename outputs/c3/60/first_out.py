
import numpy as np

# Create the game board
board = np.zeros((10, 10), dtype=int)

# Define the players
player1 = 1
player2 = -1

# Define the current player
current_player = player1

# Main game loop
while True:
    # Get the player's move
    move = int(input("Player {}'s move: ".format(current_player)))

    # Place the player's piece on the board
    board[move, np.argmin(board[:, move])] = current_player

    # Check if the player has won
    if np.any(np.abs(np.sum(board, axis=0)) >= 3) or np.any(np.abs(np.sum(board, axis=1)) >= 3):
        print("Player {} wins!".format(current_player))
        break

    # Check if the game is a draw
    if np.all(board != 0):
        print("Draw!")
        break

    # Switch to the other player
    current_player = -current_player
