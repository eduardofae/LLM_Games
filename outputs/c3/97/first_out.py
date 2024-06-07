import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Define the players
player1 = 1
player2 = 2

# Define the game over flag
game_over = False

# Define the winner flag
winner = 0

# Define the current player
current_player = player1

# Game loop
while not game_over:

    # Get the player's move
    print("Player", current_player, "turn:")
    move = input("Enter the column number (1-10): ")

    # Check if the move is valid
    if not move.isdigit() or int(move) < 1 or int(move) > 10 or grid[9, int(move) - 1] != 0:
        print("Invalid move. Please try again.")
        continue

    # Place the player's piece on the grid
    grid[9, int(move) - 1] = current_player

    # Check if the player has won
    if check_win(grid, current_player):
        winner = current_player
        game_over = True

    # Change the current player
    current_player = player1 if current_player == player2 else player2

# Check if the game is a draw
if not game_over:
    if np.all(grid != 0):
        print("Draw!")
        game_over = True

# Print the winner
if winner != 0:
    print("Player", winner, "wins!")


def check_win(grid, player):

    # Check for a horizontal win
    for i in range(10):
        if np.all(grid[i, :] == player):
            return True

    # Check for a vertical win
    for j in range(10):
        if np.all(grid[:, j] == player):
            return True

    # Check for a diagonal win
    for i in range(6):
        for j in range(6):
            if np.all(grid[i:i+3, j:j+3] == player):
                return True
            if np.all(grid[i:i+3, 9-j-2:9-j+1] == player):
                return True

    # No win found
    return False
