import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Define the players' turn
player_turn = 1

# Game loop
while True:
    # Get the player's input
    column = int(input("Player {}: Enter the column (1-10): ".format(player_turn))) - 1

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
            grid[row, column] = player_turn
            break

    # Check if the player has won
    if check_win(grid, player_turn):
        print("Player {} wins!".format(player_turn))
        break

    # Check if the game is a draw
    if np.all(grid != 0):
        print("Draw!")
        break

    # Switch the player's turn
    player_turn = 3 - player_turn

# Check if there is a line of 3 adjacent pieces
def check_win(grid, player):
    # Check rows
    for row in range(10):
        if np.all(grid[row, :3] == player) or np.all(grid[row, 3:6] == player) or np.all(grid[row, 6:9] == player):
            return True

    # Check columns
    for col in range(10):
        if np.all(grid[:3, col] == player) or np.all(grid[3:6, col] == player) or np.all(grid[6:9, col] == player):
            return True

    # Check diagonals
    for i in range(8):
        if np.all(grid[i:i+3, i:i+3] == player) or np.all(grid[i:i+3, 9-i-2:9-i+1] == player):
            return True

    return False
