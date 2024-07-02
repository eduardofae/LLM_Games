import numpy as np

# Create the grid
grid = np.zeros((10, 10))

# Define the players
player1 = 1
player2 = -1

# Define the game state
game_over = False
draw = False

# Get the players' names
player1_name = input("Player 1, enter your name: ")
player2_name = input("Player 2, enter your name: ")

# Initialize the number of wins and losses for each player
player1_wins = 0
player2_wins = 0

# Initialize the number of turns
num_turns = 0

# Start the game
while not game_over:
    # Get the player's move
    if grid[9, 0] == 0:
        column = int(input("{}({}): Enter a column (0-9): ".format(player1_name, player1_wins)))
    else:
        column = int(input("{}({}): Enter a column (0-9): ".format(player2_name, player2_wins)))

    # Check if the move is valid
    if column < 0 or column > 9 or grid[9, column] != 0:
        print("Invalid move, try again.")
        continue

    # Update the grid
    for i in range(9, -1, -1):
        if grid[i, column] == 0:
            grid[i, column] = player1 if player1 == 1 else player2
            break

    # Increment the number of turns
    num_turns += 1

    # Check if the player has won
    if check_win(grid, player1) or check_win(grid, player2):
        game_over = True
        if player1 == 1:
            player1_wins += 1
            print("{} wins!".format(player1_name))
        else:
            player2_wins += 1
            print("{} wins!".format(player2_name))

    # Check if there is a draw
    elif np.all(grid != 0):
        game_over = True
        draw = True
        print("Draw!")

    # Switch the player
    player1, player2 = player2, player1

# Define the function to check for a win
def check_win(grid, player):
    # Check for horizontal wins
    for row in range(10):
        if np.all(grid[row, :] == player):
            return True

    # Check for vertical wins
    for col in range(10):
        if np.all(grid[:, col] == player):
            return True

    # Check for diagonal wins
    for i in range(10):
        if np.all(grid[i, :i] == player) or np.all(grid[i, 9-i:] == player):
            return True

    return False

# Reset the game
def reset_game():
    global grid, game_over, draw, player1, player2, num_turns
    grid = np.zeros((10, 10))
    game_over = False
    draw = False
    player1 = 1
    player2 = -1
    num_turns = 0

# Save the game state
def save_game():
    with open('game_state.txt', 'w') as f:
        f.write(grid.tostring())

# Load the game state
def load_game():
    global grid
    with open('game_state.txt', 'r') as f:
        grid = np.fromstring(f.read(), dtype=int).reshape((10, 10))

# Main game loop
while True:
    # Get the player's input
    command = input("Enter a command (play/reset/save/load/quit): ")

    # Execute the command
    if command == "play":
        # Start a new game
        reset_game()
        while not game_over:
            # Get the player's move
            if grid[9, 0] == 0:
                column = int(input("{}({}): Enter a column (0-9): ".format(player1_name, player1_wins)))
            else:
                column = int(input("{}({}): Enter a column (0-9): ".format(player2_name, player2_wins)))

            # Check if the move is valid
            if column < 0 or column > 9 or grid[9, column] != 0:
                print("Invalid move, try again.")
                continue

            # Update the grid
            for i in range(9, -1, -1):
                if grid[i, column] == 0:
                    grid[i, column] = player1 if player1 == 1 else player2
                    break

            # Increment the number of turns
            num_turns += 1

            # Check if the player has won
            if check_win(grid, player1) or check_win(grid, player2):
                game_over = True
                if player1 == 1:
                    player1_wins += 1
                    print("{} wins!".format(player1_name))
                else:
                    player2_wins += 1
                    print("{} wins!".format(player2_name))

            # Check if there is a draw
            elif np.all(grid != 0):
                game_over = True
                draw = True
                print("Draw!")

            # Switch the player
            player1, player2 = player2, player1
    elif command == "reset":
        # Reset the game
        reset_game()
    elif command == "save":
        # Save the game state
        save_game()
    elif command == "load":
        # Load the game state
        load_game()
    elif command == "quit":
        # Quit the game
        break
    else:
        # Invalid command
        print("Invalid command.")
