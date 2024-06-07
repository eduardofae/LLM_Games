import numpy as np

def create_board():
    """Creates a 3x3 grid."""
    board = np.zeros((3, 3))
    return board

def print_board(board):
    """Prints the board."""
    for row in board:
        for cell in row:
            if cell == 0:
                print("-", end=" ")
            elif cell == 1:
                print("X", end=" ")
            else:
                print("O", end=" ")
        print()

def check_win(board):
    """Checks if there is a winner."""
    # Check if there is a winner in rows
    for row in board:
        if (row == [1, 1, 1]).all() or (row == [2, 2, 2]).all():
            return True

    # Check if there is a winner in columns
    for col in range(3):
        if (board[:, col] == [1, 1, 1]).all() or (board[:, col] == [2, 2, 2]).all():
            return True

    # Check if there is a winner in diagonals
    if (board.diagonal() == [1, 1, 1]).all() or (board.diagonal() == [2, 2, 2]).all()):
        return True
    if (np.flip(board).diagonal() == [1, 1, 1]).all() or (np.flip(board).diagonal() == [2, 2, 2]).all()):
        return True

    # Check if there is a draw
    if (board == 0).any():
        return False

    return True

def get_player_move(board):
    """Gets the player's move."""
    while True:
        move = input("Enter your move (row, column): ")
        row, col = map(int, move.split(","))
        if row < 0 or row > 2 or col < 0 or col > 2:
            print("Invalid move. Please enter a valid move.")
        elif board[row, col] != 0:
            print("That space is already taken. Please enter a valid move.")
        else:
            return row, col

def play_game():
    """Plays the game."""
    board = create_board()
    player = 1  # 1 is X, 2 is O

    while True:
        print_board(board)
        row, col = get_player_move(board)
        board[row, col] = player
        if check_win(board):
            print(f"Player {player} wins!")
            break
        player = 3 - player

if __name__ == "__main__":
    play_game()
