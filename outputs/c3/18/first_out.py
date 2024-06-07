import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Define the players
players = ['X', 'O']

# Set the current player to player 1
current_player = 0

# Set the game won to False
game_won = False

# While the game is not won and there are free spaces
while not game_won and np.any(grid == 0):
    
    # Get the column where the player wants to place their piece
    column = int(input(f"Player {players[current_player]}, choose a column (0-9): "))
    
    # Check if the column is valid
    if column < 0 or column > 9 or grid[0][column] != 0:
        print("Invalid column. Please choose again.")
        continue
    
    # Place the player's piece in the lowest free space of the column
    for row in range(9, -1, -1):
        if grid[row][column] == 0:
            grid[row][column] = players[current_player]
            break
    
    # Check if the player has won
    game_won = check_win(grid, players[current_player])
    
    # Switch to the other player
    current_player = (current_player + 1) % 2

# Print the grid
print(grid)

# Print the winner
if game_won:
    print(f"Player {players[current_player]} wins!")
else:
    print("Draw!")

# Define the function to check if a player has won
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
    for row in range(7):
        for col in range(7):
            if np.all(grid[row:row+3, col:col+3] == player) or np.all(grid[row:row+3, col-2:col+1] == player):
                return True
    
    return False
