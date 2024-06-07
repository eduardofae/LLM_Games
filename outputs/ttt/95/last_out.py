import numpy as np

def jdv():
    """
    Function to play the game jdv.

    The game is played on a 3x3 grid, and two players take turns placing their pieces in a free space.
    The first player to make a line of three adjacent pieces wins.
    If there are no more free spaces, the game is declared a draw.

    Args:
        None

    Returns:
        None
    """

    # Initialize the game board
    board = np.zeros((3, 3), dtype=int)

    # Initialize the player turn
    player_turn = 1

    # Initialize the game status
    game_status = "ongoing"

    # Main game loop
    while game_status == "ongoing":

        # Get the player's move
        try:
            row, col = map(int, input("Player {}'s turn (row, column): ".format(player_turn)).split())
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")
            continue

        # Check if the move is valid
        if not (0 <= row < 3 and 0 <= col < 3):
            print("Invalid move. Please enter a row and column between 0 and 2.")
            continue
        if board[row, col] != 0:
            print("Invalid move. That space is already occupied.")
            continue

        # Place the player's piece on the board
        board[row, col] = player_turn

        # Check if the player has won
        if check_win(board, player_turn):
            game_status = "win"
            print("Player {} wins!".format(player_turn))
        # Check if the game is a draw
        elif np.all(board != 0):
            game_status = "draw"
            print("Draw!")

        # Switch the player turn
        player_turn = 3 - player_turn

def check_win(board, player):
    """
    Function to check if the player has won.

    Args:
        board: The current game board.
        player: The player to check for a win.

    Returns:
        True if the player has won, False otherwise.
    """

    # Check for a win in the rows
    for row in range(3):
        if np.all(board[row, :] == player):
            return True

    # Check for a win in the columns
    for col in range(3):
        if np.all(board[:, col] == player):
            return True

    # Check for a win in the diagonals
    if np.all(board.diagonal() == player):
        return True
    if np.all(np.flip(board).diagonal() == player):
        return True

    # No win found
    return False

if __name__ == "__main__":
    jdv()
