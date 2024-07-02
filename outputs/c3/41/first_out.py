import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Define the players' symbols
player1_symbol = 1
player2_symbol = -1

# Define the game state
game_over = False
draw = False

# Define the current player
current_player = player1_symbol

# Game loop
while not game_over:
    # Get the player's move
    column = int(input("Player {}'s turn. Choose a column (1-10): ".format(current_player))) - 1

    # Check if the column is valid
    if column < 0 or column > 9:
        print("Invalid column. Please choose a column between 1 and 10.")
        continue

    # Check if the column is full
    if grid[0, column] != 0:
        print("Column is full. Please choose another column.")
        continue

    # Drop the piece into the column
    row = 0
    while grid[row + 1, column] == 0:
        row += 1
    grid[row, column] = current_player

    # Check if the player has won
    if check_win(grid, current_player):
        game_over = True
        print("Player {} wins!".format(current_player))
        break

    # Check if the game is a draw
    if np.all(grid != 0):
        game_over = True
        draw = True
        print("Draw!")
        break

    # Switch the current player
    current_player *= -1

# Print the final grid
print(grid)

# Define the function to check if the player has won
def check_win(grid, player):
    # Check for horizontal wins
    for row in range(10):
        for col in range(7):
            if grid[row, col] == player and grid[row, col + 1] == player and grid[row, col + 2] == player:
                return True

    # Check for vertical wins
    for row in range(7):
        for col in range(10):
            if grid[row, col] == player and grid[row + 1, col] == player and grid[row + 2, col] == player:
                return True

    # Check for diagonal wins
    for row in range(7):
        for col in range(7):
            if grid[row, col] == player and grid[row + 1, col + 1] == player and grid[row + 2, col + 2] == player:
                return True
            if grid[row + 2, col] == player and grid[row + 1, col + 1] == player and grid[row, col + 2] == player:
                return True

    # No win found
    return False
