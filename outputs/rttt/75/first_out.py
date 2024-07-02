import numpy as np

# Create a 3x3 grid
grid = np.zeros((3, 3), dtype=np.int8)

# Define the players
player1 = 1
player2 = -1

# Define the game state
game_over = False
winner = None

# Define the current player
current_player = player1

# Define the number of turns
num_turns = 0

# Execute the game loop
while not game_over:
    
    # Print the grid
    print(grid)
    
    # Get the player's move
    row, col = map(int, input("Player {}'s turn: ".format(current_player)).split())
    
    # Check if the move is valid
    if grid[row, col] != 0:
        print("Invalid move")
        continue
    
    # Place the player's piece on the grid
    grid[row, col] = current_player

    # Increment the number of turns
    num_turns += 1
    
    # Check if the player has won
    winner = check_winner(grid)
    
    # Check if the game is over
    if winner is not None or num_turns == 9:
        game_over = True
    
    # Switch the current player
    current_player *= -1

# Print the winner
if winner is None:
    print("Draw")
else:
    print("Player {} wins".format(winner))

# Define the function to check if a player has won
def check_winner(grid):
    
    # Check for a winner horizontally
    for row in grid:
        if np.all(row == row[0]) and row[0] != 0:
            return row[0]
    
    # Check for a winner vertically
    for col in grid.T:
        if np.all(col == col[0]) and col[0] != 0:
            return col[0]
    
    # Check for a winner diagonally
    if np.all(np.diagonal(grid) == np.diagonal(grid)[0]) and np.diagonal(grid)[0] != 0:
        return np.diagonal(grid)[0]
    if np.all(np.diagonal(np.flip(grid)) == np.diagonal(np.flip(grid))[0]) and np.diagonal(np.flip(grid))[0] != 0:
        return np.diagonal(np.flip(grid))[0]
    
    # No winner yet
    return None
