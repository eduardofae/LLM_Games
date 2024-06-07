import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Define the players
players = [1, 2]

# Define the current player
current_player = 0

# Game loop
while True:
    # Get the column where the player wants to place their piece
    column = int(input(f"Player {players[current_player]}, enter a column (1-10): ")) - 1

    # Check if the column is valid
    if column < 0 or column > 9:
        print("Invalid column")
        continue

    # Check if the column is full
    if grid[0, column] != 0:
        print("Column is full")
        continue

    # Place the player's piece in the lowest free space of the column
    for row in range(9, -1, -1):
        if grid[row, column] == 0:
            grid[row, column] = players[current_player]
            break

    # Check if the player has won
    if check_win(grid, players[current_player]):
        print(f"Player {players[current_player]} wins!")
        break

    # Check if the game is a draw
    if np.all(grid != 0):
        print("Draw!")
        break

    # Switch to the other player
    current_player = (current_player + 1) % 2

# Define the check_win function
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
        # Check for diagonal wins from top left to bottom right
        if np.all(np.diagonal(grid[i:, :10-i], offset=i) == player):
            return True

        # Check for diagonal wins from bottom left to top right
        if np.all(np.diagonal(np.flipud(grid[:10-i, i:]), offset=-i) == player):
            return True

    # No win found
    return False
