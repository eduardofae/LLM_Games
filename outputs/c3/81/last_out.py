import numpy as np

def create_board():
    """Create a 10x10 game board."""
    board = np.zeros((10, 10))
    return board

def place_piece(board, player, column):
    """Place a piece on the game board.

    Args:
        board: The game board.
        player: The player who is placing the piece.
        column: The column in which to place the piece.
    """
    # Find the lowest free space in the column.
    for row in range(9, -1, -1):
        if board[row][column] == 0:
            board[row][column] = player
            return

def check_for_win(board):
    """Check if there is a winner.

    Args:
        board: The game board.

    Returns:
        True if there is a winner, False otherwise.
    """
    # Check for horizontal wins.
    for row in range(10):
        for col in range(7):
            if board[row][col] != 0 and \
               board[row][col] == board[row][col+1] and \
               board[row][col] == board[row][col+2]:
                return True

    # Check for vertical wins.
    for row in range(7):
        for col in range(10):
            if board[row][col] != 0 and \
               board[row][col] == board[row+1][col] and \
               board[row][col] == board[row+2][col]:
                return True

    # Check for diagonal wins.
    for row in range(7):
        for col in range(7):
            if board[row][col] != 0 and \
               board[row][col] == board[row+1][col+1] and \
               board[row][col] == board[row+2][col+2]:
                return True

    for row in range(3, 10):
        for col in range(7):
            if board[row][col] != 0 and \
               board[row][col] == board[row-1][col+1] and \
               board[row][col] == board[row-2][col+2]:
                return True

    # No winner yet.
    return False

def print_board(board):
    """Print the game board."""
    for row in range(10):
        for col in range(10):
            if board[row][col] == 0:
                print(" ", end=" ")
            elif board[row][col] == 1:
                print("X", end=" ")
            else:
                print("O", end=" ")
        print()

def get_player_move(board):
    """Get the player's move.

    Args:
        board: The game board.

    Returns:
        The column in which the player wants to place their piece.
    """
    while True:
        try:
            column = int(input("Player {}'s turn. Choose a column (0-9): ".format(player)))
            if column < 0 or column > 9:
                print("Invalid column. Please choose a column between 0 and 9.")
            elif board[0][column] != 0:
                print("That column is full. Please choose another column.")
            else:
                return column
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 9.")

def main():
    """Play the game."""
    board = create_board()
    player = 1
    num_moves = 0

    while True:
        # Print the board.
        print_board(board)

        # Get the player's move.
        column = get_player_move(board)

        # Place the piece on the board.
        place_piece(board, player, column)

        # Check for a winner.
        if check_for_win(board):
            print("Player {} wins!".format(player))
            break

        # Check for a draw.
        num_moves += 1
        if num_moves == 100:
            print("Draw!")
            break

        # Switch players.
        player = 3 - player

if __name__ == "__main__":
    main()
