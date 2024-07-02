import numpy as np

def jdv():
    """
    Plays a game of JDV (3x3 grid tic-tac-toe).

    Returns:
        The winner of the game, or "Draw" if the game is a draw.
    """

    # Create a 3x3 grid
    board = np.zeros((3, 3))

    # Set the current player to 1
    player = 1

    # Loop until the game is over
    while True:
        # Get the player's move
        move = input("Player {}'s turn: ".format(player))

        # Convert the move to a row and column
        row, col = [int(x) for x in move.split(",")]

        # Check if the move is valid
        if board[row, col] != 0:
            print("Invalid move. Please try again.")
            continue

        # Place the player's piece on the board
        board[row, col] = player

        # Check if the player has won
        if check_win(board, player):
            print("Player {} wins!".format(player))
            return player

        # Check if the game is a draw
        if np.all(board != 0):
            print("Draw!")
            return "Draw"

        # Switch to the other player
        player = 3 - player

def check_win(board, player):
    """
    Checks if the given player has won the game.

    Args:
        board: The current state of the game board.
        player: The player to check for a win.

    Returns:
        True if the player has won, False otherwise.
    """

    # Check for a win in each row
    for row in range(3):
        if np.all(board[row, :] == player):
            return True

    # Check for a win in each column
    for col in range(3):
        if np.all(board[:, col] == player):
            return True

    # Check for a win in each diagonal
    if np.all(board.diagonal() == player) or np.all(np.flip(board).diagonal() == player):
        return True

    # No win found
    return False

if __name__ == "__main__":
    jdv()
