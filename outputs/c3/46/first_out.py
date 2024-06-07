import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Define the players
players = [1, 2]

# Define the game state
game_over = False
draw = False

# Start the game
while not game_over:
    # Get the current player
    player = players[0]

    # Get the player's move
    col = int(input("Player {}'s turn. Choose a column (0-9): ".format(player)))

    # Check if the move is valid
    if col < 0 or col > 9 or grid[0][col] != 0:
        print("Invalid move. Please choose a different column.")
        continue

    # Place the player's piece in the grid
    for i in range(9, -1, -1):
        if grid[i][col] == 0:
            grid[i][col] = player
            break

    # Check if the player has won
    if check_win(grid, player):
        print("Player {} wins!".format(player))
        game_over = True
        break

    # Check if the game is a draw
    if np.all(grid != 0):
        print("It's a draw!")
        draw = True
        game_over = True
        break

    # Switch to the other player
    players.reverse()

# Print the final grid
print(grid)

# Print the game state
if draw:
    print("It's a draw!")
else:
    print("Player {} wins!".format(player))

# Define the function to check if a player has won
def check_win(grid, player):
    # Check for a horizontal win
    for i in range(10):
        if np.all(grid[i, :] == player):
            return True

    # Check for a vertical win
    for j in range(10):
        if np.all(grid[:, j] == player):
            return True

    # Check for a diagonal win
    for i in range(10):
        for j in range(10):
            if i + 3 < 10 and j + 3 < 10 and np.all(grid[i:i+3, j:j+3] == player):
                return True
            if i + 3 < 10 and j - 3 >= 0 and np.all(grid[i:i+3, j:j-3:-1] == player):
                return True

    # No win found
    return False
