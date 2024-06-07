import numpy as np

# Create the game board
board = np.zeros((3, 3))

# Define the players' symbols
player1_symbol = 'X'
player2_symbol = 'O'

# Keep track of the current player
current_player = player1_symbol

# Keep track of the game status
game_status = 'ongoing'

# Main game loop
while game_status == 'ongoing':

    # Print the game board
    print(board)

    # Get the player's move
    row, col = map(int, input(f"Player {current_player}, enter your move (row, col): ").split())

    # Check if the move is valid
    if board[row, col] != 0:
        print("Invalid move. Please try again.")
        continue

    # Place the player's piece on the board
    board[row, col] = current_player

    # Check if the player has won
    if check_win(board, current_player):
        game_status = 'over'
        print(f"Player {current_player} wins!")
        break

    # Check if the game is a draw
    if np.all(board != 0):
        game_status = 'draw'
        print("The game is a draw!")
        break

    # Switch the current player
    current_player = player2_symbol if current_player == player1_symbol else player1_symbol

# Print the final game board
print(board)

# Print the game status
print(game_status)


def check_win(board, player):
    """
    Checks if the player has won the game.

    Args:
        board: The game board.
        player: The player to check for a win.

    Returns:
        True if the player has won, False otherwise.
    """

    # Check for a win in each row
    for row in range(3):
        if np.all(board[row, :] == player):
            return True

    # Check for a win in each column
    for col in range(3):
        if np.all(board[:, col] == player):
            return True

    # Check for a win in each diagonal
    if np.all(board.diagonal() == player):
        return True
    if np.all(np.flip(board).diagonal() == player):
        return True

    # No win found
    return False
