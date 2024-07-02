import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Define the players
player1 = 1
player2 = 2

# Define the current player
current_player = player1

# Define the game loop
while True:
    # Get the column where the current player wants to place their piece
    column = int(input("Player {}'s turn. Enter a column (0-9): ".format(current_player)))

    # Check if the column is valid
    if column < 0 or column > 9:
        print("Invalid column. Please try again.")
        continue

    # Check if the column is full
    if grid[9, column] != 0:
        print("Column {} is full. Please try again.".format(column))
        continue

    # Place the current player's piece in the lowest free space of the column
    for row in range(9, -1, -1):
        if grid[row, column] == 0:
            grid[row, column] = current_player
            break

    # Check if the current player has won
    if check_win(grid, current_player):
        print("Player {} has won!".format(current_player))
        break

    # Check if the game is a draw
    if np.all(grid != 0):
        print("The game is a draw.")
        break

    # Switch the current player
    current_player = 3 - current_player

# Define the function to check if a player has won
def check_win(grid, player):
    # Check for horizontal wins
    for row in range(10):
        if np.all(grid[row, :] == player):
            return True

    # Check for vertical wins
    for column in range(10):
        if np.all(grid[:, column] == player):
            return True

    # Check for diagonal wins
    for i in range(10):
        if np.all(grid[i, i] == player):
            return True
        if np.all(grid[i, 9 - i] == player):
            return True

    # No wins found
    return False
