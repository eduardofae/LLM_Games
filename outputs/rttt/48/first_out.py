import numpy as np

def check_winner(board):
    """Checks if there is a winner in the given board.
    Args:
        board: A 3x3 numpy array representing the game board.
    Returns:
        The player who won the game, or None if there is no winner yet.
    """
    # Check for horizontal wins
    for row in range(3):
        if np.all(board[row] == board[row][0]) and board[row][0] != 0:
            return board[row][0]

    # Check for vertical wins
    for col in range(3):
        if np.all(board[:, col] == board[0, col]) and board[0, col] != 0:
            return board[0, col]

    # Check for diagonal wins
    if np.all(np.diag(board) == board[0, 0]) and board[0, 0] != 0:
        return board[0, 0]
    if np.all(np.diag(np.flipud(board)) == board[0, 2]) and board[0, 2] != 0:
        return board[0, 2]

    # No winner yet
    return None

def check_draw(board):
    """Checks if the game is a draw.
    Args:
        board: A 3x3 numpy array representing the game board.
    Returns:
        True if the game is a draw, False otherwise.
    """
    return np.all(board != 0)

def play_jdv():
    """Plays a game of jdv."""

    # Create a 3x3 game board
    board = np.zeros((3, 3), dtype=int)

    # Get the player names
    player1 = input("Player 1 name: ")
    player2 = input("Player 2 name: ")

    # Set the current player to player 1
    current_player = 1

    # Loop until there is a winner or a draw
    while True:

        # Get the player's move
        row = int(input(f"{player1}'s turn. Row: "))
        col = int(input(f"{player1}'s turn. Column: "))

        # Check if the move is valid
        if row < 0 or row > 2 or col < 0 or col > 2 or board[row, col] != 0:
            print("Invalid move.")
            continue

        # Place the player's piece on the board
        board[row, col] = current_player

        # Check if there is a winner
        winner = check_winner(board)
        if winner is not None:
            print(f"{winner} wins!")
            break

        # Check if there is a draw
        draw = check_draw(board)
        if draw:
            print("Draw!")
            break

        # Switch to the other player
        current_player = 2 if current_player == 1 else 1


if __name__ == "__main__":
    play_jdv()
