import numpy as np

# Create the game board
board = np.zeros((10, 10), dtype=int)

# Create a list of the players
players = ['X', 'O']

# Set the current player to the first player
current_player = 0

# Set the game state to not finished
game_state = 'not finished'

# Main game loop
while game_state == 'not finished':
    # Get the player's move
    while True:
        try:
            move = int(input("Player {}'s turn. Enter a column (1-10): ".format(players[current_player])))
        except ValueError:
            print("Invalid move. Please enter a valid column.")
        else:
            break

    # Check if the move is valid
    if move not in range(1, 11) or board[9, move - 1] != 0:
        print("Invalid move. Please enter a valid column.")
        continue

    # Place the player's piece on the board
    for i in range(9, -1, -1):
        if board[i, move - 1] == 0:
            board[i, move - 1] = players[current_player]
            break

    # Check if the player has won
    if check_win(board, players[current_player]):
        game_state = 'win'
        print("Player {} wins!".format(players[current_player]))

    # Check if the game is a draw
    elif np.all(board != 0):
        game_state = 'draw'
        print("The game is a draw.")

    # Switch to the other player
    current_player = (current_player + 1) % 2

# Print the final game board
print(board)


def check_win(board, player):
    """
    Check if the player has won the game.

    Args:
        board (numpy.ndarray): The game board.
        player (str): The player to check for a win.

    Returns:
        bool: True if the player has won, False otherwise.
    """

    # Check for horizontal wins
    for row in board:
        if np.all(row == player):
            return True

    # Check for vertical wins
    for col in board.T:
        if np.all(col == player):
            return True

    # Check for diagonal wins
    for i in range(10):
        # Check for diagonal wins from top left to bottom right
        if np.all(board.diagonal(i) == player):
            return True

        # Check for diagonal wins from bottom left to top right
        if np.all(np.flipud(board).diagonal(i) == player):
            return True

    # No wins found
    return False
