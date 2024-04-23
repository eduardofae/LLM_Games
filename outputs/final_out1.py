import numpy as np

def game():
    # Initialize the game board
    board = np.zeros((3, 3))

    # Players' turn
    player = 1
    game_state = "ongoing"

    # Game loop
    while game_state == "ongoing":
        # Print the game board
        print_board(board)

        # Get the player's move
        try:
            row, col = map(int, input("Enter your move (row, col): ").split())
            if not (0 <= row < 3 and 0 <= col < 3):
                raise ValueError("Invalid move. Please enter a valid row and column.")
            if board[row, col] != 0:
                raise ValueError("Invalid move. The space is already occupied.")
        except ValueError:
            print("Invalid input. Please enter integers within the bounds of the game board.")
            continue

        # Place the player's piece on the board
        board[row, col] = player

        # Check if the player has won
        if check_win(board, player):
            game_state = "won"
            print("Player", player, "has won!")

        # Check if the game is a draw
        elif np.all(board != 0):
            game_state = "drawn"
            print("The game is a draw.")

        # Switch player
        player = 3 - player

def check_win(board, player):
    # Iterate over rows, columns, and diagonals to check for wins
    for i in range(3):
        # Check for horizontal win
        if np.all(board[i, :] == player):
            return True

        # Check for vertical win
        if np.all(board[:, i] == player):
            return True

    # Check for diagonal wins
    if np.all(board.diagonal() == player):
        return True
    if np.all(np.flip(board).diagonal() == player):
        return True

    # No win yet
    return False

def print_board(board):
    # Print the game board with visual representation
    for row in board:
        print(" | ".join(["_" if cell == 0 else ("X" if cell == 1 else "O") for cell in row]))

# Start the game
print("Welcome to JdV!")
print("Instructions: Two players take turns placing their pieces on a 3x3 grid. The first player to make a line of three adjacent pieces (horizontally, vertically, or diagonally) loses, and the other player wins. If there are no more free spaces, the game is a draw.")
game()
