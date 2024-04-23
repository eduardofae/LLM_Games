import numpy as np

def game():
    # Initialize the game board
    board = np.zeros((3, 3))

    # Players' turn
    player = 1

    # Game loop
    while True:
        # Print the game board
        print(board)

        # Get the player's move
        row, col = map(int, input("Enter your move (row, col): ").split())

        # Check if the move is valid
        if board[row, col] != 0:
            print("Invalid move. Please try again.")
            continue

        # Place the player's piece on the board
        board[row, col] = player

        # Check if the player has won
        if check_win(board, player):
            print("Player", player, "has won!")
            break

        # Check if the game is a draw
        if np.all(board != 0):
            print("The game is a draw.")
            break

        # Switch player
        player = 3 - player

def check_win(board, player):
    # Check for horizontal win
    for row in range(3):
        if np.all(board[row, :] == player):
            return True

    # Check for vertical win
    for col in range(3):
        if np.all(board[:, col] == player):
            return True

    # Check for diagonal win
    if np.all(board.diagonal() == player):
        return True
    if np.all(np.flip(board).diagonal() == player):
        return True

    # No win yet
    return False

# Start the game
game()