
import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Define the players
players = [1, 2]

# Game loop
while True:
    # Get the current player
    player = players[0]

    # Get the player's input
    column = int(input(f"Player {player}, choose a column (1-10): ")) - 1

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
            grid[i, column] = player
            break

    # Check if the player has won
    if check_win(grid, player):
        print(f"Player {player} wins!")
        break

    # Check if the game is a draw
    if np.all(grid != 0):
        print("Draw!")
        break

    # Switch players
    players.reverse()

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
    for i in range(10):
        for j in range(10):
            if grid[i, j] == player:
                # Check for a diagonal win in the northeast direction
                if i + 2 < 10 and j + 2 < 10 and grid[i+1, j+1] == player and grid[i+2, j+2] == player:
                    return True

                # Check for a diagonal win in the northwest direction
                if i - 2 >= 0 and j + 2 < 10 and grid[i-1, j+1] == player and grid[i-2, j+2] == player:
                    return True

                # Check for a diagonal win in the southeast direction
                if i + 2 < 10 and j - 2 >= 0 and grid[i+1, j-1] == player and grid[i+2, j-2] == player:
                    return True

                # Check for a diagonal win in the southwest direction
                if i - 2 >= 0 and j - 2 >= 0 and grid[i-1, j-1] == player and grid[i-2, j-2] == player:
                    return True

    # No win found
    return False
