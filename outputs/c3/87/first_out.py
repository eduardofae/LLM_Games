import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Define the players' symbols
player1_symbol = 1
player2_symbol = 2

# Define the current player
current_player = player1_symbol

# Define the game loop
while True:
    # Get the player's move
    column = int(input("Player {}: Enter a column (1-10): ".format(current_player))) - 1

    # Check if the column is valid
    if column < 0 or column > 9:
        print("Invalid column. Please enter a column between 1 and 10.")
        continue

    # Check if the column is full
    if grid[9, column] != 0:
        print("Column is full. Please choose another column.")
        continue

    # Place the player's piece in the column
    for i in range(9, -1, -1):
        if grid[i, column] == 0:
            grid[i, column] = current_player
            break

    # Check if the player has won
    if check_win(grid, current_player):
        print("Player {} wins!".format(current_player))
        break

    # Switch to the other player
    current_player = player2_symbol if current_player == player1_symbol else player1_symbol

# Check if the game is a draw
if np.all(grid != 0):
    print("The game is a draw.")

# Define the function to check if a player has won
def check_win(grid, player_symbol):
    # Check for a horizontal win
    for i in range(10):
        if np.all(grid[i, :] == player_symbol):
            return True

    # Check for a vertical win
    for j in range(10):
        if np.all(grid[:, j] == player_symbol):
            return True

    # Check for a diagonal win
    for i in range(7):
        for j in range(7):
            if np.all(grid[i:i+3, j:j+3] == player_symbol):
                return True
    
    for i in range(2,10):
        for j in range(7):
            if np.all(grid[i:i-3:-1, j:j+3] == player_symbol):
                return True

    # No win found
    return False
