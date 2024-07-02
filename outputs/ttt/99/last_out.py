import numpy as np

def create_board():
    """
    Creates a new 3x3 game board.

    Returns:
        A 3x3 numpy array representing the game board.
    """

    return np.array([[' ', ' ', ' '],
                       [' ', ' ', ' '],
                       [' ', ' ', ' ']])


def print_board(board):
    """
    Prints the current state of the game board.

    Args:
        board: The current state of the game board.
    """

    for row in board:
        print(' '.join(row))


def get_player_input(player_name):
    """
    Gets the player's move.

    Args:
        player_name: The name of the player whose turn it is.

    Returns:
        A tuple representing the player's move (row, column).
    """

    while True:
        try:
            move = input(f"{player_name}, enter your move (row, column): ")
            row, column = map(int, move.split(","))
            if 0 <= row <= 2 and 0 <= column <= 2:
                return row, column
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print("Invalid move. Please try again.")


def check_for_win(board):
    """
    Checks if there is a winner on the board.

    Args:
        board: The current state of the game board.

    Returns:
        True if there is a winner, False otherwise.
    """

    # Check for a horizontal win
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != ' ':
            return True

    # Check for a vertical win
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] and board[0][column] != ' ':
            return True

    # Check for a diagonal win
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True

    # No winner yet
    return False


def check_for_draw(board):
    """
    Checks if the game is a draw.

    Args:
        board: The current state of the game board.

    Returns:
        True if the game is a draw, False otherwise.
    """

    # Check if there are any empty spaces on the board
    for row in range(3):
        for column in range(3):
            if board[row][column] == ' ':
                return False

    # No empty spaces, so the game is a draw
    return True


def play_jdv():
    """
    Plays the jdv game.
    """

    # Create a new game board
    board = create_board()

    # Get the names of the two players
    player1_name = input("Player 1, enter your name: ")
    player2_name = input("Player 2, enter your name: ")

    # Determine who will play first
    player1_turn = True

    # Loop until the game is over
    while True:
        # Print the current state of the game board
        print_board(board)

        # Get the current player's move
        if player1_turn:
            row, column = get_player_input(player1_name)
        else:
            row, column = get_player_input(player2_name)

        # Place the player's piece on the board
        board[row][column] = 'X' if player1_turn else 'O'

        # Check if the player has won
        if check_for_win(board):
            print(f"{player1_name if player1_turn else player2_name} wins!")
            break

        # Check if the game is a draw
        if check_for_draw(board):
            print("The game is a draw.")
            break

        # Switch turns
        player1_turn = not player1_turn


if __name__ == "__main__":
    play_jdv()
