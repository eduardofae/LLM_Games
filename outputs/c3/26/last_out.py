import numpy as np
import enum


# Create a 10x10 grid
grid = np.zeros((10, 10))

# Define the players' symbols
player1_symbol = input("Player 1 symbol: ")
player2_symbol = input("Player 2 symbol: ")

# Define the current player
current_player = player1_symbol

# Define the game state
GameState = enum.Enum('GameState', ['ongoing', 'win', 'draw'])
game_state = GameState.ongoing

# Game loop
while game_state == GameState.ongoing:
    try:
        # Get the player's move
        move = int(input(f"{current_player}'s move (1-10): "))

        # Validate the move
        if move < 1 or move > 10 or grid[0][move - 1] != 0:
            raise ValueError("Invalid move. Please enter a valid move (1-10).")

        # Place the player's piece on the grid
        for i in range(9, -1, -1):
            if grid[i][move - 1] == 0:
                grid[i][move - 1] = current_player
                break

        # Check if the player has won
        if check_win(grid, current_player):
            game_state = GameState.win
            print(f"{current_player} wins!")

        # Check if the game is a draw
        elif np.all(grid != 0):
            game_state = GameState.draw
            print("Draw!")

        # Switch the current player
        else:
            current_player = player2_symbol if current_player == player1_symbol else player1_symbol

    except ValueError as e:
        print(e)
        continue

# Print the final grid
print_grid(grid)

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

# Define the function to print the grid
def print_grid(grid):
    # Add a border around the grid
    grid = np.pad(grid, 1, mode='constant', constant_values=0)

    for row in grid:
        for cell in row:
            print(cell if cell != 0 else ' ', end=' ')
        print()
