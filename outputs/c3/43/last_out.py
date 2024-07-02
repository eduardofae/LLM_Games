import numpy as np

# Game constants
GRID_SIZE = 10
PLAYERS = ["Player 1", "Player 2"]

def create_grid():
    """Creates a new empty grid."""
    return np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)

def print_grid(grid):
    """Prints the grid to the console."""
    for row in grid:
        for cell in row:
            print(cell, end=" ")
        print()

def place_piece(grid, player, col):
    """Places a piece in the lowest free space of the given column."""
    for row in range(GRID_SIZE-1, -1, -1):
        if grid[row][col] == 0:
            grid[row][col] = player
            return

def check_win(grid):
    """Checks if there is a line of 3 adjacent pieces."""
    # Check horizontal lines
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE-2):
            if grid[row][col] != 0 and grid[row][col] == grid[row][col+1] == grid[row][col+2]:
                return grid[row][col]

    # Check vertical lines
    for col in range(GRID_SIZE):
        for row in range(GRID_SIZE-2):
            if grid[row][col] != 0 and grid[row][col] == grid[row+1][col] == grid[row+2][col]:
                return grid[row][col]

    # Check diagonal lines
    for row in range(GRID_SIZE-2):
        for col in range(GRID_SIZE-2):
            if grid[row][col] != 0 and grid[row][col] == grid[row+1][col+1] == grid[row+2][col+2]:
                return grid[row][col]
    
    return 0

def is_draw(grid):
    """Checks if the game is a draw."""
    return np.all(grid != 0)

def get_player_input(player):
    """Gets the player's input for the column to place their piece."""
    while True:
        try:
            col = int(input("{}: Choose a column (0-9): ".format(player)))
            if 0 <= col < GRID_SIZE:
                return col
            else:
                print("Invalid column. Please choose a column between 0 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 9.")

def main():
    """Plays the game."""
    # Create a new grid
    grid = create_grid()
    
    # Display welcome message and get player names
    print("Welcome to Connect Four!")
    player1 = input("Enter Player 1's name: ")
    player2 = input("Enter Player 2's name: ")

    # Set the current player
    current_player = 0

    # Game loop
    while True:
        # Print the grid
        print_grid(grid)

        # Get the player's input
        col = get_player_input(PLAYERS[current_player])

        # Place the piece
        place_piece(grid, current_player + 1, col)

        # Check for a win
        winner = check_win(grid)
        if winner != 0:
            print("{} wins!".format(PLAYERS[current_player]))
            break

        # Check for a draw
        if is_draw(grid):
            print("Draw!")
            break

        # Switch to the other player
        current_player = (current_player + 1) % 2

if __name__ == "__main__":
    main()
