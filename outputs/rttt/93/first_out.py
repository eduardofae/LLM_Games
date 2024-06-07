import numpy as np

# Create a 3x3 grid
grid = np.zeros((3, 3))

# Define the players
player1 = 'X'
player2 = 'O'

# Define the current player
current_player = player1

# Game loop
while True:
    # Get the player's move
    row, col = map(int, input("Enter row and column: ").split())

    # Check if the move is valid
    if grid[row, col] != 0:
        print("Invalid move")
        continue

    # Place the player's piece on the grid
    grid[row, col] = current_player

    # Check if the player has won
    if (grid[row, 0] == grid[row, 1] == grid[row, 2] != 0 or
            grid[0, col] == grid[1, col] == grid[2, col] != 0 or
            grid[0, 0] == grid[1, 1] == grid[2, 2] != 0 or
            grid[0, 2] == grid[1, 1] == grid[2, 0] != 0):
        print(f"{current_player} wins!")
        break

    # Check if the game is a draw
    if np.all(grid != 0):
        print("Draw!")
        break

    # Switch the current player
    current_player = player2 if current_player == player1 else player1
