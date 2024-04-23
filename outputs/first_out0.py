import numpy as np

# Create a 3x3 grid
grid = np.zeros((3, 3))

# Player 1's turn
player = 1

# Game loop
while True:
    # Get the player's move
    row, col = map(int, input("Player {}'s turn: ".format(player)).split())

    # Check if the move is valid
    if grid[row, col] != 0:
        print("Invalid move. Try again.")
        continue

    # Place the player's piece on the grid
    grid[row, col] = player

    # Check if the player has won
    if check_win(grid, player):
        print("Player {} wins!".format(player))
        break

    # Check if the game is a draw
    if np.all(grid != 0):
        print("Draw!")
        break

    # Switch to the other player
    player = 3 - player

# Check if a player has won
def check_win(grid, player):
    # Check rows
    for i in range(3):
        if np.all(grid[i, :] == player):
            return True

    # Check columns
    for j in range(3):
        if np.all(grid[:, j] == player):
            return True

    # Check diagonals
    if np.all(grid.diagonal() == player) or np.all(np.flip(grid).diagonal() == player):
        return True

    # No winner yet
    return False