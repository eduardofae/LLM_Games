import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Define the players
players = [1, 2]

# Define the current player
current_player = 0

# Define the game loop
while True:
    # Get the column where the player wants to place their piece
    column = int(input("Player {}: Enter a column (1-10): ".format(players[current_player]))) - 1

    # Check if the column is valid
    if column < 0 or column > 9:
        print("Invalid column. Please enter a number between 1 and 10.")
        continue

    # Check if the column is full
    if grid[0, column] != 0:
        print("Column {} is full. Please choose another column.".format(column + 1))
        continue

    # Place the player's piece in the column
    for i in range(9, -1, -1):
        if grid[i, column] == 0:
            grid[i, column] = players[current_player]
            break

    # Check if the player has won
    if check_win(grid, players[current_player]):
        print("Player {} wins!".format(players[current_player]))
        break

    # Check if there are no more free spaces
    if np.all(grid != 0):
        print("Draw!")
        break

    # Switch to the other player
    current_player = (current_player + 1) % 2

# Define the function to check if a player has won
def check_win(grid, player):
    # Check for horizontal wins
    for i in range(10):
        if np.all(grid[i] == player):
            return True

    # Check for vertical wins
    for j in range(10):
        if np.all(grid[:, j] == player):
            return True

    # Check for diagonal wins
    for i in range(10):
        for j in range(10):
            if grid[i, j] == player and grid[i+1, j+1] == player and grid[i+2, j+2] == player:
                return True
            if grid[i, j] == player and grid[i+1, j-1] == player and grid[i+2, j-2] == player:
                return True
    return False
