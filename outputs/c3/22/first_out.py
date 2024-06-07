
import numpy as np

# Create the game board
board = np.zeros((10, 10))

# Define the players
players = [1, 2]

# Define the game loop
while True:
    # Get the current player
    player = players[0]

    # Get the player's move
    move = input(f"Player {player}, enter your move (column): ")

    # Check if the move is valid
    if not move.isdigit() or int(move) < 1 or int(move) > 10:
        print("Invalid move. Please enter a number between 1 and 10.")
        continue

    # Check if the column is full
    if board[:, int(move) - 1].max() > 0:
        print("This column is full. Please choose another one.")
        continue

    # Place the player's piece on the board
    board[board[:, int(move) - 1] == 0, int(move) - 1] = player

    # Check if the player has won
    if check_win(board, player):
        print(f"Player {player} wins!")
        break

    # Check if the game is a draw
    if board.max() >= 1 and board.min() >= 1:
        print("It's a draw!")
        break

    # Switch to the other player
    players = players[1:] + players[:1]

# Define the function to check if a player has won
def check_win(board, player):
    # Check for horizontal wins
    for row in range(10):
        if np.all(board[row, :] == player):
            return True

    # Check for vertical wins
    for col in range(10):
        if np.all(board[:, col] == player):
            return True

    # Check for diagonal wins
    for i in range(10):
        if np.all(board.diagonal(i) == player) or np.all(np.flipud(board).diagonal(i) == player):
            return True

    return False
