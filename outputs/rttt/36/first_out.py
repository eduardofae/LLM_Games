import numpy as np

def jdv():
    """
    Plays a game of jdv.

    Args:
        None

    Returns:
        None
    """

    # Create a 3x3 grid
    grid = np.zeros((3, 3), dtype=int)

    # Set the player's turns
    player1 = 1
    player2 = -1

    # Keep track of the current player
    current_player = player1

    # Keep track of the number of moves played
    num_moves = 0

    # Play the game until someone wins or the grid is full
    while True:
        # Get the player's move
        move = input("Player {}'s turn: ".format(current_player))

        # Check if the move is valid
        if not is_valid_move(grid, move):
            print("Invalid move. Please try again.")
            continue

        # Place the player's piece on the grid
        grid[move[0], move[1]] = current_player

        # Increment the number of moves played
        num_moves += 1

        # Check if the player has won
        if has_won(grid, current_player):
            print("Player {} wins!".format(current_player))
            break

        # Check if the game is a draw
        if num_moves == 9:
            print("Draw!")
            break

        # Switch to the other player
        current_player *= -1


def is_valid_move(grid, move):
    """
    Checks if a move is valid.

    Args:
        grid: The current game grid.
        move: The player's move.

    Returns:
        True if the move is valid, False otherwise.
    """

    # Check if the move is within the bounds of the grid
    if move[0] < 0 or move[0] > 2 or move[1] < 0 or move[1] > 2:
        return False

    # Check if the space is already occupied
    if grid[move[0], move[1]] != 0:
        return False

    return True


def has_won(grid, player):
    """
    Checks if a player has won the game.

    Args:
        grid: The current game grid.
        player: The player to check for a win.

    Returns:
        True if the player has won, False otherwise.
    """

    # Check for a win in a row
    for i in range(3):
        if np.all(grid[i, :] == player):
            return True

    # Check for a win in a column
    for j in range(3):
        if np.all(grid[:, j] == player):
            return True

    # Check for a win in a diagonal
    if np.all(np.diag(grid) == player) or np.all(np.diag(np.fliplr(grid)) == player):
        return True

    return False


if __name__ == "__main__":
    jdv()
