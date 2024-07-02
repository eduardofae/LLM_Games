
import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10))

# Define the players' symbols
player1_symbol = 'X'
player2_symbol = 'O'

# Define the current player
current_player = player1_symbol

# Define the game state
game_state = 'ongoing'

# Game loop
while game_state == 'ongoing':
    # Get the player's move
    move = int(input(f"{current_player}'s move: "))

    # Check if the move is valid
    if move < 1 or move > 10 or grid[0][move - 1] != 0:
        print("Invalid move. Please try again.")
        continue

    # Place the player's piece on the grid
    for i in range(9, -1, -1):
        if grid[i][move - 1] == 0:
            grid[i][move - 1] = current_player
            break

    # Check if the player has won
    if check_win(grid, current_player):
        game_state = 'win'
        print(f"{current_player} wins!")
    # Check if the game is a draw
    elif np.all(grid != 0):
        game_state = 'draw'
        print("Draw!")
    # Switch the current player
    else:
        current_player = player2_symbol if current_player == player1_symbol else player1_symbol

# Print the final grid
print(grid)

# Define the function to check if a player has won
def check_win(grid, player):
    # Check for a horizontal win
    for i in range(10):
        if np.all(grid[i] == player):
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
            if i - 3 >= 0 and j + 3 < 10 and np.all(grid[i-3:i, j:j+3] == player):
                return True

    # No win
    return False
