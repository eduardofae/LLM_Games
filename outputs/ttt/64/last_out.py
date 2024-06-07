import numpy as np

# Initialize the game board
board = np.zeros((3, 3), dtype=int)

# Define the player symbols
player1 = "X"
player2 = "O"

# Define the game state
game_over = False
winner = None

# Define functions to check if a move is valid, if a player has won, and to reset the game board
def is_valid_move(board, row, col):
    """
    Check if a move is valid.

    Args:
        board (np.ndarray): The game board.
        row (int): The row of the move.
        col (int): The column of the move.

    Returns:
        bool: True if the move is valid, False otherwise.
    """
    return (row >= 0 and row < board.shape[0] and
            col >= 0 and col < board.shape[1] and
            board[row, col] == 0)

def has_won(board, player):
    """
    Check if a player has won.

    Args:
        board (np.ndarray): The game board.
        player (str): The player symbol (X or O).

    Returns:
        bool: True if the player has won, False otherwise.
    """
    # Check rows
    for i in range(board.shape[0]):
        if np.all(board[i, :] == player):
            return True

    # Check columns
    for j in range(board.shape[1]):
        if np.all(board[:, j] == player):
            return True

    # Check diagonals
    if np.all(board.diagonal() == player):
        return True

    if np.all(np.flip(board).diagonal() == player):
        return True

    return False

def reset_board():
    """
    Reset the game board to its initial state.
    """
    board[:] = 0

# Define a function to get the board size from the user
def get_board_size():
    """
    Get the board size from the user.

    Returns:
        int: The board size.
    """
    while True:
        try:
            board_size = int(input("Enter the board size (e.g., 3 for a 3x3 board): "))
            if board_size < 3 or board_size > 5:
                print("Invalid board size. Please enter a value between 3 and 5.")
                continue
            return board_size
        except ValueError:
            print("Invalid input. Please enter an integer.")

# Define a function to get the player symbols from the user
def get_player_symbols():
    """
    Get the player symbols from the user.

    Returns:
        tuple: A tuple containing the player symbols (e.g., ("X", "O")).
    """
    while True:
        try:
            player1_symbol = input("Enter player 1's symbol: ")
            player2_symbol = input("Enter player 2's symbol: ")
            if player1_symbol == player2_symbol:
                print("Player symbols must be different.")
                continue
            return player1_symbol, player2_symbol
        except ValueError:
            print("Invalid input. Please enter a single character.")

# Get the board size from the user
board_size = get_board_size()

# Create a game board with the specified size
board = np.zeros((board_size, board_size), dtype=int)

# Get the player symbols from the user
player1, player2 = get_player_symbols()

# Start the game loop
while not game_over:
    # Get the current player's move
    if player1 is not None:
        try:
            row, col = map(int, input("Player 1's move (row, col): ").split())
        except ValueError:
            print("Invalid input. Please enter two integers separated by a comma.")
            continue

        # Check if the move is valid
        if not is_valid_move(board, row, col):
            print("Invalid move. Please try again.")
            continue
    else:
        try:
            row, col = map(int, input("Player 2's move (row, col): ").split())
        except ValueError:
            print("Invalid input. Please enter two integers separated by a comma.")
            continue

        # Check if the move is valid
        if not is_valid_move(board, row, col):
            print("Invalid move. Please try again.")
            continue

    # Place the player's piece on the board
    board[row, col] = player1 if player1 is not None else player2

    # Check if the player has won
    if has_won(board, player1):
        winner = player1
        game_over = True
    elif has_won(board, player2):
        winner = player2
        game_over = True

    # Check if the game is a draw
    if not np.any(board == 0):
        winner = "draw"
        game_over = True

    # Swap the player symbols
    player1, player2 = player2, player1

# Print the game board
print_board(board)

# Print the winner
if winner is not None:
    print(f"{winner} wins!")
else:
    print("Game over. It's a draw.")

# Ask if the players want to play again
play_again = input("Do you want to play again? (y/n): ")
if play_again == "y":
    reset_board()
    game_over = False
    winner = None
