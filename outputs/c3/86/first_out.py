import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Define the players
players = ["Player 1", "Player 2"]

# Define the current player
current_player = 0

# Define the winning lines
winning_lines = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)],
]

# Game loop
while True:
    # Get the player's move
    col = int(input(f"{players[current_player]}'s turn. Choose a column (0-9): "))

    # Check if the move is valid
    if col < 0 or col > 9 or grid[9, col] != 0:
        print("Invalid move. Please choose a different column.")
        continue

    # Place the player's piece
    for i in range(9, -1, -1):
        if grid[i, col] == 0:
            grid[i, col] = current_player + 1
            break

    # Check if the player has won
    if any(all(grid[x, y] == current_player + 1 for x, y in line) for line in winning_lines):
        print(f"{players[current_player]} wins!")
        break

    # Check if the game is a draw
    if np.all(grid != 0):
        print("Draw!")
        break

    # Switch to the other player
    current_player = (current_player + 1) % 2
