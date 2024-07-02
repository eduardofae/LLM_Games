import numpy as np

def jdv(board):
    """
    Plays a game of JDV on the given board.

    Args:
        board: A 3x3 numpy array representing the game board.

    Returns:
        The winning player, or None if the game is a draw.
    """

    # Check if the game is already over.
    winner = check_winner(board)
    if winner is not None:
        return winner

    # Get the next player's move.
    move = get_move(board)

    # Place the player's piece on the board.
    board[move[0], move[1]] = current_player

    # Check if the game is over.
    winner = check_winner(board)
    if winner is not None:
        return winner

    # Switch to the other player's turn.
    current_player = -current_player

    # Recursively call jdv() to continue the game.
    return jdv(board)


def check_winner(board):
    """
    Checks if the given board has a winner.

    Args:
        board: A 3x3 numpy array representing the game board.

    Returns:
        The winning player, or None if the game is not over.
    """

    # Check for a winner in each row.
    for row in board:
        if np.all(row == current_player):
            return current_player

    # Check for a winner in each column.
    for col in board.T:
        if np.all(col == current_player):
            return current_player

    # Check for a winner in each diagonal.
    if np.all(board.diagonal() == current_player):
        return current_player
    if np.all(np.flip(board).diagonal() == current_player):
        return current_player

    # If there are no winners, return None.
    return None


def get_move(board):
    """
    Gets the next player's move.

    Args:
        board: A 3x3 numpy array representing the game board.

    Returns:
        A tuple representing the player's move.
    """

    # Get the player's input.
    move = input("Enter your move (row, col): ")

    # Convert the input to a tuple of integers.
    row, col = map(int, move.split(","))

    # Check if the move is valid.
    if board[row, col] != 0:
        print("Invalid move. Please try again.")
        return get_move(board)

    # Return the player's move.
    return (row, col)


# Set the current player to 1.
current_player = 1

# Create a 3x3 game board.
board = np.zeros((3, 3), dtype=int)

# Play the game.
winner = jdv(board)

# Print the winner.
if winner is not None:
    print("Player {} wins!".format(winner))
else:
    print("The game is a draw.")
