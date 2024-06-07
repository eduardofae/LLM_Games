import numpy as np

def jdv():
    """
    A simple game of jdv.

    The game is played on a 3x3 grid. Two players take turns placing their pieces in a free space of the grid.
    The first player to make a line of three adjacent pieces (horizontally, vertically, or diagonally) wins.
    If there are no more free spaces, the game is declared a draw.

    Args:
        None

    Returns:
        None
    """

    # Create the game board.
    board = np.zeros((3, 3), dtype=int)

    # Create a list of the possible winning lines.
    winning_lines = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
    ]

    # Create a list of the players.
    players = [1, 2]

    # Start the game.
    while True:
        # Get the current player.
        player = players[0]

        # Get the current player's move.
        move = input("Player {}'s move (row, column): ".format(player))
        row, column = map(int, move.split(","))

        # Check if the move is valid.
        if not (0 <= row < 3 and 0 <= column < 3 and board[row, column] == 0):
            print("Invalid move. Try again.")
            continue

        # Place the player's piece on the board.
        board[row, column] = player

        # Check if the player has won.
        for winning_line in winning_lines:
            if all(board[winning_line[0][0], winning_line[0][1]] == player and board[winning_line[1][0], winning_line[1][1]] == player and board[winning_line[2][0], winning_line[2][1]] == player):
                print("Player {} wins!".format(player))
                return

        # Check if the game is a draw.
        if np.all(board != 0):
            print("It's a draw!")
            return

        # Switch to the other player.
        players = players[1:] + players[:1]


if __name__ == "__main__":
    jdv()
