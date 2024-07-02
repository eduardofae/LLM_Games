import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Define the players' pieces
player1_piece = 1
player2_piece = 2

# Define the game state
game_over = False
draw = False

# Define the current player
current_player = player1_piece

# Game loop
while not game_over:

    # Get the player's move
    column = int(input("Player {}: Enter a column (1-10): ".format(current_player))) - 1

    # Check if the column is valid
    if column < 0 or column > 9:
        print("Invalid column")
        continue

    # Check if the column is full
    if grid[9, column] != 0:
        print("Column is full")
        continue

    # Place the player's piece in the column
    for i in range(9, -1, -1):
        if grid[i, column] == 0:
            grid[i, column] = current_player
            break

    # Check if the player has won
    if check_win(grid, current_player):
        print("Player {} wins!".format(current_player))
        game_over = True
        break

    # Check if the game is a draw
    if np.all(grid != 0):
        print("Draw!")
        draw = True
        break

    # Switch the current player
    current_player = player2_piece if current_player == player1_piece else player1_piece

# Print the final grid
print(grid)

# Define the function to check if a player has won
def check_win(grid, player):
    # Check for horizontal wins
    for i in range(10):
        if np.all(grid[i, :] == player):
            return True

    # Check for vertical wins
    for j in range(10):
        if np.all(grid[:, j] == player):
            return True

    # Check for diagonal wins
    for i in range(7):
        for j in range(7):
            if np.all(grid[i:i+3, j:j+3] == player):
                return True

    for i in range(7):
        for j in range(2, 10):
            if np.all(grid[i:i+3, j-2:j+1] == player):
                return True

    return False
