# Import the necessary modules.
import numpy as np

# Create the game board.
board = np.zeros((3, 3))

# Define the player symbols.
player1_symbol = 'X'
player2_symbol = 'O'

# Keep track of the current player.
current_player = player1_symbol

# Game loop.
while True:
    # Get the player's move.
    row, col = map(int, input("Enter your move (row, col): ").split())

    # Check if the move is valid.
    if board[row, col] != 0:
        print("Invalid move.")
        continue

    # Place the player's piece on the board.
    board[row, col] = current_player

    # Check if the player has won.
    if check_win(board, current_player):
        print(f"{current_player} wins!")
        break

    # Check if the game is a draw.
    if np.all(board != 0):
        print("Draw.")
        break

    # Switch to the other player.
    current_player = player2_symbol if current_player == player1_symbol else player1_symbol

# Print the final board.
print(board)

# Check if the player has won.
def check_win(board, player):
    # Check for horizontal wins.
    for row in range(3):
        if np.all(board[row, :] == player):
            return True

    # Check for vertical wins.
    for col in range(3):
        if np.all(board[:, col] == player):
            return True

    # Check for diagonal wins.
    if np.all(board.diagonal() == player) or np.all(np.flip(board).diagonal() == player):
        return True

    # No win yet.
    return False
