def jdv():
    """
    This function implements the jdv game.
    """

    # Create the game board.
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    # Get the names of the two players.
    player1 = input("Player 1, enter your name: ")
    player2 = input("Player 2, enter your name: ")

    # Determine who goes first.
    first_player = input("Who goes first? (1 or 2): ")

    # Keep track of the current player.
    current_player = first_player

    # Keep track of the number of moves that have been made.
    num_moves = 0

    # Play the game until someone wins or there is a draw.
    while True:
        # Get the move from the current player.
        move = input("Player {}, enter your move (row, column): ".format(current_player))

        # Split the move into the row and column.
        row, column = move.split(",")

        # Convert the row and column to integers.
        row = int(row)
        column = int(column)

        # Check if the move is valid.
        if not (0 <= row < 3 and 0 <= column < 3 and board[row][column] == " "):
            print("Invalid move. Please try again.")
            continue

        # Make the move.
        board[row][column] = current_player

        # Increment the number of moves.
        num_moves += 1

        # Check if the game is over.
        if check_winner(board):
            print("Player {} wins!".format(current_player))
            break
        elif num_moves == 9:
            print("Draw!")
            break

        # Switch to the other player.
        if current_player == "1":
            current_player = "2"
        else:
            current_player = "1"


def check_winner(board):
    """
    This function checks if there is a winner in the given board.

    Args:
        board: The game board.

    Returns:
        True if there is a winner, False otherwise.
    """

    # Check for a winner in each row.
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return True

    # Check for a winner in each column.
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check for a winner in each diagonal.
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    # No winner yet.
    return False


if __name__ == "__main__":
    jdv()
