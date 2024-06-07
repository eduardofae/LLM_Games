import numpy as np
from enum import Enum

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Define the players' symbols
player1_symbol = 'X'
player2_symbol = 'O'

# Define the game state
GameState = Enum('GameState', ['ongoing', 'win', 'draw'])
game_state = GameState.ongoing

# Define the current player
current_player = 1

# Get the players' names
player1_name = input("Enter player 1's name: ")
player2_name = input("Enter player 2's name: ")

# Start the game loop
while game_state == GameState.ongoing:
    # Get the current player's move
    if current_player == 1:
        player_name = player1_name
    else:
        player_name = player2_name

    player_move = input(f"{player_name}'s turn. Enter the column number (1-10): ")
    player_move = int(player_move) - 1

    # Validate the player's move
    if player_move < 0 or player_move > 9 or grid[9, player_move] != 0:
        print("Invalid move. Please enter a valid column number.")
        continue

    # Place the player's piece on the grid
    grid[9, player_move] = current_player

    # Check if there is a winner
    game_state = check_winner(grid)

    # Switch to the other player
    current_player = 3 - current_player

# Print the final grid
print_grid(grid)

# Print the winner
if game_state == GameState.draw:
    print("Draw!")
else:
    if current_player == 1:
        print(f"{player1_name} wins!")
    else:
        print(f"{player2_name} wins!")

# Check if there is a winner
def check_winner(grid):
    # Check for a horizontal win
    for row in range(10):
        if all(grid[row, col] == grid[row, col + 1] for col in range(7)):
            return GameState.win

    # Check for a vertical win
    for col in range(10):
        if all(grid[row, col] == grid[row + 1, col] for row in range(7)):
            return GameState.win

    # Check for a diagonal win
    for row in range(7):
        for col in range(7):
            if all(grid[row + i, col + i] == grid[row + i + 1, col + i + 1] for i in range(3)):
                return GameState.win

            if all(grid[row + i, col - i] == grid[row + i + 1, col - i - 1] for i in range(3)):
                return GameState.win

    # Check for a draw
    if all(grid[row, col] != 0 for row in range(10) for col in range(10)):
        return GameState.draw

    # No winner yet
    return GameState.ongoing

# Print the grid
def print_grid(grid):
    for row in range(10):
        for col in range(10):
            if grid[row, col] == 0:
                print(' ', end=' ')
            elif grid[row, col] == 1:
                print(player1_symbol, end=' ')
            else:
                print(player2_symbol, end=' ')
        print()

# TODO: Implement game history tracking and graphical user interface
