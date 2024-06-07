import numpy as np

# Create a 10x10 grid
grid = np.zeros((10,10))

# Create a list of players
players = ['X', 'O']

# Set the current player to the first player
current_player = 0

# Set the game to not over
game_over = False

# While the game is not over
while not game_over:
    # Get the column where the player wants to place their piece
    column = int(input("Player {}: Enter a column (0-9): ".format(players[current_player])))

    # Check if the column is valid
    if column < 0 or column > 9:
        print("Invalid column. Please enter a column between 0 and 9.")
        continue

    # Check if the column is full
    if grid[:,column].max() > 0:
        print("Column {} is full. Please enter a different column.".format(column))
        continue

    # Place the piece in the column
    grid[grid[:,column] == 0, column] = players[current_player]

    # Check if the player has won
    if np.any(np.all(grid == players[current_player], axis=0)) or \
       np.any(np.all(grid == players[current_player], axis=1)) or \
       np.any(np.diagonal(grid) == players[current_player]) or \
       np.any(np.flipud(grid).diagonal() == players[current_player]):
        print("Player {} wins!".format(players[current_player]))
        game_over = True

    # Check if the game is a draw
    if np.all(grid != 0):
        print("Draw!")
        game_over = True

    # Switch to the other player
    current_player = (current_player + 1) % 2

# Print the final grid
print(grid)
