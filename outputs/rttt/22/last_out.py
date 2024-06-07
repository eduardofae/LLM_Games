import numpy as np

def jdv():
    # Create a 3x3 game board
    board = np.zeros((3, 3), dtype=int)

    # Player 1 is 'X' and Player 2 is 'O'
    player1 = 'X'
    player2 = 'O'

    # Keep track of whose turn it is
    turn = 0

    # Main game loop
    while True:
        # Display the game board
        print_board(board)

        # Get the current player's move
        move = get_player_move(board, turn)

        # Check if the move is valid
        if not is_valid_move(board, move):
            print("Invalid move. Try again.")
            continue

        # Place the player's piece on the game board
        board[move[0], move[1]] = turn

        # Check if the player has won
        if check_win(board, turn):
            print(f"Player {turn} wins!")
            break

        # Check if there are no more free spaces
        if np.all(board != 0):
            print("Draw!")
            break

        # Switch turns
        turn = (turn + 1) % 2

def get_player_move(board, turn):
    while True:
        try:
            # Get the player's move
            row, col = input(f"Player {turn}, enter your move (row, col): ").split()

            # Check if the move is valid
            if not is_valid_move(board, (int(row), int(col))):
                raise ValueError("Invalid move.")

            # Return the player's move
            return int(row), int(col)
        except ValueError:
            print("Invalid move. Try again.")

def is_valid_move(board, move):
    # Check if the move is within the bounds of the game board
    if not (0 <= move[0] < 3 and 0 <= move[1] < 3):
        return False

    # Check if the move is on a free space
    if board[move[0], move[1]] != 0:
        return False

    # The move is valid
    return True

def check_win(board, turn):
    # Check for horizontal wins
    for row in range(3):
        if np.all(board[row, :] == turn):
            return True

    # Check for vertical wins
    for col in range(3):
        if np.all(board[:, col] == turn):
            return True

    # Check for diagonal wins
    if np.all(board.diagonal() == turn) or np.all(np.flip(board).diagonal() == turn):
        return True

    # No win
    return False

def print_board(board):
    for row in range(3):
        for col in range(3):
            if board[row, col] == 0:
                print(' ', end=' ')
            else:
                print(board[row, col], end=' ')
        print()

if __name__ == "__main__":
    jdv()
