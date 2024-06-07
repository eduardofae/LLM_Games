import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10))

# Define the player's turns
player1 = True
player2 = False

# Define the winning conditions
winning_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

# Game loop
while True:
    # Print the grid
    print(grid)

    # Get the player's move
    if player1:
        column = int(input("Player 1, choose a column (0-9): "))
    else:
        column = int(input("Player 2, choose a column (0-9): "))

    # Check if the column is valid
    if column < 0 or column > 9:
        print("Invalid column. Please choose a column between 0 and 9.")
        continue

    # Check if the column is full
    if grid[9, column] != 0:
        print("Column is full. Please choose another column.")
        continue

    # Place the player's piece in the column
    for i in range(9, -1, -1):
        if grid[i, column] == 0:
            grid[i, column] = 1 if player1 else 2
            break

    # Check if the player has won
    for condition in winning_conditions:
        if grid[condition[0], condition[1]] == grid[condition[1], condition[2]] and grid[condition[1], condition[2]] == grid[condition[2], condition[0]] and grid[condition[2], condition[0]] != 0:
            print("Player", ("1" if player1 else "2"), "wins!")
            break

    # Check if the game is a draw
    if np.all(grid != 0):
        print("Draw!")
        break

    # Switch the player's turns
    player1 = not player1
    player2 = not player2
