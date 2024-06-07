import numpy as np

# Create a 3x3 grid
grid = np.zeros((3, 3), dtype=int)

# Define the players
players = [1, 2]

# Define the current player
current_player = players[0]

# Define the winning combinations
winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

# Play the game
while True:
    # Get the player's move
    move = int(input(f"Player {current_player}, enter your move (1-9): ")) - 1

    # Check if the move is valid
    if grid[move // 3, move % 3] != 0:
        print("Invalid move. Please try again.")
        continue

    # Place the player's piece on the grid
    grid[move // 3, move % 3] = current_player

    # Check if the player has won
    for combination in winning_combinations:
        if grid[combination[0] // 3, combination[0] % 3] == grid[combination[1] // 3, combination[1] % 3] == grid[combination[2] // 3, combination[2] % 3] != 0:
            print(f"Player {current_player} wins!")
            break

    # Check if there are no more free spaces
    if np.all(grid != 0):
        print("Draw!")
        break

    # Switch the current player
    current_player = players[(players.index(current_player) + 1) % len(players)]
