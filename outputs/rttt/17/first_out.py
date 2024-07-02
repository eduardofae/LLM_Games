# Import the necessary libraries.
import numpy as np

# Define the game board.
board = np.zeros((3, 3))

# Define the player symbols.
player1_symbol = 'X'
player2_symbol = 'O'

# Define the current player.
current_player = player1_symbol

# Define the game loop.
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

# Define the function to check if a player has won.
def check_win(board, player):
    # Check for horizontal wins.
    for i in range(3):
        if np.all(board[i, :] == player):
            return True

    # Check for vertical wins.
    for j in range(3):
        if np.all(board[:, j] == player):
            return True

    # Check for diagonal wins.
    if np.all(board.diagonal() == player):
        return True
    if np.all(np.flip(board).diagonal() == player):
        return True

    # Otherwise, the player has not won.
    return False
