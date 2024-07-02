import numpy as np

def jdv():
    # Create a 3x3 grid
    grid = np.zeros((3, 3), dtype=int)

    # Set the current player to 1
    current_player = 1

    # Main game loop
    while True:
        # Get the player's move
        move = input(f"Player {current_player}, enter your move (row, column): ")
        row, column = map(int, move.split(","))

        # Check if the move is valid
        if grid[row, column] != 0:
            print("Invalid move. Please try again.")
            continue

        # Place the player's piece on the grid
        grid[row, column] = current_player

        # Check if the player has won
        if check_win(grid, current_player):
            print(f"Player {current_player} wins!")
            break

        # Check if the game is a draw
        if np.all(grid != 0):
            print("Draw!")
            break

        # Switch to the other player
        current_player = 3 - current_player

# Function to check if a player has won
def check_win(grid, player):
    # Check for a win in each row
    for row in range(3):
        if np.all(grid[row, :] == player):
            return True

    # Check for a win in each column
    for column in range(3):
        if np.all(grid[:, column] == player):
            return True

    # Check for a win in each diagonal
    if np.all(np.diag(grid) == player) or np.all(np.diag(np.flip(grid)) == player):
        return True

    # No win found
    return False

# Start the game
jdv()
