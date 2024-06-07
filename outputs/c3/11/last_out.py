import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Define the players
player1 = 1
player2 = -1

# Define the current player
current_player = player1

# Define the number of wins for each player
player1_wins = 0
player2_wins = 0

# Define the pieces for each player
player1_piece = "X"
player2_piece = "O"

# Define the size of the grid
grid_size = 10

# Define the number of pieces in a row that are required to win
winning_streak = 4

# Define the computer player
computer_player = -1

# Define the difficulty levels
difficulty_levels = ["Easy", "Medium", "Hard"]

# Get the difficulty level from the player
difficulty_level = input("Choose a difficulty level (Easy, Medium, Hard): ")

# Set the computer player's difficulty level
if difficulty_level == "Easy":
    computer_difficulty = 0.1
elif difficulty_level == "Medium":
    computer_difficulty = 0.5
elif difficulty_level == "Hard":
    computer_difficulty = 0.9
else:
    print("Invalid difficulty level")
    exit()

# Game loop
while True:
    # Print the game board
    for row in grid:
        for cell in row:
            if cell == 0:
                print(" ", end=" ")
            elif cell == player1:
                print(player1_piece, end=" ")
            else:
                print(player2_piece, end=" ")
        print()

    # Get the column where the player wants to place their piece
    if current_player == player1:
        column = int(input("Player {} choose a column (0-9): ".format(current_player)))
    else:
        column = get_computer_move(grid, computer_player, winning_streak, computer_difficulty)

    # Check if the column is valid
    if column < 0 or column > grid_size - 1:
        print("Invalid column")
        continue

    # Check if the column is full
    if grid[0, column] != 0:
        print("Column is full")
        continue

    # Place the player's piece in the lowest free space of the column
    for i in range(grid_size - 1, -1, -1):
        if grid[i, column] == 0:
            grid[i, column] = current_player
            break

    # Check if the player has won
    if check_win(grid, current_player, winning_streak):
        print("Player {} wins!".format(current_player))
        if current_player == player1:
            player1_wins += 1
        else:
            player2_wins += 1
        break

    # Check if the game is a draw
    if np.all(grid != 0):
        print("Draw")
        break

    # Switch to the other player
    current_player = -current_player

# Function to check if a player has won
def check_win(grid, player, winning_streak):
    # Check for horizontal wins
    for i in range(grid_size):
        for j in range(grid_size - winning_streak + 1):
            if np.all(grid[i, j:j+winning_streak] == player):
                return True

    # Check for vertical wins
    for j in range(grid_size):
        for i in range(grid_size - winning_streak + 1):
            if np.all(grid[i:i+winning_streak, j] == player):
                return True

    # Check for diagonal wins
    for i in range(grid_size - winning_streak + 1):
        for j in range(grid_size - winning_streak + 1):
            if np.all(grid[i:i+winning_streak, j:j+winning_streak] == player):
                return True

    for i in range(grid_size - winning_streak + 1):
        for j in range(grid_size - 1, winning_streak - 1, -1):
            if np.all(grid[i:i+winning_streak, j:j-winning_streak:-1] == player):
                return True

    return False

# Function to get the computer's move
def get_computer_move(grid, player, winning_streak, difficulty):
    # Check for winning moves
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i, j] == 0:
                grid[i, j] = player
                if check_win(grid, player, winning_streak):
                    grid[i, j] = 0
                    return j
                grid[i, j] = 0

    # Check for blocking moves
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i, j] == 0:
                grid[i, j] = -player
                if check_win(grid, -player, winning_streak):
                    grid[i, j] = 0
                    return j
                grid[i, j] = 0

    # Choose a random move with a probability of difficulty
    while True:
        column = np.random.randint(0, grid_size)
        if grid[0, column] == 0 and np.random.rand() < difficulty:
            return column

# Reset the game
def reset_game():
    global grid, current_player
    grid = np.zeros((grid_size, grid_size), dtype=int)
    current_player = player1

# Play again
while True:
    choice = input("Play again? (y/n): ")
    if choice == "y":
        reset_game()
    else:
        break

print("Final score:")
print("Player 1:", player1_wins)
print("Player 2:", player2_wins)
