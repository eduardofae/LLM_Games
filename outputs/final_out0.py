import numpy as np

# Create a 3x3 grid
board = np.zeros((3, 3))

# Player 1's turn
current_player = 1

# Game loop
while True:
    # Get the player's move
    row, col = map(int, input("Player {}'s turn: ".format(current_player)).split())

    # Check if the move is valid
    if board[row, col] != 0:
        print("Invalid move. Try again.")
        continue

    # Place the player's piece on the grid
    board[row, col] = current_player

    # Check if the player has won
    if has_won(board, current_player):
        print("Player {} wins!".format(current_player))
        break

    # Check if the game is a draw
    if board.all():
        print("Draw!")
        break

    # Switch to the other player
    current_player = 3 - current_player

# Check if a player has won
def has_won(board, player):
    # Check rows
    for row in board:
        if np.all(row == player):
            return True

    # Check columns
    for col in board.T:
        if np.all(col == player):
            return True

    # Check diagonals
    if np.all(board.diagonal() == player) or np.all(np.flip(board).diagonal() == player):
        return True

    # No winner yet
    return False