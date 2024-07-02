import numpy as np

def jdv():
    """
    Play a game of jdv.

    The game is played on a 3x3 grid. Two players take turns placing their pieces
    in a free space of the grid. The first player to make a line of 3 (horizontally,
    vertically, or diagonally) adjacent pieces wins. If there are no more free spaces,
    the game is declared a draw.
    """

    # Create a 3x3 grid
    grid = np.zeros((3, 3), dtype=int)

    # Set the current player to 1
    current_player = 1

    # Play the game until there is a winner or a draw
    while True:
        # Get the player's move
        move = input(f"Player {current_player}, enter your move (row, column): ")
        row, column = move.split(",")
        row = int(row)
        column = int(column)

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

        # Check if there is a draw
        if np.all(grid != 0):
            print("Draw!")
            break

        # Switch to the other player
        current_player = 3 - current_player

def check_win(grid, player):
    """
    Check if the player has won the game.

    Args:
        grid (numpy.array): The game grid.
        player (int): The player to check for a win.

    Returns:
        bool: True if the player has won, False otherwise.
    """

    # Check for a win in each row
    for row in range(3):
        if np.all(grid[row, :] == player):
            return True

    # Check for a win in each column
    for column in range(3):
        if np.all(grid[:, column] == player):
            return True

    # Check for a win in each diagonal
    if np.all(grid.diagonal() == player):
        return True
    if np.all(np.flip(grid).diagonal() == player):
        return True

    # No win found
    return False

if __name__ == "__main__":
    jdv()
