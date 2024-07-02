import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Define the players
player1 = 1
player2 = -1

# Define the current player
current_player = player1

# Game loop
while True:
    # Get the column where the player wants to place their piece
    column = int(input("Player {} choose a column (0-9): ".format(current_player)))

    # Check if the column is valid
    if column < 0 or column > 9:
        print("Invalid column")
        continue

    # Check if the column is full
    if grid[0, column] != 0:
        print("Column is full")
        continue

    # Place the player's piece in the lowest free space of the column
    for i in range(9, -1, -1):
        if grid[i, column] == 0:
            grid[i, column] = current_player
            break

    # Check if the player has won
    if check_win(grid, current_player):
        print("Player {} wins!".format(current_player))
        break

    # Check if the game is a draw
    if np.all(grid != 0):
        print("Draw")
        break

    # Switch to the other player
    current_player = -current_player

# Function to check if a player has won
def check_win(grid, player):
    # Check for horizontal wins
    for i in range(10):
        if np.all(grid[i, :] == player):
            return True

    # Check for vertical wins
    for j in range(10):
        if np.all(grid[:, j] == player):
            return True

    # Check for diagonal wins
    for i in range(7):
        if np.all(grid[i:i+3, i:i+3] == player):
            return True

    for i in range(7):
        if np.all(grid[i:i+3, 9-i:6-i] == player):
            return True

    return False
