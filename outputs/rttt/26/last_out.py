import numpy as np

def jdv():
    """
    This function implements the game jdv.

    The game is played on a 3x3 grid, and two players take turns placing their pieces in a free space.
    The first player to make a line of three adjacent pieces wins the game.
    If there are no more free spaces, the game is declared a draw.

    The function returns the winner of the game, or None if the game is a draw.
    """

    # Create the game board
    board = np.zeros((3, 3))

    # Create a list of the possible winning lines
    winning_lines = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]

    # Keep track of the current player
    player = 1

    # Main game loop
    while True:
        # Get the player's move
        try:
            move = tuple(map(int, input("Player {}'s turn: ".format(player)).split(",")))
        except ValueError:
            print("Invalid input. Please enter two integers separated by a comma.")
            continue

        # Check if the move is valid
        if not (0 <= move[0] < 3 and 0 <= move[1] < 3 and board[move] == 0):
            print("Invalid move. Please enter a free space.")
            continue

        # Place the player's piece on the board
        board[move] = player

        # Check if the player has won
        for line in winning_lines:
            if all(board[x] == player for x in line):
                return player

        # Check if the game is a draw
        if np.all(board != 0):
            return None

        # Switch to the other player
        player = 3 - player

if __name__ == "__main__":
    winner = jdv()

    if winner is None:
        print("Draw")
    else:
        print("Player {} wins".format(winner))
