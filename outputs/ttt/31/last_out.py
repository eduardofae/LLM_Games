import numpy as np

def jdv():
    """
    Plays a game of jdv.

    The game is played on a 3x3 grid. Two players take turns placing their pieces in a free space of the grid.
    The first player to make a line of 3 (horizontally, vertically, or diagonally) adjacent pieces wins.
    If there are no more free spaces, the game is declared a draw.
    """

    # Create the game board.
    board = np.zeros((3, 3), dtype=int)

    # Create a variable to track the current player.
    current_player = 1

    # Create a loop to play the game.
    while True:
        # Get the player's move.
        try:
            move = input("Player {}'s move (row, column): ".format(current_player))
            row, column = map(int, move.split(","))
        except ValueError:
            print("Invalid move. Please try again.")
            continue

        # Check if the move is valid.
        if not (0 <= row < 3 and 0 <= column < 3) or board[row, column] != 0:
            print("Invalid move. Please try again.")
            continue

        # Place the player's piece on the board.
        board[row, column] = current_player

        # Check if the player has won.
        if check_win(board, current_player):
            print("Player {} wins!".format(current_player))
            break

        # Check if the game is a draw.
        if np.all(board != 0):
            print("Draw!")
            break

        # Switch to the other player.
        current_player = 3 - current_player

def check_win(board, player):
    """
    Checks if the given player has won the game.

    Args:
        board: The game board.
        player: The player to check for a win.

    Returns:
        True if the player has won, False otherwise.
    """

    # Check for a win horizontally.
    for row in range(3):
        if np.all(board[row, :] == player):
            return True

    # Check for a win vertically.
    for column in range(3):
        if np.all(board[:, column] == player):
            return True

    # Check for a win diagonally.
    if np.all(board.diagonal() == player):
        return True
    if np.all(np.flip(board).diagonal() == player):
        return True

    # No win found.
    return False

if __name__ == "__main__":
    jdv()
