import numpy as np

def jdv(board_size=3):
    """
    This function implements the jdv game.

    Args:
        board_size (int): The size of the game board.
    """

    # Create the game board
    board = np.zeros((board_size, board_size), dtype=int)

    # Create a list of the players
    players = ['X', 'O']

    # Set the current player
    current_player = 0

    # Set the status of the game to ongoing
    game_status = 'ongoing'

    # Loop until the game is over
    while game_status == 'ongoing':

        # Get the move from the current player
        move = input("Player {}: Enter your move (row, column): ".format(players[current_player]))

        # Check if the move is valid
        if not is_valid_move(board, move):
            print("Invalid move. Please try again.")
            continue

        # Place the piece on the board
        board[move[0], move[1]] = players[current_player]

        # Check if the current player has won
        if has_won(board, players[current_player]):
            game_status = 'won'
            winner = players[current_player]
        
        # Check if the game is a draw
        elif np.all(board != 0):
            game_status = 'draw'

        # Switch to the other player
        current_player = (current_player + 1) % 2

    # Print the game board
    print(board)

    # Print the winner or draw message
    if game_status == 'won':
        print("Player {} has won!".format(winner))
    else:
        print("The game is a draw.")

    # Ask the player if they want to play again
    play_again = input("Do you want to play again? (y/n) ")
    if play_again == 'y':
        jdv(board_size)


def is_valid_move(board, move):
    """
    This function checks if a move is valid.

    Args:
        board (numpy.ndarray): The game board.
        move (tuple): The move to check.

    Returns:
        bool: True if the move is valid, False otherwise.
    """

    # Check if the row and column are within the bounds of the board
    if move[0] < 0 or move[0] >= board.shape[0] or move[1] < 0 or move[1] >= board.shape[1]:
        return False

    # Check if the space is already occupied
    if board[move[0], move[1]] != 0:
        return False

    return True


def has_won(board, player):
    """
    This function checks if a player has won.

    Args:
        board (numpy.ndarray): The game board.
        player (str): The player to check.

    Returns:
        bool: True if the player has won, False otherwise.
    """

    # Check the rows
    for i in range(board.shape[0]):
        if np.all(board[i, :] == player):
            return True

    # Check the columns
    for i in range(board.shape[1]):
        if np.all(board[:, i] == player):
            return True

    # Check the diagonals
    if np.all(board.diagonal() == player) or np.all(np.flip(board).diagonal() == player):
        return True

    return False


if __name__ == "__main__":
    jdv()
