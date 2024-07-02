import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Define the players' symbols
player1_symbol = 'X'
player2_symbol = 'O'

# Define the game state
game_over = False
draw = False
winner = None

# Define the current player
current_player = player1_symbol

# Game loop
while not game_over:

    # Get the player's move
    column = int(input("Player {}, enter a column (1-10): ".format(current_player))) - 1

    # Check if the move is valid
    if column < 0 or column > 9 or grid[9, column] != 0:
        print("Invalid move. Please try again.")
        continue

    # Place the player's piece in the grid
    for i in range(9, -1, -1):
        if grid[i, column] == 0:
            grid[i, column] = current_player
            break

    # Check if the player has won
    if check_win(grid, current_player):
        game_over = True
        winner = current_player
    
    # Check if the game is a draw
    elif np.all(grid != 0):
        game_over = True
        draw = True

    # Switch the current player
    if current_player == player1_symbol:
        current_player = player2_symbol
    else:
        current_player = player1_symbol

# Print the game over message
if draw:
    print("The game is a draw.")
else:
    print("Player {} wins!".format(winner))

# Print the final grid
print(grid)

# Function to check if a player has won
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
        if np.all(grid[i:i+3, i:i+3] == player):
            return True
    
    for i in range(3):
        if np.all(grid[i:i+3, 7-i:10-i] == player):
            return True
    
    return False
