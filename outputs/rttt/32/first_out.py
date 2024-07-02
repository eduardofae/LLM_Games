# Import the necessary modules.
import numpy as np

# Create the game board.
board = np.zeros((3, 3))

# Define the players' turns.
player1 = 1
player2 = 2

# Define the winning lines.
winning_lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

# Start the game loop.
while True:
    # Print the game board.
    print(board)

    # Get the player's move.
    move = int(input("Player {}'s turn: ".format(player1 if player1 == 1 else player2)))

    # Place the player's piece on the board.
    board[move] = player1 if player1 == 1 else player2

    # Check if the player has won.
    for line in winning_lines:
        if board[line[0]] == board[line[1]] == board[line[2]] != 0:
            print("Player {} wins!".format(player1 if player1 == 1 else player2))
            break

    # Check if the game is a draw.
    if np.all(board != 0):
        print("Draw!")
        break

    # Switch the player's turns.
    player1, player2 = player2, player1
