import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Define the players
players = ["Player 1", "Player 2"]

# Define the game loop
while True:
    # Get the current player
    player = players[0]

    # Get the player's move
    move = int(input(f"{player}'s move (column): "))

    # Check if the move is valid
    if move < 1 or move > 10 or grid[9, move - 1] != 0:
        print("Invalid move. Try again.")
        continue

    # Place the player's piece
    for i in range(9, -1, -1):
        if grid[i, move - 1] == 0:
            grid[i, move - 1] = 1 if player == "Player 1" else 2
            break

    # Check if the player has won
    if check_win(grid, player):
        print(f"{player} wins!")
        break

    # Check if the game is a draw
    if np.all(grid != 0):
        print("Draw!")
        break

    # Switch players
    players = players[1:]

# Define the function to check if a player has won
def check_win(grid, player):
    # Check for horizontal wins
    for i in range(10):
        if np.all(grid[i] == player):
            return True

    # Check for vertical wins
    for j in range(10):
        if np.all(grid[:, j] == player):
            return True

    # Check for diagonal wins
    for i in range(7):
        if np.all(np.diag(grid[i:i+3, i:i+3]) == player):
            return True
        if np.all(np.diag(grid[i:i+3, 9-i:6-i]) == player):
            return True

    return False
