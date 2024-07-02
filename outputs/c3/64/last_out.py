import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Create a list of players
players = [1, 2]

# Create a loop to take turns
while True:
    # Get the current player
    player = players[0]

    # Get the column where the player wants to place their piece
    while True:
        try:
            column = int(input(f"Player {player}, choose a column (1-10): "))
        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 10.")
            continue
        if column < 1 or column > 10:
            print("Invalid column. Please choose a column between 1 and 10.")
            continue
        break

    # Check if the column is full
    if grid[:, column-1].max() == 2:
        print("Column is full. Please choose another column.")
        continue

    # Find the lowest free space in the column
    row = np.where(grid[:, column-1] == 0)[0][-1]

    # Place the player's piece in the grid
    grid[row, column-1] = player

    # Print the grid
    print(grid)

    # Check if the player has won
    if check_win(grid, player):
        print(f"Player {player} wins!")
        break

    # Check if the game is a draw
    if grid.max() == 2:
        print("Draw!")
        break

    # Switch players
    players = players[1:] + players[:1]


# Check if the player has won
def check_win(grid, player):
    # Check for horizontal wins
    for row in range(10):
        if np.all(grid[row, :] == player):
            return True

    # Check for vertical wins
    for col in range(10):
        if np.all(grid[:, col] == player):
            return True

    # Check for diagonal wins
    for i in range(10):
        # Check for diagonal wins from top left to bottom right
        if np.all(np.diagonal(grid[i:, :i+1]) == player):
            return True

        # Check for diagonal wins from bottom left to top right
        if np.all(np.diagonal(np.flipud(grid[i:, :i+1]))) == player:
            return True

    # No wins found
    return False
