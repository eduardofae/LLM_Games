
# Import the necessary libraries.
import numpy as np

# Define the game board.
board = np.zeros((3, 3))

# Define the players.
players = ["X", "O"]

# Define the game loop.
while True:
    # Get the current player.
    player = players[0]

    # Get the player's move.
    move = input(f"Player {player}, enter your move (row, column): ")

    # Check if the move is valid.
    if not (0 <= move[0] < 3 and 0 <= move[1] < 3 and board[move[0], move[1]] == 0):
        print("Invalid move. Please try again.")
        continue

    # Place the player's piece on the board.
    board[move[0], move[1]] = player

    # Check if the player has won.
    if (
        (board[move[0], 0] == player and board[move[0], 1] == player and board[move[0], 2] == player)
        or (board[0, move[1]] == player and board[1, move[1]] == player and board[2, move[1]] == player)
        or (board[0, 0] == player and board[1, 1] == player and board[2, 2] == player)
        or (board[0, 2] == player and board[1, 1] == player and board[2, 0] == player)
    ):
        print(f"Player {player} wins!")
        break

    # Check if the game is a draw.
    if np.all(board != 0):
        print("Draw!")
        break

    # Switch to the next player.
    players = players[1:]
