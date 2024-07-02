import numpy as np

def jdv():
    """
    A simple command-line game of Jdv.

    The game is played on a 3x3 grid. Two players take turns placing their pieces
    in a free space on the grid. The first player to get three of their pieces in a
    row (horizontally, vertically, or diagonally) wins. If the board is filled
    up and neither player has won, the game is declared a draw.

    Args:
        None

    Returns:
        None
    """

    # Create a 3x3 grid
    board = np.zeros((3, 3))

    # Keep track of which player's turn it is
    player = 1

    # Keep track of whether the game has been won
    game_won = False

    # Keep track of the number of moves that have been made
    moves = 0

    # Game loop
    while not game_won and moves < 9:
        # Get the player's move
        row, col = input(f"Player {player}, enter your move (row, col): ").split()
        row = int(row) - 1
        col = int(col) - 1

        # Check if the move is valid
        if board[row, col] != 0:
            print("Invalid move. Please try again.")
            continue

        # Place the player's piece on the board
        board[row, col] = player

        # Check if the player has won
        if check_win(board, player):
            game_won = True
            print(f"Player {player} wins!")
        else:
            # Switch to the other player's turn
            player = 3 - player

        # Increment the number of moves
        moves += 1

    # If the game is not won, it is a draw
    if not game_won:
        print("Draw!")

def check_win(board, player):
    """
    Checks if the given player has won the game.

    Args:
        board: The game board.
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
    if np.all(board.diagonal() == player):
        return True
    if np.all(np.flip(board).diagonal() == player):
        return True

    # No win found
    return False

if __name__ == "__main__":
    jdv()
