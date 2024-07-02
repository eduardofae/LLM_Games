def jdv():
    """
    This function implements the "jdv" game, where two players take turns placing their pieces in a free space of a 3x3 grid,
    until one of them makes a line with 3 (horizontally, vertically or diagonally) adjacent pieces, in which case the person
    that made the line loses, and the opponent is the winner. If there are no more free spaces, the game is declared a draw.
    """

    # Create the game board
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]

    # Create a list of the possible winning combinations
    winning_combinations = [[(0, 0), (0, 1), (0, 2)],
                            [(1, 0), (1, 1), (1, 2)],
                            [(2, 0), (2, 1), (2, 2)],
                            [(0, 0), (1, 0), (2, 0)],
                            [(0, 1), (1, 1), (2, 1)],
                            [(0, 2), (1, 2), (2, 2)],
                            [(0, 0), (1, 1), (2, 2)],
                            [(0, 2), (1, 1), (2, 0)]]

    # Create a variable to keep track of the current player
    current_player = 'X'

    # Create a variable to keep track of the number of moves made
    num_moves = 0

    # Main game loop
    while True:

        # Print the game board
        print_board(board)

        # Get the player's move
        move = get_move(current_player)

        # Place the player's piece on the board
        board[move[0]][move[1]] = current_player

        # Increment the number of moves made
        num_moves += 1

        # Check if the player has won
        if check_win(board, current_player):
            print(f"{current_player} wins!")
            break

        # Check if the game is a draw
        if num_moves == 9:
            print("Draw!")
            break

        # Switch to the other player
        current_player = 'O' if current_player == 'X' else 'X'


def print_board(board):
    """
    This function prints the current state of the game board.
    """

    for row in board:
        for space in row:
            print(space, end=' ')
        print()


def get_move(player):
    """
    This function gets the player's move.
    """

    while True:
        try:
            move = input(f"{player}'s turn. Enter your move (row, column): ")
            move = [int(x) for x in move.split(',')]
            if move[0] < 0 or move[0] > 2 or move[1] < 0 or move[1] > 2:
                raise ValueError
            if board[move[0]][move[1]] != ' ':
                raise ValueError
            return move
        except ValueError:
            print("Invalid move. Please enter a valid move.")


def check_win(board, player):
    """
    This function checks if the player has won.
    """

    for combination in winning_combinations:
        if all([board[x[0]][x[1]] == player for x in combination]):
            return True

    return False


if __name__ == "__main__":
    jdv()
