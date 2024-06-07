import numpy as np

# Create a 3x3 grid
grid = np.zeros((3, 3))

# Define the players
player1 = 'X'
player2 = 'O'

# Define the current player
current_player = player1

# Game loop
while True:
    # Get the player's move
    row, col = map(int, input("Enter your move (row, col): ").split())

    # Check if the move is valid
    if grid[row, col] != 0:
        print("Invalid move.")
        continue

    # Place the player's piece on the grid
    grid[row, col] = current_player

    # Check if the player has won
    if check_win(grid, current_player):
        print(f"{current_player} wins!")
        break

    # Check if the game is a draw
    if np.all(grid != 0):
        print("Draw!")
        break

    # Switch the current player
    current_player = player2 if current_player == player1 else player1

# Function to check if the player has won
def check_win(grid, player):
    # Check the rows
    for row in grid:
        if np.all(row == player):
            return True

    # Check the columns
    for col in grid.T:
        if np.all(col == player):
            return True

    # Check the diagonals
    if np.all(grid.diagonal() == player) or np.all(np.flip(grid).diagonal() == player):
        return True

    # Otherwise, the player has not won
    return False
