import numpy as np

def jdv():
    # Create a 3x3 grid
    grid = np.zeros((3, 3))

    # Create a list of players
    players = ['X', 'O']

    # Set the current player to the first player
    current_player = 0

    # Game loop
    while True:

        # Get the player's move
        row, col = map(int, input("Player {}'s turn (row, col): ".format(players[current_player])).split())

        # Check if the move is valid
        if grid[row, col] != 0:
            print("Invalid move. Try again.")
            continue

        # Place the player's piece on the grid
        grid[row, col] = players[current_player]

        # Check if the player made a line
        if check_for_win(grid):
            print("Player {} wins!".format(players[current_player]))
            break

        # Check if the game is a draw
        if np.all(grid != 0):
            print("Draw!")
            break

        # Switch to the other player
        current_player = (current_player + 1) % 2

def check_for_win(grid):
    # Check for a horizontal win
    for row in range(3):
        if np.all(grid[row, :] == grid[row, 0]) and grid[row, 0] != 0:
            return True

    # Check for a vertical win
    for col in range(3):
        if np.all(grid[:, col] == grid[0, col]) and grid[0, col] != 0:
            return True

    # Check for a diagonal win
    if np.all(grid.diagonal() == grid[0, 0]) and grid[0, 0] != 0:
        return True
    if np.all(np.flip(grid).diagonal() == grid[0, 2]) and grid[0, 2] != 0:
        return True

    # No win yet
    return False

if __name__ == "__main__":
    jdv()
