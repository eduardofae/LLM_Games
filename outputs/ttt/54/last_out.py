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
        while True:
            move = input(f"Player {player}, enter your move (row, col): ").split()
            if len(move) != 2 or not move[0].isdigit() or not move[1].isdigit():
                print("Invalid move. Please try again.")
            else:
                row = int(move[0]) - 1
                col = int(move[1]) - 1
                break

        # Check if the move is valid
        if not is_valid_move(board, row, col):
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

def is_valid_move(board, row, col):
    """
    Checks if the given move is valid.

    Args:
        board: The game board.
        row: The row of the move.
        col: The column of the move.

    Returns:
        True if the move is valid, False otherwise.
    """

    if row < 0 or row > 2 or col < 0 or col > 2:
        return False
    if board[row, col] != 0:
        return False
    return True

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
