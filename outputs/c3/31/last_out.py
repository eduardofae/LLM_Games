import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Define the players' symbols
player1_symbol = input("Player 1 symbol (X/O): ")
player2_symbol = input("Player 2 symbol (X/O): ")

# Define the game state
game_state = "ongoing"

# Get the players' names
player1_name = input("Player 1 name: ")
player2_name = input("Player 2 name: ")

# Start the game loop
while game_state == "ongoing":
    # Get the player's move
    player = player1_symbol if game_state == "ongoing" else player2_symbol
    try:
        column = int(input(f"{player1_name if player == player1_symbol else player2_name}'s turn. Enter a column number (1-10): ")) - 1
    except ValueError:
        print("Invalid column number. Please try again.")
        continue

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

# Add replayability
while True:
    choice = input("Play again (y/n)? ")
    if choice == "y":
        # Reset the grid
        grid = np.zeros((10, 10), dtype=int)
        # Reset the game state
        game_state = "ongoing"
        # Start a new game
        continue
    else:
        break

# Add performance optimizations
def check_win_optimized(grid, player, last_move):
    # Check for horizontal wins
    if last_move[0] >= 0 and last_move[0] <= 6:
        if np.all(grid[last_move[0]:last_move[0]+3, last_move[1]] == player):
            return True

    # Check for vertical wins
    if last_move[1] >= 0 and last_move[1] <= 6:
        if np.all(grid[last_move[0], last_move[1]:last_move[1]+3] == player):
            return True

    # Check for diagonal wins
    if last_move[0] >= 0 and last_move[0] <= 6 and last_move[1] >= 0 and last_move[1] <= 6:
        if np.all(grid[last_move[0]:last_move[0]+3, last_move[1]:last_move[1]+3] == player):
            return True

    # Check for anti-diagonal wins
    if last_move[0] >= 0 and last_move[0] <= 6 and last_move[1] >= 3 and last_move[1] <= 9:
        if np.all(grid[last_move[0]:last_move[0]+3, last_move[1]:last_move[1]-3:-1] == player):
            return True

    return False

# Update the check_win function
check_win = check_win_optimized

# Add additional features
# Keep track of the number of wins
player1_wins = 0
player2_wins = 0

# Implement a timer
import time
time_limit = int(input("Time limit (seconds): "))
start_time = time.time()

# Start the game loop
while game_state == "ongoing":
    # Get the player's move
    player = player1_symbol if game_state == "ongoing" else player2_symbol
    try:
        column = int(input(f"{player1_name if player == player1_symbol else player2_name}'s turn. Enter a column number (1-10): ")) - 1
    except ValueError:
        print("Invalid column number. Please try again.")
        continue

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
        if player == player1_symbol:
            player1_wins += 1
        else:
            player2_wins += 1
    elif np.all(grid != 0):
        game_state = "draw"
        print("Draw!")

    # Check if the time limit has been reached
    if time.time() - start_time >= time_limit:
        game_state = "time_out"
        print("Time out!")
        if player1_wins > player2_wins:
            winner = player1_name
        elif player2_wins > player1_wins:
            winner = player2_name
        else:
            winner = "Draw"
        print(f"{winner} wins!")

# Print the final grid
print(grid)

# Print the number of wins
print(f"{player1_name}: {player1_wins} wins")
print(f"{player2_name}: {player2_wins} wins")

# Add online multiplayer
# ...

# Add a graphical user interface (GUI)
# ...

# Add error handling to the online multiplayer functionality
# ...

# Implement a replay system
# ...
