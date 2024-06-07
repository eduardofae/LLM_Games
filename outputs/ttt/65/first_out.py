import numpy as np

def jdv():
    """
    This function implements the jdv game, where 2 players take turns placing their pieces in a free space of a 3x3 grid, until one of them makes a line with 3 (horizontally, vertically or diagonally) adjacent pieces, in which case the person that made the line wins. If there are no more free spaces, the game is declared a draw.
    """

    # Create the game board
    board = np.zeros((3, 3))

    # Create a list of the players
    players = ['X', 'O']

    # Set the current player to the first player
    currentPlayer = players[0]

    # Create a list of the valid moves
    validMoves = [(i, j) for i in range(3) for j in range(3) if board[i, j] == 0]

    # Play the game until there is a winner or a draw
    while validMoves:
        # Get the current player's move
        move = input(f"Player {currentPlayer}, enter your move (row, column): ")
        move = move.split(',')
        move = (int(move[0]), int(move[1]))

        # Check if the move is valid
        if move not in validMoves:
            print("Invalid move. Please try again.")
            continue

        # Place the current player's piece on the board
        board[move[0], move[1]] = currentPlayer

        # Check if the current player has won
        if checkWin(board, currentPlayer):
            print(f"Player {currentPlayer} wins!")
            break

        # Switch to the other player
        currentPlayer = players[(players.index(currentPlayer) + 1) % 2]

        # Update the list of valid moves
        validMoves = [(i, j) for i in range(3) for j in range(3) if board[i, j] == 0]

    # If there are no more valid moves, the game is a draw
    if not validMoves:
        print("Draw!")

def checkWin(board, player):
    """
    This function checks if the given player has won the game.

    Args:
        board: The game board.
        player: The player to check.

    Returns:
        True if the player has won, False otherwise.
    """

    # Check for a win in the rows
    for row in board:
        if all(row == player):
            return True

    # Check for a win in the columns
    for col in board.T:
        if all(col == player):
            return True

    # Check for a win in the diagonals
    if all(board.diagonal() == player) or all(np.flip(board).diagonal() == player):
        return True

    # Otherwise, the player has not won
    return False

if __name__ == "__main__":
    jdv()
