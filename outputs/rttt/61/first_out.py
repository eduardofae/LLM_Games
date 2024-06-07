import numpy as np

def jdv_game():
    """Play a game of JDV (3x3 grid, 2 players take turns placing their pieces in a free space until one of them makes a line with 3 adjacent pieces, in which case they lose)"""

    # Create a 3x3 grid
    grid = np.zeros((3, 3), dtype=int)

    # Initialize the current player
    current_player = 1

    # Main game loop
    while True:
        # Get the player's move
        move = input(f"Player {current_player}, enter your move (row, column): ")
        row, column = map(int, move.split(","))

        # Check if the move is valid
        if grid[row, column] != 0:
            print("Invalid move. Please try again.")
            continue

        # Place the player's piece on the grid
        grid[row, column] = current_player

        # Check if the player has won
        if check_win(grid, current_player):
            print(f"Player {current_player} wins!")
            break

        # Check if the game is a draw
        if np.all(grid != 0):
            print("Draw!")
            break

        # Switch to the other player
        current_player = 3 - current_player

def check_win(grid, player):
    """Check if the given player has won the game"""

    # Check for horizontal wins
    for row in range(3):
        if np.all(grid[row, :] == player):
            return True

    # Check for vertical wins
    for column in range(3):
        if np.all(grid[:, column] == player):
            return True

    # Check for diagonal wins
    if np.all(np.diagonal(grid) == player) or np.all(np.diagonal(np.flip(grid)) == player):
        return True

    # No win condition met
    return False

if __name__ == "__main__":
    jdv_game()
