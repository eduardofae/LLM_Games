
import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Define the players
players = [1, -1]

# Define the game loop
while True:
    # Get the current player
    player = players[0]

    # Get the player's move
    move = input("Player {} choose a column: ".format(player))

    # Check if the move is valid
    if not (0 <= move < 10 and grid[9, move] == 0):
        print("Invalid move. Please try again.")
        continue

    # Drop the player's piece
    for i in range(9, -1, -1):
        if grid[i, move] == 0:
            grid[i, move] = player
            break

    # Check if the player has won
    if check_win(grid, player):
        print("Player {} wins!".format(player))
        break

    # Switch to the other player
    players = players[1:]

# Check if the game is a draw
if np.all(grid != 0):
    print("Draw!")

# Function to check if there is a winner
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
            if grid[i, j] == player and (grid[i+1, j+1] == player and grid[i+2, j+2] == player) or (grid[i+1, j-1] == player and grid[i+2, j-2] == player):
                return True

    # No winner yet
    return False
