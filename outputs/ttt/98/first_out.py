import numpy as np

def jdv():
    # Create a 3x3 grid
    grid = np.zeros((3, 3), dtype=int)

    # Set the current player to 1
    player = 1

    # Create a loop that runs until there is a winner or a draw
    while True:
        # Print the grid
        print(grid)

        # Get the move from the current player
        row, col = map(int, input("Player {}'s turn: ".format(player)).split())

        # Check if the move is valid
        if grid[row, col] != 0:
            print("Invalid move.")
            continue

        # Place the player's piece in the grid
        grid[row, col] = player

        # Check if the current player has won
        if check_win(grid, player):
            print("Player {} wins!".format(player))
            break

        # Check if there is a draw
        if np.all(grid != 0):
            print("Draw!")
            break

        # Switch to the other player
        player = 3 - player

def check_win(grid, player):
    # Check the rows for a win
    for row in grid:
        if np.all(row == player):
            return True

    # Check the columns for a win
    for col in grid.T:
        if np.all(col == player):
            return True

    # Check the diagonals for a win
    if np.all(grid.diagonal() == player) or np.all(np.flip(grid).diagonal() == player):
        return True

    # No win yet
    return False

if __name__ == "__main__":
    jdv()
