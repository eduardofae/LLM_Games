import numpy as np

# Create a 7x6 grid
grid = np.zeros((7, 6), dtype=int)

# Define the players
players = [1, 2]

# Define the current player
current_player = 0

# Define the game loop
while True:
    # Get the column where the player wants to place their piece
    try:
        column = int(input("Player {}: Enter a column (1-6): ".format(players[current_player]))) - 1
    except ValueError:
        print("Invalid column. Please enter a number between 1 and 6.")
        continue

    # Check if the column is valid
    if column < 0 or column > 5:
        print("Invalid column. Please enter a number between 1 and 6.")
        continue

    # Check if the column is full
    if grid[0, column] != 0:
        print("Column {} is full. Please choose another column.".format(column + 1))
        continue

    # Place the player's piece in the column
    for i in range(6, -1, -1):
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
    for i in range(7):
        if np.all(grid[i] == player):
            return True

    # Check for vertical wins
    for j in range(6):
        if np.all(grid[:, j] == player):
            return True

    # Check for diagonal wins
    for i in range(7):
        for j in range(6):
            if grid[i, j] == player and grid[i+1, j+1] == player and grid[i+2, j+2] == player:
                return True
            if grid[i, j] == player and grid[i+1, j-1] == player and grid[i+2, j-2] == player:
                return True
    return False

# Add a game over state
if check_win(grid, players[current_player]) or np.all(grid != 0):
    print("Game over.")
