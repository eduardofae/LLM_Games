import numpy as np
import ascii_graph

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
    try:
        column = int(input("Player {}: Enter a column (1-10): ".format(current_player))) - 1
    except ValueError:
        print("Invalid input. Please enter an integer between 1 and 10.")
        continue

    # Check if the column is valid
    if column < 0 or column > 9:
        print("Invalid column. Please enter a number between 1 and 10.")
        continue

    # Check if the column is full
    if grid[9, column] != 0:
        print("Column is full. Please choose a different column.")
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
print(ascii_graph.graph_from_numpy_array(grid))

# Define the function to check if a player has won
def check_win(grid, player):
    """
    Checks if a player has won the game.

    Args:
        grid (numpy.ndarray): The game grid.
        player (int): The player to check for a win.

    Returns:
        bool: True if the player has won, False otherwise.
    """

    # Check for wins in any direction (horizontal, vertical, or diagonal)
    window_size = 3
    for i in range(grid.shape[0] - window_size + 1):
        for j in range(grid.shape[1] - window_size + 1):
            window = grid[i:i+window_size, j:j+window_size]
            if np.all(window == player):
                return True

    return False

# Function to handle grids of any size
def check_win_generalized(grid, player, window_size):
    """
    Checks if a player has won the game on a grid of any size.

    Args:
        grid (numpy.ndarray): The game grid.
        player (int): The player to check for a win.
        window_size (int): The size of the winning window.

    Returns:
        bool: True if the player has won, False otherwise.
    """

    for i in range(grid.shape[0] - window_size + 1):
        for j in range(grid.shape[1] - window_size + 1):
            window = grid[i:i+window_size, j:j+window_size]
            if np.all(window == player):
                return True

    return False
