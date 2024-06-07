import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Define the players
players = ['X', 'O']

# Define the current player
current_player = 0

# Define the game loop
while True:
    # Get the player's input
    column = int(input("Player {} choose a column (1-10): ".format(players[current_player]))) - 1

    # Check if the column is valid
    if column < 0 or column > 9:
        print("Invalid column")
        continue

    # Check if the column is full
    if grid[0, column] != 0:
        print("Column is full")
        continue

    # Place the player's piece in the column
    for i in range(9, -1, -1):
        if grid[i, column] == 0:
            grid[i, column] = players[current_player]
            break

    # Check if the player has won
    if grid[i, column] == grid[i+1, column] and grid[i, column] == grid[i+2, column]:
        print("Player {} wins!".format(players[current_player]))
        break
    if grid[i, column] == grid[i, column+1] and grid[i, column] == grid[i, column+2]:
        print("Player {} wins!".format(players[current_player]))
        break
    if grid[i, column] == grid[i+1, column+1] and grid[i, column] == grid[i+2, column+2]:
        print("Player {} wins!".format(players[current_player]))
        break
    if grid[i, column] == grid[i+1, column-1] and grid[i, column] == grid[i+2, column-2]:
        print("Player {} wins!".format(players[current_player]))
        break

    # Check if the game is a draw
    if np.all(grid != 0):
        print("Draw!")
        break

    # Switch the current player
    current_player = (current_player + 1) % 2
