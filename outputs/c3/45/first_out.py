
import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10))

# Define the players' symbols
player1_symbol = 'X'
player2_symbol = 'O'

# Define the current player
current_player = player1_symbol

# Create a function to check if there is a winner
def check_winner(grid):
  
    # Check for a horizontal win
    for i in range(10):
        for j in range(7):
            if grid[i, j] == grid[i, j + 1] == grid[i, j + 2] != 0:
                return grid[i, j]

    # Check for a vertical win
    for j in range(10):
        for i in range(7):
            if grid[i, j] == grid[i + 1, j] == grid[i + 2, j] != 0:
                return grid[i, j]

    # Check for a diagonal win
    for i in range(7):
        for j in range(7):
            if grid[i, j] == grid[i + 1, j + 1] == grid[i + 2, j + 2] != 0:
                return grid[i, j]
            if grid[i, j] == grid[i + 1, j - 1] == grid[i + 2, j - 2] != 0:
                return grid[i, j]

    # Check for a draw
    if np.all(grid != 0):
        return 'draw'

    # No winner yet
    return None

# Create a function to place a piece
def place_piece(grid, player_symbol, column):
  
    # Find the lowest free space in the column
    for i in range(9, -1, -1):
        if grid[i, column] == 0:
            grid[i, column] = player_symbol
            break

# Main game loop
while True:
  
    # Get the player's input
    column = int(input(f"{current_player}'s turn. Enter a column number (0-9): "))

    # Place the piece
    place_piece(grid, current_player, column)

    # Check for a winner
    winner = check_winner(grid)

    # Print the grid
    print(grid)

    # Check if there is a winner or a draw
    if winner == player1_symbol:
        print("Player 1 wins!")
        break
    elif winner == player2_symbol:
        print("Player 2 wins!")
        break
    elif winner == 'draw':
        print("Draw!")
        break

    # Switch the current player
    if current_player == player1_symbol:
        current_player = player2_symbol
    else:
        current_player = player1_symbol
