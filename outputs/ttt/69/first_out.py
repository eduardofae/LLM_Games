
import numpy as np

# Create the game board
board = np.zeros((3, 3))

# Define the player symbols
player1 = 'X'
player2 = 'O'

# Start the game loop
while True:
    # Get the player's move
    player = player1 if player1 == 'X' else player2
    move = input("Player {}'s turn: ".format(player))
    move = [int(x) for x in move.split(',')]

    # Check if the move is valid
    if board[move[0], move[1]] != 0:
        print("Invalid move. Please try again.")
        continue

    # Place the player's piece on the board
    board[move[0], move[1]] = player

    # Check if the player has won
    if any([
        np.all(board[i, :] == player) for i in range(3)
    ] or [
        np.all(board[:, i] == player) for i in range(3)
    ] or [
        np.all(np.diagonal(board) == player) or
        np.all(np.flip(np.diagonal(board), axis=0) == player)
    ]):
        print("Player {} wins!".format(player))
        break

    # Check if there are no more free spaces
    if np.all(board != 0):
        print("It's a draw!")
        break

    # Switch the player
    player1, player2 = player2, player1
