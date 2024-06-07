import numpy as np

def jdv():
    """
    This function implements the jdv game.
    """

    # Create the game board
    board = np.zeros((3, 3), dtype=int)

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


def is_valid_move(board, move):
    """
    This function checks if a move is valid.
    """

    # Check if the row and column are within the bounds of the board
    if move[0] < 0 or move[0] > 2 or move[1] < 0 or move[1] > 2:
        return False

    # Check if the space is already occupied
    if board[move[0], move[1]] != 0:
        return False

    return True


def has_won(board, player):
    """
    This function checks if a player has won.
    """

    # Check the rows
    for i in range(3):
        if np.all(board[i, :] == player):
            return True

    # Check the columns
    for i in range(3):
        if np.all(board[:, i] == player):
            return True

    # Check the diagonals
    if np.all(board.diagonal() == player) or np.all(np.flip(board).diagonal() == player):
        return True

    return False


if __name__ == "__main__":
    jdv()
