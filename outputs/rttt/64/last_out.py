"""
jdv game.

The game is played by two players who take turns placing their pieces in a free space of a 3x3 grid.
The first player to make a line of 3 (horizontally, vertically or diagonally) adjacent pieces loses the game.
If there are no more free spaces, the game is declared a draw.
"""

import numpy as np

def create_board():
    """
    Create the game board.

    Returns:
        A numpy array representing the game board.
    """

    return np.zeros((3, 3))

def get_available_moves(board):
    """
    Get the available moves for the current player.

    Args:
        board: The game board.

    Returns:
        A list of tuples representing the available moves.
    """

    return [(i, j) for i in range(3) for j in range(3) if board[i, j] == 0]

def get_player_move(board, player):
    """
    Get the player's move.

    Args:
        board: The game board.
        player: The current player.

    Returns:
        A tuple representing the player's move.
    """

    while True:
        try:
            move = input("Player {}'s turn: ".format(player))
            move = tuple(int(x) for x in move.split(","))
            if move not in get_available_moves(board):
                print("Invalid move. Please enter a valid move.")
                continue
            return move
        except ValueError:
            print("Invalid move. Please enter a valid move.")

def update_board(board, move, player):
    """
    Update the game board with the player's move.

    Args:
        board: The game board.
        move: The player's move.
        player: The current player.
    """

    board[move] = player

def check_win(board, player):
    """
    Check if the player has won the game.

    Args:
        board: The game board.
        player: The current player.

    Returns:
        True if the player has won, False otherwise.
    """

    # Check for a horizontal win
    for i in range(3):
        if np.all(board[i] == player):
            return True

    # Check for a vertical win
    for j in range(3):
        if np.all(board[:, j] == player):
            return True

    # Check for a diagonal win
    if np.all(np.diagonal(board) == player):
        return True
    if np.all(np.diagonal(np.flipud(board)) == player):
        return True

    # No win
    return False

def main():
    """
    Play the jdv game.
    """

    # Create the game board
    board = create_board()

    # Set the current player to 1
    current_player = 1

    # Loop until the game is over
    while True:

        # Get the player's move
        move = get_player_move(board, current_player)

        # Update the board
        update_board(board, move, current_player)

        # Check if the player has won
        if check_win(board, current_player):
            print("Player {} loses.".format(current_player))
            break

        # Check if there are no more available moves
        if len(get_available_moves(board)) == 0:
            print("Draw.")
            break

        # Switch the current player
        current_player = 3 - current_player

if __name__ == "__main__":
    main()
