import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Define the players
players = [1, 2]

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

# Main game loop
while True:
    # Get the current player
    player = players[0]

    # Get the player's move
    while True:
        try:
            row = int(input(f"Player {player}, choose a row (0-9): "))
            column = int(input(f"Player {player}, choose a column (0-9): "))
        except ValueError:
            print("Invalid move")
        else:
            break

    # Check if the move is valid
    if row < 0 or row > 9 or column < 0 or column > 9:
        print("Invalid move")
        continue

    # Check if the space is empty
    if grid[row, column] != 0:
        print("Space is already occupied")
        continue

    # Check if the column is full
    if grid[:, column].max() == 2:
        print("Column is full")
        continue

    # Place the player's piece in the space
    grid[row, column] = player

    # Check if the player has won
    for line in winning_lines:
        if grid[line[0], line[1]] == grid[line[1], line[2]] == grid[line[0], line[2]]:
            if grid[line[0], line[1]] == 0:
                print("Draw")
            else:
                print(f"Player {player} wins!")
            break

    # Check if the game is a draw
    if np.all(grid != 0):
        print("Draw")
        break

    # Switch players
    players.reverse()

    # Print the grid
    print(grid)
