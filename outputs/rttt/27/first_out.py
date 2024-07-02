import numpy as np

def jdv():
    """
    This function implements the jdv game, where 2 players take turns placing their pieces in a free space of a 3x3 grid, until one of them makes a line with 3 (horizontally, vertically or diagonally) adjacent pieces, in which case the person that made the line loses, and the opponent is the winner. If there are no more free spaces, the game is declared a draw.
    """

    # Create the game board
    board = np.zeros((3, 3))

    # Create a list of the players
    players = ['X', 'O']

    # Set the current player to the first player
    current_player = players[0]

    # Define the winning lines
    winning_lines = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

    # Play the game until someone wins or there are no more free spaces
    while True:
        # Get the player's move
        move = int(input("Player " + current_player + ", enter your move (1-9): ")) - 1

        # Check if the move is valid
        if board[move // 3, move % 3] != 0:
            print("Invalid move. Please try again.")
            continue

        # Place the player's piece on the board
        board[move // 3, move % 3] = current_player

        # Check if the player has won
        for winning_line in winning_lines:
            if board[winning_line[0] // 3, winning_line[0] % 3] == board[winning_line[1] // 3, winning_line[1] % 3] == board[winning_line[2] // 3, winning_line[2] % 3] != 0:
                print("Player " + current_player + " has won!")
                return

        # Check if there are no more free spaces
        if np.all(board != 0):
            print("Draw!")
            return

        # Switch to the other player
        current_player = players[(players.index(current_player) + 1) % 2]

# Play the game
jdv()
