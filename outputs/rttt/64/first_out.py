import numpy as np

def jdv():
    """
    jdv game.

    The game is played by two players who take turns placing their pieces in a free space of a 3x3 grid.
    The first player to make a line of 3 (horizontally, vertically or diagonally) adjacent pieces loses the game.
    If there are no more free spaces, the game is declared a draw.
    """

    # Create the game board
    board = np.zeros((3, 3))

    # Create a list of the available moves
    moves = [(i, j) for i in range(3) for j in range(3)]

    # Create a dictionary to store the player's moves
    player_moves = {1: [], 2: []}

    # Set the current player to 1
    current_player = 1

    # Loop until the game is over
    while True:

        # Get the player's move
        move = input("Player {}'s turn: ".format(current_player))

        # Check if the move is valid
        if move not in moves:
            print("Invalid move.")
            continue

        # Update the board
        board[move] = current_player

        # Update the list of available moves
        moves.remove(move)

        # Update the player's moves
        player_moves[current_player].append(move)

        # Check if the game is over
        if check_win(board, current_player):
            print("Player {} loses.".format(current_player))
            break
        elif len(moves) == 0:
            print("Draw.")
            break

        # Switch the current player
        current_player = 3 - current_player

def check_win(board, player):
    """
    Check if a player has won the game.

    Args:
        board: The game board.
        player: The current player.

    Returns:
        True if the player has won, False otherwise.
    """

    # Check for a horizontal win
    for i in range(3):
        if np.all(board[i] == player):
            return True

    # Check for a vertical win
    for j in range(3):
        if np.all(board[:, j] == player):
            return True

    # Check for a diagonal win
    if np.all(np.diagonal(board) == player):
        return True
    if np.all(np.diagonal(np.flipud(board)) == player):
        return True

    # No win
    return False

if __name__ == "__main__":
    jdv()
