import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10))

# Define the players
player1 = 1
player2 = 2

# Define the game over flag
game_over = False

# Define the winner flag
winner = 0

# Define the current player
current_player = player1

# Define the number of moves
num_moves = 0

# Print the grid
print(grid)

# While the game is not over
while not game_over:
    # Get the column number from the current player
    column = int(input("Player {}: Enter a column number (0-9): ".format(current_player)))

    # Check if the column is valid
    if column < 0 or column > 9:
        print("Invalid column number")
        continue

    # Check if the column is full
    if grid[0, column] != 0:
        print("Column is full")
        continue

    # Place the current player's piece in the lowest free space of the column
    for row in range(9, -1, -1):
        if grid[row, column] == 0:
            grid[row, column] = current_player
            break

    # Print the grid
    print(grid)

    # Check if the current player has won
    winner = check_winner(grid, current_player)

    # If the current player has won, set the game over flag to True
    if winner != 0:
        game_over = True

    # Increment the number of moves
    num_moves += 1

    # Switch the current player
    current_player = 3 - current_player

# If the game is over, print the winner
if winner != 0:
    print("Player {} wins!".format(winner))
else:
    print("Draw")

# Function to check if a player has won
def check_winner(grid, player):
    # Check for a horizontal win
    for row in range(10):
        for col in range(7):
            if grid[row, col] == player and grid[row, col+1] == player and grid[row, col+2] == player:
                return player

    # Check for a vertical win
    for row in range(7):
        for col in range(10):
            if grid[row, col] == player and grid[row+1, col] == player and grid[row+2, col] == player:
                return player

    # Check for a diagonal win
    for row in range(7):
        for col in range(7):
            if grid[row, col] == player and grid[row+1, col+1] == player and grid[row+2, col+2] == player:
                return player

    # Check for a reverse diagonal win
    for row in range(7):
        for col in range(2, 10):
            if grid[row, col] == player and grid[row+1, col-1] == player and grid[row+2, col-2] == player:
                return player

    # If no winner, return 0
    return 0
