
import numpy as np

def jdv():
    # Create a 3x3 grid
    grid = np.zeros((3, 3), dtype=int)

    # Set the player turn to 1
    player = 1

    # Keep track of the number of moves made
    moves = 0

    # Main game loop
    while True:
        # Get the player's move
        row, col = map(int, input("Enter your move (row, column): ").split())

        # Check if the move is valid
        if grid[row, col] != 0:
            print("Invalid move. Please try again.")
            continue

        # Place the player's piece on the grid
        grid[row, col] = player

        # Increment the number of moves made
        moves += 1

        # Check if the player has won
        if check_win(grid, player):
            print(f"Player {player} wins!")
            break

        # Check if the game is a draw
        if moves == 9:
            print("Draw!")
            break

        # Switch to the other player
        player = 3 - player


# Function to check if a player has won
def check_win(grid, player):
    # Check rows
    for row in range(3):
        if np.all(grid[row, :] == player):
            return True

    # Check columns
    for col in range(3):
        if np.all(grid[:, col] == player):
            return True

    # Check diagonals
    if np.all(np.diag(grid) == player):
        return True

    if np.all(np.diag(np.flip(grid)) == player):
        return True

    # No win yet
    return False


# Start the game
if __name__ == "__main__":
    jdv()
