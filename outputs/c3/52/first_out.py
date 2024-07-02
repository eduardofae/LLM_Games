
import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Create a list of players
players = [1, 2]

# Create a variable to keep track of the current player
current_player = 0

# Create a variable to keep track of the winner
winner = None

# Create a variable to keep track of the number of moves
num_moves = 0

# Game loop
while winner is None and num_moves < 100:
    # Get the column where the player wants to place their piece
    column = input("Player {} choose a column (0-9): ".format(players[current_player]))

    # Check if the column is valid
    if not (0 <= column < 10):
        print("Invalid column. Please choose a column between 0 and 9.")
        continue

    # Check if the column is full
    if grid[:, column].max() == 2:
        print("Column {} is full. Please choose another column.".format(column))
        continue

    # Place the player's piece in the lowest free space of the column
    row = np.where(grid[:, column] == 0)[0][-1]
    grid[row, column] = players[current_player]

    # Check if the player has won
    if check_win(grid, players[current_player]):
        winner = players[current_player]
        break

    # Switch to the other player
    current_player = (current_player + 1) % 2

    # Increment the number of moves
    num_moves += 1

# Print the winner
if winner is not None:
    print("Player {} wins!".format(winner))
else:
    print("Draw!")

# Print the grid
print(grid)

# Function to check if a player has won
def check_win(grid, player):
    # Check for a horizontal win
    for row in range(10):
        if np.all(grid[row, :] == player):
            return True

    # Check for a vertical win
    for col in range(10):
        if np.all(grid[:, col] == player):
            return True

    # Check for a diagonal win
    for i in range(-9, 10):
        # Check the main diagonal
        if np.all(grid.diagonal(i) == player):
            return True

        # Check the anti-diagonal
        if np.all(np.flipud(grid).diagonal(i) == player):
            return True

    # No win
    return False
