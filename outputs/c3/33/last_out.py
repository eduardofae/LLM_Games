import numpy as np

# Game board
board = np.zeros((10, 10), dtype=int)

# Players
players = [1, 2]

def get_player_input(player):
    """
    Get player input for the column to place their piece.

    Args:
        player (int): The player number (1 or 2).

    Returns:
        int: The column number (0-9).
    """
    while True:
        try:
            column = int(input(f"Player {player}, choose a column (0-9): "))
            if column < 0 or column > 9:
                print("Invalid column")
                continue
            return column
        except ValueError:
            print("Invalid input")

def place_piece(player, column):
    """
    Place a piece on the game board.

    Args:
        player (int): The player number (1 or 2).
        column (int): The column number (0-9).
    """
    row = np.where(board[:, column] == 0)[0][-1]
    board[row, column] = player

def check_for_win(player):
    """
    Check if the player has won.

    Args:
        player (int): The player number (1 or 2).

    Returns:
        bool: True if the player has won, False otherwise.
    """
    return (
        np.any(np.sum(board, axis=0) == 3 * player) or
        np.any(np.sum(board, axis=1) == 3 * player) or
        np.any(np.diagonal(board) == 3 * player) or
        np.any(np.diagonal(np.flipud(board)) == 3 * player)
    )

def check_for_draw():
    """
    Check if the game is a draw.

    Returns:
        bool: True if the game is a draw, False otherwise.
    """
    return np.all(board != 0)

# Game loop
while True:
    # Get player input
    column = get_player_input(players[0])

    # Check if column is full
    if board[:, column].max() == 2:
        print("Column is full")
        continue

    # Place piece
    place_piece(players[0], column)

    # Check for win
    if check_for_win(players[0]):
        print(f"Player {players[0]} wins!")
        break

    # Check for draw
    if check_for_draw():
        print("Draw")
        break

    # Switch players
    players = players[1:] + players[:1]
