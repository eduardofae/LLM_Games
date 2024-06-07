import numpy as np

def check_win(grid):
    # Check for horizontal wins
    for row in range(10):
        for col in range(7):
            if grid[row][col] != 0 and grid[row][col] == grid[row][col+1] and grid[row][col] == grid[row][col+2]:
                return grid[row][col]

    # Check for vertical wins
    for row in range(7):
        for col in range(10):
            if grid[row][col] != 0 and grid[row][col] == grid[row+1][col] and grid[row][col] == grid[row+2][col]:
                return grid[row][col]

    # Check for diagonal wins
    for row in range(7):
        for col in range(7):
            if grid[row][col] != 0 and grid[row][col] == grid[row+1][col+1] and grid[row][col] == grid[row+2][col+2]:
                return grid[row][col]
    for row in range(7):
        for col in range(3, 10):
            if grid[row][col] != 0 and grid[row][col] == grid[row+1][col-1] and grid[row][col] == grid[row+2][col-2]:
                return grid[row][col]

    # Check for draw
    if np.count_nonzero(grid) == 100:
        return -1

    # No win or draw
    return 0

def play_pong():
    # Create a 10x10 grid
    grid = np.zeros((10, 10), dtype=int)

    # Set the player turn to 1
    player = 1

    # Game loop
    while True:
        # Display the current grid state
        print(grid)

        # Get the player's move
        try:
            col = int(input(f"Player {player}, choose a column (0-9): "))
        except ValueError:
            print("Invalid column. Please choose a column between 0 and 9.")
            continue

        # Check if the column is valid
        if col < 0 or col > 9:
            print("Invalid column. Please choose a column between 0 and 9.")
            continue

        # Check if the column is full
        if grid[:, col].max() == 0:
            print("That column is full. Please choose another column.")
            continue

        # Place the player's piece in the lowest free space of the column
        row = np.argmax(grid[:, col] == 0)
        grid[row, col] = player

        # Check if the player has won
        winner = check_win(grid)
        if winner != 0:
            if winner == -1:
                print("Draw!")
            else:
                print(f"Player {winner} wins!")
            break

        # Switch the player turn
        player = 3 - player

# Play the game
play_pong()
