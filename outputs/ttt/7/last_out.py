import random
import pickle

# Create a 3x3 grid
grid = [['-', '-', '-'],
        ['-', '-', '-'],
        ['-', '-', '-']]

# Get player names
player1 = input("Enter player 1 name: ")
player2 = "Computer"

# Set player symbols
player1_symbol = 'X'
player2_symbol = 'O'

# Set current player
current_player = player1

# Initialize player win counts
player1_wins = 0
player2_wins = 0

# Set difficulty level for computer opponent
difficulty = input("Choose difficulty level for computer opponent (easy/hard): ")

# Set game settings
grid_size = 3
num_players = 2

# Game loop
while True:
    # Print the grid
    print("Current grid:")
    for row in grid:
        print(' '.join(row))

    # Get player input
    if current_player == player1:
        try:
            row = int(input("Enter row (1-3): "))
            col = int(input("Enter column (1-3): "))
        except ValueError:
            print("Invalid input. Please enter integers only.")
            continue

        # Check if the input is valid
        if not (1 <= row <= grid_size and 1 <= col <= grid_size):
            print("Invalid input. Row and column must be between 1 and 3.")
            continue

        # Check if the space is free
        if grid[row-1][col-1] != '-':
            print("Invalid move. Space already occupied.")
            continue

        # Place the player's symbol in the space
        grid[row-1][col-1] = current_player
    else:
        # Computer's turn
        if difficulty == "easy":
            # Random move
            available_moves = [(row, col) for row in range(grid_size) for col in range(grid_size) if grid[row][col] == '-']
            row, col = random.choice(available_moves)
        elif difficulty == "hard":
            # Minimax algorithm to find the best move
            best_score = -1000
            best_move = None
            for row in range(grid_size):
                for col in range(grid_size):
                    if grid[row][col] == '-':
                        grid[row][col] = player2_symbol
                        score = minimax(grid, False)
                        grid[row][col] = '-'
                        if score > best_score:
                            best_score = score
                            best_move = (row, col)
            row, col = best_move
        grid[row][col] = current_player

    # Check if the player has won
    if check_win(grid, current_player):
        if current_player == player1:
            player1_wins += 1
        else:
            player2_wins += 1
        print(f"{current_player} wins!")
        break

    # Check if the game is a draw
    if check_draw(grid):
        print("It's a draw!")
        break

    # Switch the current player
    if current_player == player1:
        current_player = player2
    else:
        current_player = player1

# Print player win counts
print(f"{player1} wins: {player1_wins}")
print(f"{player2} wins: {player2_wins}")

# Ask to play again
while True:
    play_again = input("Do you want to play again? (y/n): ")
    if play_again == 'y':
        # Reset the grid and start a new game
        grid = [['-', '-', '-'],
                ['-', '-', '-'],
                ['-', '-', '-']]
        current_player = player1
    else:
        break

# Save the game state
save_game = input("Do you want to save the game? (y/n): ")
if save_game == 'y':
    with open('game_state.pkl', 'wb') as f:
        pickle.dump((grid, current_player, player1_wins, player2_wins), f)

# Load the game state
load_game = input("Do you want to load a saved game? (y/n): ")
if load_game == 'y':
    with open('game_state.pkl', 'rb') as f:
        grid, current_player, player1_wins, player2_wins = pickle.load(f)

# Check if a player has won
def check_win(grid, player):
    # Check horizontally
    for row in grid:
        if all(element == player for element in row):
            return True

    # Check vertically
    for col in range(grid_size):
        if all(grid[row][col] == player for row in range(grid_size)):
            return True

    # Check diagonally
    if grid[0][0] == player and grid[1][1] == player and grid[2][2] == player:
        return True
    if grid[0][2] == player and grid[1][1] == player and grid[2][0] == player:
        return True

    return False

# Check if the game is a draw
def check_draw(grid):
    for row in grid:
        for element in row:
            if element == '-':
                return False
    return True

# Minimax algorithm for computer opponent (hard difficulty)
def minimax(grid, is_maximizing):
    # Check if the game is over
    if check_win(grid, player1_symbol):
        return -1
    elif check_win(grid, player2_symbol):
        return 1
    elif check_draw(grid):
        return 0

    # Get all possible moves for the current player
    available_moves = [(row, col) for row in range(grid_size) for col in range(grid_size) if grid[row][col] == '-']

    # Initialize the best score
    best_score = -1000 if is_maximizing else 1000

    # Iterate over all possible moves
    for row, col in available_moves:
        # Make the move
        grid[row][col] = player2_symbol if is_maximizing else player1_symbol

        # Recursively call minimax to evaluate the move
        score = minimax(grid, not is_maximizing)

        # Undo the move
        grid[row][col] = '-'

        # Update the best score if necessary
        if is_maximizing and score > best_score:
            best_score = score
        elif not is_maximizing and score < best_score:
            best_score = score

    return best_score
