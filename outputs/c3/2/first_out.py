import numpy as np

# Create the game board
board = np.zeros((10, 10), dtype=int)

# Define the players
players = [1, 2]

# Define the current player
current_player = 0

# Game loop
while True:
    # Get the column where the player wants to place their piece
    column = int(input(f"Player {players[current_player]}, enter the column where you want to place your piece: ")) - 1

    # Check if the column is valid
    if column < 0 or column > 9:
        print("Invalid column. Please enter a column between 1 and 10.")
        continue

    # Check if the column is full
    if board[9, column] != 0:
        print("The column is full. Please choose another column.")
        continue

    # Place the player's piece in the column
    for i in range(9, -1, -1):
        if board[i, column] == 0:
            board[i, column] = players[current_player]
            break

    # Check if the player has won
    if check_win(board, players[current_player]):
        print(f"Player {players[current_player]} wins!")
        break

    # Check if the game is a draw
    if np.all(board != 0):
        print("The game is a draw.")
        break

    # Switch to the other player
    current_player = (current_player + 1) % 2

# Function to check if a player has won
def check_win(board, player):
    # Check for horizontal wins
    for i in range(10):
        for j in range(7):
            if board[i, j] == player and board[i, j+1] == player and board[i, j+2] == player:
                return True

    # Check for vertical wins
    for i in range(7):
        for j in range(10):
            if board[i, j] == player and board[i+1, j] == player and board[i+2, j] == player:
                return True

    # Check for diagonal wins
    for i in range(7):
        for j in range(7):
            if board[i, j] == player and board[i+1, j+1] == player and board[i+2, j+2] == player:
                return True
    for i in range(7):
        for j in range(2,10):
            if board[i, j] == player and board[i+1, j-1] == player and board[i+2, j-2] == player:
                return True

    # No win found
    return False
