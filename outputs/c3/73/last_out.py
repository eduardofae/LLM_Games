import numpy as np

def check_winner(board):
    """
    Checks if there is a winner in the given board.

    Args:
        board: A 10x10 numpy array representing the game board.

    Returns:
        The player number of the winner, or 0 if there is no winner.
    """

    # Check for horizontal wins.
    for row in range(10):
        for col in range(7):
            if board[row, col] != 0 and board[row, col] == board[row, col+1] and board[row, col] == board[row, col+2]:
                return board[row, col]

    # Check for vertical wins.
    for col in range(10):
        for row in range(7):
            if board[row, col] != 0 and board[row, col] == board[row+1, col] and board[row, col] == board[row+2, col]:
                return board[row, col]

    # Check for diagonal wins.
    for row in range(7):
        for col in range(7):
            if board[row, col] != 0 and board[row, col] == board[row+1, col+1] and board[row, col] == board[row+2, col+2]:
                return board[row, col]

    for row in range(7):
        for col in range(3, 10):
            if board[row, col] != 0 and board[row, col] == board[row+1, col-1] and board[row, col] == board[row+2, col-2]:
                return board[row, col]

    # No winner yet.
    return 0


def print_board(board):
    """
    Prints the given board to the console.

    Args:
        board: A 10x10 numpy array representing the game board.
    """

    for row in range(10):
        for col in range(10):
            print(board[row, col], end=" ")
        print()


def get_player_input(player, board):
    """
    Gets the column where the given player wants to place their piece.

    Args:
        player: The player number (1 or 2).
        board: A 10x10 numpy array representing the game board.

    Returns:
        The column number where the player wants to place their piece.
    """

    while True:
        try:
            col = int(input("Player {}'s turn. Enter a column number (0-9): ".format(player)))
            if col < 0 or col > 9:
                raise ValueError
            if board[0, col] != 0:
                print("Column {} is full. Please choose another column.".format(col))
                continue
            break
        except ValueError:
            print("Invalid column number. Please enter a number between 0 and 9.")

    return col


def main():
    """
    Runs the main game loop.
    """

    # Create a new game board.
    board = np.zeros((10, 10), dtype=int)

    # Set the current player to 1.
    current_player = 1

    # Game loop.
    while True:
        # Get the column where the current player wants to place their piece.
        col = get_player_input(current_player, board)

        # Place the current player's piece in the lowest free space of the chosen column.
        for row in range(9, -1, -1):
            if board[row, col] == 0:
                board[row, col] = current_player
                break

        # Print the updated board.
        print_board(board)

        # Check if there is a winner.
        winner = check_winner(board)
        if winner != 0:
            print("Player {} wins!".format(winner))
            break

        # Check if there are no more free spaces.
        if np.all(board != 0):
            print("Draw!")
            break

        # Switch to the other player.
        current_player = 3 - current_player


if __name__ == "__main__":
    main()
