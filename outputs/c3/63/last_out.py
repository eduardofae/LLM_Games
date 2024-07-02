import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10))

# Define the players
players = [1, 2]

# Define the current player
current_player = 0

# Define the game loop
while True:
    # Get the player's move
    try:
        column = int(input("Player {}: Enter a column number (1-10): ".format(players[current_player]))) - 1
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 10.")
        continue

    # Check if the move is valid
    if column < 0 or column > 9 or grid[9, column] != 0:
        print("Invalid move. Please try again.")
        continue

    # Drop the player's piece into the grid
    for i in range(9, -1, -1):
        if grid[i, column] == 0:
            grid[i, column] = players[current_player]
            break

    # Check if the player has won
    if np.any(check_win(grid, players[current_player])):
        print("Player {} wins!".format(players[current_player]))
        break

    # Check if the game is a draw
    if np.all(grid != 0):
        print("Draw!")
        break

    # Switch to the other player
    current_player = (current_player + 1) % 2

# Define the function to check for a win
def check_win(grid, player):
    # Check for a horizontal win
    for i in range(10):
        if np.all(grid[i, :7] == player):
            return True

    # Check for a vertical win
    for j in range(10):
        if np.all(grid[:, j] == player):
            return True

    # Check for a diagonal win
    for i in range(7):
        if np.all(grid[i:i+3, i:i+3] == player):
            return True

    for i in range(7):
        if np.all(grid[i:i+3, 9-i:6-i] == player):
            return True

    # No win found
    return False
