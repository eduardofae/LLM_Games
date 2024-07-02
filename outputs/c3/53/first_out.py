import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Define the players' symbols
player1_symbol = 'X'
player2_symbol = 'O'

# Define the game state
game_over = False
draw = False

# Define the current player
current_player = player1_symbol

# Game loop
while not game_over:
    # Get the player's move
    column = int(input(f"Player {current_player}, choose a column (1-10): ")) - 1

    # Check if the column is valid
    if column < 0 or column > 9:
        print("Invalid column. Please choose a column between 1 and 10.")
        continue

    # Check if the column is full
    if grid[9, column] != 0:
        print("Column is full. Please choose another column.")
        continue

    # Place the player's piece in the lowest free space of the column
    for row in range(9, -1, -1):
        if grid[row, column] == 0:
            grid[row, column] = current_player
            break

    # Check if the player has won
    if check_win(grid, current_player):
        print(f"Player {current_player} wins!")
        game_over = True
    elif check_draw(grid):
        print("Draw!")
        game_over = True
    else:
        # Switch to the other player
        current_player = player2_symbol if current_player == player1_symbol else player1_symbol

# Print the final grid
print(grid)

# Define the function to check if a player has won
def check_win(grid, player):
    # Check for horizontal wins
    for row in range(10):
        if all(grid[row, i] == player for i in range(3)):
            return True

    # Check for vertical wins
    for column in range(10):
        if all(grid[i, column] == player for i in range(3)):
            return True

    # Check for diagonal wins
    for row in range(8):
        for column in range(8):
            if all(grid[row+i, column+i] == player for i in range(3)):
                return True

    for row in range(8):
        for column in range(2, 10):
            if all(grid[row+i, column-i] == player for i in range(3)):
                return True

    return False

# Define the function to check if the game is a draw
def check_draw(grid):
    return all(grid[9, column] != 0 for column in range(10))
