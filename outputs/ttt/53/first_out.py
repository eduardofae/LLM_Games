import numpy as np

def check_winner(board):
    """
    Check if there is a winner in the board.

    Args:
        board (np.array): The game board.

    Returns:
        bool: True if there is a winner, False otherwise.
    """
    # Check if there is a winner in the rows.
    for row in board:
        if all(row == row[0]) and row[0] != 0:
            return True

    # Check if there is a winner in the columns.
    for col in board.T:
        if all(col == col[0]) and col[0] != 0:
            return True

    # Check if there is a winner in the diagonals.
    if all(board.diagonal() == board.diagonal()[0]) and board.diagonal()[0] != 0:
        return True

    if all(np.flip(board).diagonal() == np.flip(board).diagonal()[0]) and np.flip(board).diagonal()[0] != 0:
        return True

    return False


def print_board(board):
    """
    Print the game board.

    Args:
        board (np.array): The game board.
    """
    for row in board:
        print(" | ".join(map(str, row)))
    print()


def get_player_input(player):
    """
    Get the player's input.

    Args:
        player (int): The player number (1 or 2).

    Returns:
        tuple: The row and column of the player's move.
    """
    while True:
        row = int(input("Player {} enter row: ".format(player))) - 1
        col = int(input("Player {} enter column: ".format(player))) - 1

        if 0 <= row < 3 and 0 <= col < 3 and board[row, col] == 0:
            return row, col

        print("Invalid move. Try again.")


# Create the game board.
board = np.zeros((3, 3), dtype=int)

# Set the player number.
player = 1

# Game loop.
while True:
    # Print the game board.
    print_board(board)

    # Get the player's input.
    row, col = get_player_input(player)

    # Place the player's piece on the board.
    board[row, col] = player

    # Check if there is a winner.
    if check_winner(board):
        print("Player {} wins!".format(player))
        break

    # Check if there is a draw.
    if np.all(board != 0):
        print("Draw!")
        break

    # Switch the player number.
    player = 3 - player
