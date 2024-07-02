
import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Define the players' symbols
player1_symbol = 'X'
player2_symbol = 'O'

# Define the current player
current_player = 1

# Define the winning combinations
winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

# Main game loop
while True:
    # Print the grid
    print(grid)

    # Get the player's input
    column = int(input("Player {}'s turn. Choose a column (1-10): ".format(current_player))) - 1

    # Check if the column is valid
    if column < 0 or column > 9:
        print("Invalid column. Please choose a column between 1 and 10.")
        continue

    # Check if the column is full
    if grid[0, column] != 0:
        print("Column is full. Please choose another column.")
        continue

    # Place the player's piece in the lowest free space of the column
    for row in range(9, -1, -1):
        if grid[row, column] == 0:
            grid[row, column] = current_player
            break

    # Check if the player has won
    for combination in winning_combinations:
        if grid[combination[0], combination[1]] == grid[combination[1], combination[2]] == grid[combination[2], combination[3]] != 0:
            print("Player {} wins!".format(current_player))
            break

    # Check if there are no more free spaces
    if np.all(grid != 0):
        print("Draw!")
        break

    # Switch to the other player
    current_player = 3 - current_player
