import numpy as np

# Create a 3x3 grid
grid = np.zeros((3, 3), dtype=int)

# Define the players' symbols
player1 = 'X'
player2 = 'O'

# Keep track of the current player
current_player = player1

# Keep track of the scores
player1_score = 0
player2_score = 0

# Keep track of the game statistics
num_moves = 0
avg_game_length = 0

# Main game loop
while True:
    # Print the grid
    print_grid(grid)

    # Get the player's move
    if current_player == player1:
        try:
            row, col = map(int, input("Enter your move (row, column): ").split())
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a comma.")
            continue
    else:
        # AI opponent's move
        row, col = get_ai_move(grid)

    # Check if the move is valid
    if not (0 <= row < grid.shape[0] and 0 <= col < grid.shape[1]) or grid[row, col] != 0:
        print("Invalid move. Please try again.")
        continue

    # Place the player's piece on the grid
    grid[row, col] = current_player

    # Increment the number of moves
    num_moves += 1

    # Check if the game is over
    if check_win(grid, current_player):
        print(f"{current_player} wins!")
        if current_player == player1:
            player1_score += 1
        else:
            player2_score += 1
        break
    elif np.all(grid != 0):
        print("Tie!")
        break

    # Switch to the other player
    current_player = player1 if current_player == player2 else player2

# Calculate the average game length
avg_game_length = num_moves / (player1_score + player2_score + 1)

# Print the scores and game statistics
print(f"Player 1 score: {player1_score}")
print(f"Player 2 score: {player2_score}")
print(f"Number of moves: {num_moves}")
print(f"Average game length: {avg_game_length:.2f}")

# Ask the user if they want to play again
while True:
    choice = input("Do you want to play again? (y/n): ")
    if choice == 'y':
        # Reset the grid and start a new game
        grid = np.zeros((3, 3), dtype=int)
        current_player = player1
        num_moves = 0
    elif choice == 'n':
        # Exit the game
        break
    else:
        print("Invalid choice. Please enter 'y' or 'n'.")

# Define the function to print the grid
def print_grid(grid):
    for row in grid:
        for cell in row:
            if cell == 0:
                print(' ', end='|')
            else:
                print(cell, end='|')
        print()

# Define the function to check if a player has won
def check_win(grid, player):
    # Check rows
    for row in range(grid.shape[0]):
        if np.all(grid[row, :] == player):
            return True

    # Check columns
    for col in range(grid.shape[1]):
        if np.all(grid[:, col] == player):
            return True

    # Check diagonals
    if np.all(grid.diagonal() == player) or np.all(np.flip(grid).diagonal() == player):
        return True

    # No win yet
    return False

# Define the function to get the AI opponent's move
def get_ai_move(grid):
    # Get a list of all possible moves
    possible_moves = []
    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            if grid[row, col] == 0:
                possible_moves.append((row, col))

    # Choose a random move from the list
    return random.choice(possible_moves)
