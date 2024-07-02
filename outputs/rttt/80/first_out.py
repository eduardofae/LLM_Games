def jdv():
    """
    This function implements the game jdv.

    The game is played on a 3x3 grid, and two players take turns placing their pieces in a free space.
    The first player to make a line of three adjacent pieces wins the game. If there are no more free spaces, the game is declared a draw.

    Args:
        None

    Returns:
        str: The winner of the game, or "Draw" if the game is a draw.
    """

    # Create the game board
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    # Get the names of the two players
    player1 = input("Player 1, what is your name? ")
    player2 = input("Player 2, what is your name? ")

    # Keep track of whose turn it is
    turn = 1

    # Play the game until someone wins or there are no more free spaces
    while True:
        # Get the player's move
        if turn == 1:
            move = input(f"{player1}, it's your turn. Enter your move (row, column): ")
        else:
            move = input(f"{player2}, it's your turn. Enter your move (row, column): ")

        # Check if the move is valid
        try:
            row, column = map(int, move.split(","))
            if row < 0 or row > 2 or column < 0 or column > 2 or board[row][column] != " ":
                print("Invalid move. Please try again.")
                continue
        except ValueError:
            print("Invalid move. Please try again.")
            continue

        # Place the player's piece on the board
        if turn == 1:
            board[row][column] = "X"
        else:
            board[row][column] = "O"

        # Check if the player has won
        if check_win(board):
            if turn == 1:
                return player1
            else:
                return player2

        # Check if there are no more free spaces
        if check_draw(board):
            return "Draw"

        # Switch turns
        turn = 3 - turn


def check_win(board):
    """
    This function checks if a player has won the game.

    Args:
        board: The game board.

    Returns:
        bool: True if a player has won, False otherwise.
    """

    # Check for a win horizontally
    for row in board:
        if row[0] != " " and row[0] == row[1] == row[2]:
            return True

    # Check for a win vertically
    for column in range(3):
        if board[0][column] != " " and board[0][column] == board[1][column] == board[2][column]:
            return True

    # Check for a win diagonally
    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return True
    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return True

    # No win yet
    return False


def check_draw(board):
    """
    This function checks if the game is a draw.

    Args:
        board: The game board.

    Returns:
        bool: True if the game is a draw, False otherwise.
    """

    # Check if there are any free spaces
    for row in board:
        for space in row:
            if space == " ":
                return False

    # No free spaces, so it's a draw
    return True


# Play the game
winner = jdv()

# Print the winner
print(f"The winner is {winner}!")
