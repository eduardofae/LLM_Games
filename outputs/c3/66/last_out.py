import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Create a list of player turns
player_turns = [1, 2]

# Create a flag to check if the game is over
game_over = False

# Create a counter to keep track of the number of moves made
move_count = 0

# Define a function to check if a player has made a line of 3
def check_win(grid, player):
    
    # Check for horizontal lines
    for row in range(10):
        if np.all(grid[row, :] == player):
            return True
    
    # Check for vertical lines
    for column in range(10):
        if np.all(grid[:, column] == player):
            return True
    
    # Check for diagonal lines
    for i in range(10):
        if np.all(np.diagonal(grid, i) == player):
            return True
        if np.all(np.diagonal(np.flip(grid, axis=0), i) == player):
            return True
    
    # No lines of 3 found
    return False

# Main game loop
while not game_over:
    
    # Get the current player's turn
    player_turn = player_turns[move_count % 2]
    
    # Get the player's input
    while True:
        try:
            column = int(input("Player {}: Enter a column (1-10): ".format(player_turn))) - 1
            if column < 0 or column > 9:
                raise ValueError("Invalid column")
            break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 10.")
    
    # Check if the column is full
    if grid[0, column] != 0:
        print("Column is full")
        continue
    
    # Place the player's piece in the lowest free space of the column
    for row in range(9, -1, -1):
        if grid[row, column] == 0:
            grid[row, column] = player_turn
            break
    
    # Check if the player has made a line of 3
    if check_win(grid, player_turn):
        print("Player {} wins!".format(player_turn))
        game_over = True
    
    # Increment the move count
    move_count += 1
    
    # Check if the game is a draw
    if move_count == 100:
        print("Draw")
        game_over = True

# Print the final grid
print(grid)
