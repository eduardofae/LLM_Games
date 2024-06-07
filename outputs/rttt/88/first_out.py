import numpy as np

# Create a 3x3 grid
grid = np.zeros((3, 3), dtype=int)

# Define the players' symbols
player1 = 'X'
player2 = 'O'

# Keep track of the current player
current_player = player1

# Main game loop
while True:
    # Print the grid
    print(grid)

    # Get the player's move
    row, col = map(int, input("Enter your move (row, column): ").split())

    # Check if the move is valid
    if grid[row, col] != 0:
        print("Invalid move. Please try again.")
        continue

    # Place the player's piece on the grid
    grid[row, col] = current_player

    # Check if the game is over
    if check_win(grid, current_player):
        print(f"{current_player} wins!")
        break
    elif np.all(grid != 0):
        print("Tie!")
        break

    # Switch to the other player
    current_player = player1 if current_player == player2 else player2

# Define the function to check if a player has won
def check_win(grid, player):
    # Check rows
    for row in range(3):
        if np.all(grid[row, :] == player):
            return True

    # Check columns
    for col in range(3):
        if np.all(grid[:, col] == player):
            return True

    # Check diagonals
    if np.all(grid.diagonal() == player) or np.all(np.flip(grid).diagonal() == player):
        return True

    # No win yet
    return False
