import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Define the players
players = ["Player 1", "Player 2"]

# Define the current player
current_player = 0

# Define the scores
scores = [0, 0]

# Define the number of rounds
num_rounds = 3

# Game loop
for round in range(1, num_rounds + 1):
    # Print the round number
    print(f"Round {round}")

    # Print the grid
    print(grid)

    # Game loop for each round
    while True:
        # Get the column where the player wants to place their piece
        while True:
            try:
                column = int(input(f"{players[current_player]}, enter a column (1-10): ")) - 1
                if column < 0 or column > 9:
                    raise ValueError("Invalid column")
                break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 10.")

        # Check if the column is full
        if grid[0, column] != 0:
            print("Column is full")
            continue

        # Place the player's piece in the lowest free space of the column
        for row in range(9, -1, -1):
            if grid[row, column] == 0:
                grid[row, column] = current_player + 1
                break

        # Check if the player has won
        if check_win(grid, current_player + 1):
            print(f"{players[current_player]} wins round {round}!")
            scores[current_player] += 1
            break

        # Check if the game is a draw
        if np.all(grid != 0):
            print("Draw!")
            break

        # Switch to the other player
        current_player = (current_player + 1) % 2

    # Reset the grid for the next round
    grid = np.zeros((10, 10), dtype=int)

# Print the final scores
print(f"Final scores: {players[0]}: {scores[0]}, {players[1]}: {scores[1]}")

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
