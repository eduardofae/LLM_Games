import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Define the players
player1 = 1
player2 = 2

# Define the game loop
while True:
    # Get the player's move
    move = int(input("Player {}'s turn. Enter a column number (1-10): ".format(player1 if player1 == 1 else player2))) - 1

    # Check if the move is valid
    if move < 0 or move > 9 or grid[9, move] != 0:
        print("Invalid move. Please try again.")
        continue

    # Place the player's piece on the grid
    for i in range(9, -1, -1):
        if grid[i, move] == 0:
            grid[i, move] = player1 if player1 == 1 else player2
            break

    # Check if the player has won
    if check_win(grid, player1 if player1 == 1 else player2):
        print("Player {} wins!".format(player1 if player1 == 1 else player2))
        break

    # Check if the game is a draw
    if np.all(grid != 0):
        print("Draw!")
        break

    # Switch players
    player1, player2 = player2, player1

# Define the function to check if a player has won
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
            if i + 2 < 10 and j + 2 < 10 and grid[i, j] == player and grid[i + 1, j + 1] == player and grid[i + 2, j + 2] == player:
                return True
            if i + 2 < 10 and j - 2 >= 0 and grid[i, j] == player and grid[i + 1, j - 1] == player and grid[i + 2, j - 2] == player:
                return True

    # No wins found
    return False
