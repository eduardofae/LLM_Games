import numpy as np

def jdv():
    """
    Plays a game of jdv.

    Args:
        None

    Returns:
        None
    """

    # Create a 3x3 board
    board = np.zeros((3, 3), dtype=int)

    # Set the player's turns
    player_1 = 1
    player_2 = -1

    # Keep track of the current player
    current_player_id = player_1

    # Keep track of the number of moves played
    num_moves_played = 0

    # Play the game until someone wins or the board is full
    while True:
        # Get the player's move
        move = input("Player {}'s turn: ".format(current_player_id))

        try:
            # Convert the player's move to a tuple of integers
            move = tuple(int(x) for x in move.split())
        except ValueError:
            # The player's move is invalid
            print("Invalid move. Please try again.")
            continue

        # Check if the move is valid
        if not is_move_valid(board, move):
            print("Invalid move. Please try again.")
            continue

        # Place the player's piece on the board
        board[move[0], move[1]] = current_player_id

        # Increment the number of moves played
        num_moves_played += 1

        # Check if the player has won
        if has_player_won(board, current_player_id):
            print("Player {} wins!".format(current_player_id))
            break

        # Check if the game is a draw
        if num_moves_played == 9:
            print("Draw!")
            break

        # Switch to the other player
        current_player_id *= -1


def is_move_valid(board, move):
    """
    Checks if a move is valid.

    Args:
        board: The current game board.
        move: The player's move.

    Returns:
        True if the move is valid, False otherwise.
    """

    # Check if the move is within the bounds of the board
    if move[0] < 0 or move[0] > 2 or move[1] < 0 or move[1] > 2:
        return False

    # Check if the space is already occupied
    if board[move[0], move[1]] != 0:
        return False

    return True


def has_player_won(board, player):
    """
    Checks if a player has won the game.

    Args:
        board: The current game board.
        player: The player to check for a win.

    Returns:
        True if the player has won, False otherwise.
    """

    # Check for a win in a row
    for i in range(3):
        if np.all(board[i, :] == player):
            return True

    # Check for a win in a column
    for j in range(3):
        if np.all(board[:, j] == player):
            return True

    # Check for a win in a diagonal
    if np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player):
        return True

    return False


if __name__ == "__main__":
    try:
        jdv()
    except KeyboardInterrupt:
        print("\nExiting game.")
