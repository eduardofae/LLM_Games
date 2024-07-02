import numpy as np

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Define the players
players = ['X', 'O']

# Define the game loop function
def game_loop():
    while True:
        # Get the current player
        player = players[0]

        # Display the game board
        print(grid)

        # Get the column where the player wants to place their piece
        while True:
            try:
                column = int(input(f"Player {player}, choose a column (0-9): "))
                if not (0 <= column <= 9):
                    print("Invalid column. Please choose a column between 0 and 9.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter an integer between 0 and 9.")

        # Check if the column is full
        if grid[:, column].max() == 2:
            print("Column is full. Please choose another column.")
            continue

        # Place the player's piece in the lowest free space of the column
        row = grid[:, column].argmax()
        grid[row, column] = 1 if player == 'X' else 2

        # Check if the player has won
        if check_win(grid, player):
            print(f"Player {player} wins!")
            break

        # Check if the game is a draw
        if grid.max() == 2 and np.all(grid[:, column].max() == 2):
            print("Draw!")
            break

        # Switch to the other player
        players = players[1:]

    # Display the final game board
    print(grid)


# Define the function to check if a player has won
def check_win(grid, player):
    # Check for horizontal wins
    for row in range(10):
        if np.all(grid[row, :] == player):
            return True

    # Check for vertical wins
    for column in range(10):
        if np.all(grid[:, column] == player):
            return True

    # Check for diagonal wins
    for i in range(-9, 10):
        # Check for diagonal wins from top left to bottom right
        if np.all(np.diagonal(np.roll(grid, i, axis=0), i) == player):
            return True

        # Check for diagonal wins from bottom left to top right
        if np.all(np.diagonal(np.roll(grid, -i, axis=0), -i) == player):
            return True

    # No win found
    return False


# Start the game loop
game_loop()
