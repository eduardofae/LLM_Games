import numpy as np

# Create a 3x3 grid
grid = np.zeros((3, 3))

# Define the players
players = ['X', 'O']

# Define the winner
winner = None

# Create a function to check if there is a winner
def check_winner():
    for i in range(3):
        # Check rows
        if np.all(grid[i] == grid[i][0]) and grid[i][0] != 0:
            return grid[i][0]
        # Check columns
        if np.all(grid[:, i] == grid[0, i]) and grid[0, i] != 0:
            return grid[0, i]
    # Check diagonals
    if np.all(grid.diagonal() == grid[0, 0]) and grid[0, 0] != 0:
        return grid[0, 0]
    if np.all(np.flip(grid).diagonal() == grid[0, 2]) and grid[0, 2] != 0:
        return grid[0, 2]
    return None

# Create a function to play the game
def play_game():
    global winner

    # Loop until there is a winner or no more free spaces
    while winner is None and np.count_nonzero(grid) < 9:
        # Get the current player's move
        player = players[np.count_nonzero(grid) % 2]
        row, col = map(int, input(f"{player}'s turn: ").split())

        # Check if the move is valid
        if grid[row, col] == 0:
            # Place the player's piece in the grid
            grid[row, col] = player
        else:
            print("Invalid move")

        # Check if there is a winner
        winner = check_winner()

    # Print the result
    if winner is not None:
        print(f"{winner} wins!")
    else:
        print("Draw")

# Play the game
play_game()
