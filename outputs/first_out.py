import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Set the players' turns
player1 = 1
player2 = 2

# Set the game status
game_status = "ongoing"

# Main game loop
while game_status == "ongoing":
    print("Current grid:")
    print(grid)

    # Get the player's move
    if player1 == 1:
        move = int(input("Player 1, enter a column number (1-10): "))
    else:
        move = int(input("Player 2, enter a column number (1-10): "))

    # Validate the move
    if move < 1 or move > 10:
        print("Invalid move. Please enter a number between 1 and 10")
        continue

    # Check if the column is full
    if grid[:, move-1].max() == 3:
        print("Column is full. Please choose another column")
        continue

    # Place the player's piece in the lowest free space of the column
    for i in range(9, -1, -1):
        if grid[i, move-1] == 0:
            grid[i, move-1] = player1
            break

    # Check if the player has made a line of 3
    if check_win(grid, player1):
        game_status = "player1_wins"
    elif check_win(grid, player2):
        game_status = "player2_wins"
    elif np.all(grid != 0):
        game_status = "draw"

# Print the final game status
print("Game over!")
print(f"Game status: {game_status}")


# Function to check if a player has made a line of 3
def check_win(grid, player):
    # Check for horizontal lines
    for i in range(10):
        if np.all(grid[i, :] == player):
            return True

    # Check for vertical lines
    for j in range(10):
        if np.all(grid[:, j] == player):
            return True

    # Check for diagonal lines
    for i in range(10):
        for j in range(10):
            if i == j and np.all(np.diag(grid) == player):
                return True
            elif i + j == 9 and np.all(np.diag(np.fliplr(grid)) == player):
                return True

    return False