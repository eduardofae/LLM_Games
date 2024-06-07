import numpy as np

def check_winner(board):
    """
    Check if there is a winner in the given board.

    Args:
        board (np.array): The game board.

    Returns:
        int: The player number of the winner, or 0 if there is no winner yet.
    """

    def check_line(line):
        """
        Check if a given line (row, column, or diagonal) has a winner.

        Args:
            line (np.array): The line to check.

        Returns:
            int: The player number of the winner, or 0 if there is no winner yet.
        """
        return np.all(line == line[0]) and line[0] != 0

    # Check rows for a winner.
    for row in board:
        if check_line(row):
            return row[0]

    # Check columns for a winner.
    for col in board.T:
        if check_line(col):
            return col[0]

    # Check diagonals for a winner.
    if check_line(board.diagonal()):
        return board.diagonal()[0]

    if check_line(np.flip(board).diagonal()):
        return np.flip(board).diagonal()[0]

    # No winner yet.
    return 0


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
        try:
            row = int(input("Player {} enter row (1-3): ".format(player))) - 1
            col = int(input("Player {} enter column (1-3): ".format(player))) - 1

            if 0 <= row < 3 and 0 <= col < 3 and board[row, col] == 0:
                return row, col

            print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")


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
    winner = check_winner(board)
    if winner != 0:
        print("Player {} wins!".format(winner))
        break

    # Check if there is a draw.
    if np.all(board != 0):
        print("Draw!")
        break

    # Switch the player number.
    player = 3 - player
