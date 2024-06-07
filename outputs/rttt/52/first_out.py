import numpy as np

# Create a 3x3 grid
grid = np.zeros((3, 3), dtype=int)

# Define the players
players = ["X", "O"]

# Define the current player
currentPlayer = 0

# Define the game state
gameState = "playing"

# Main game loop
while gameState == "playing":
    # Get the current player's move
    print(f"Player {players[currentPlayer]}'s turn")
    row = int(input("Enter the row (0-2): "))
    col = int(input("Enter the column (0-2): "))

    # Check if the move is valid
    if grid[row, col] != 0:
        print("Invalid move. Please try again.")
        continue

    # Place the current player's piece on the grid
    grid[row, col] = players[currentPlayer]

    # Check if the current player has won
    if np.any(np.all(grid == players[currentPlayer], axis=0)) or \
       np.any(np.all(grid == players[currentPlayer], axis=1)) or \
       np.all(grid.diagonal() == players[currentPlayer]) or \
       np.all(np.flip(grid).diagonal() == players[currentPlayer]):
        print(f"Player {players[currentPlayer]} wins!")
        gameState = "finished"

    # Check if the game is a draw
    if np.all(grid != 0):
        print("Draw!")
        gameState = "finished"

    # Switch to the other player
    currentPlayer = (currentPlayer + 1) % len(players)
