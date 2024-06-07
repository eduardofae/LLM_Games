import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Define the players
players = ['X', 'O']

# Define the game loop
while True:

    # Get the current player
    player = players[0]

    # Get the column where the player wants to place their piece
    column = int(input("Player {}, choose a column (0-9): ".format(player)))

    # Check if the column is valid
    if column < 0 or column > 9:
        print("Invalid column. Please choose a column between 0 and 9.")
        continue

    # Check if the column is full
    if grid[0, column] != 0:
        print("Column {} is full. Please choose another column.".format(column))
        continue

    # Place the player's piece in the column
    for i in range(9, -1, -1):
        if grid[i, column] == 0:
            grid[i, column] = player
            break

    # Check if the player has won
    if check_win(grid, player):
        print("Player {} wins!".format(player))
        break

    # Check if the game is a draw
    if np.all(grid != 0):
        print("Draw!")
        break

    # Switch to the other player
    players = players[1:]

def check_win(grid, player):

    # Check for horizontal win
    for row in range(10):
        if all(grid[row, i] == player for i in range(10)):
            return True

    # Check for vertical win
    for col in range(10):
        if all(grid[i, col] == player for i in range(10)):
            return True

    # Check for diagonal win
    for i in range(10):
        if all(grid[i, i] == player):
            return True
        if all(grid[i, 9-i] == player):
            return True

    # No win yet
    return False
