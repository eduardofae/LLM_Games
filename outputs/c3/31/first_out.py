import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Define the players' symbols
player1_symbol = 1
player2_symbol = 2

# Define the game state
game_state = "ongoing"

# Get the players' names
player1_name = input("Player 1 name: ")
player2_name = input("Player 2 name: ")

# Start the game loop
while game_state == "ongoing":
    # Get the player's move
    player = player1_symbol if game_state == "ongoing" else player2_symbol
    column = int(input(f"{player1_name if player == player1_symbol else player2_name}'s turn. Enter a column number (1-10): ")) - 1

    # Check if the column is valid
    if column < 0 or column > 9:
        print("Invalid column number. Please try again.")
        continue

    # Check if the column is full
    if grid[9, column] != 0:
        print("Column is full. Please try again.")
        continue

    # Place the player's piece in the column
    for i in range(9, -1, -1):
        if grid[i, column] == 0:
            grid[i, column] = player
            break

    # Check if the player has won
    if check_win(grid, player):
        game_state = "win"
        winner = player1_name if player == player1_symbol else player2_name
        print(f"{winner} wins!")
    elif np.all(grid != 0):
        game_state = "draw"
        print("Draw!")

# Print the final grid
print(grid)

def check_win(grid, player):
    # Check for horizontal wins
    for i in range(10):
        if np.all(grid[i, :] == player):
            return True

    # Check for vertical wins
    for j in range(10):
        if np.all(grid[:, j] == player):
            return True

    # Check for diagonal wins
    for i in range(7):
        for j in range(7):
            if np.all(grid[i:i+3, j:j+3] == player):
                return True

    # Check for anti-diagonal wins
    for i in range(7):
        for j in range(3, 10):
            if np.all(grid[i:i+3, j:j-3:-1] == player):
                return True

    return False
