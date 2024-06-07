import copy

def create_board():
    """Creates a 3x3 game board."""
    board = [[" ", " ", " "] for _ in range(3)]
    return board

def print_board(board):
    """Prints the game board."""
    print("   0 1 2")
    for row in range(3):
        print(f"{row}  {' '.join(board[row])}")

def check_winner(board):
    """Checks if there is a winner."""
    # Check rows
    for row in board:
        if all(x == row[0] for x in row) and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if all(board[0][col] == board[i][col] for i in range(3)) and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if all(board[i][i] == board[0][0] for i in range(3)) and board[0][0] != " ":
        return board[0][0]

    if all(board[i][2-i] == board[0][2] for i in range(3)) and board[0][2] != " ":
        return board[0][2]

    return False

def get_available_moves(board):
    """Gets the available moves on the game board."""
    available_moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                available_moves.append((i, j))
    return available_moves

def place_piece(board, player, row, col):
    """Places a player's piece on the game board."""
    board[row][col] = player

def play_game():
    """Plays the game."""
    # Create the game board
    board = create_board()

    # Set the current player
    current_player = "X"

    # Play the game until there is a winner or a draw
    while True:
        # Print the game board
        print_board(board)

        # Get the available moves
        available_moves = get_available_moves(board)

        # Check if there are no more available moves
        if not available_moves:
            print("Draw")
            break

        # Get the player's move
        while True:
            try:
                move = input(f"{current_player}'s turn. Enter row and column (e.g. 1 2): ")
                row, col = map(int, move.split())
                if (row, col) in available_moves:
                    break
                else:
                    print("Invalid move. Please enter a row and column that are within the bounds of the game board and that do not contain another player's piece.")
            except ValueError:
                print("Invalid input. Please enter two integers separated by a space.")
                continue

        # Place the player's piece on the game board
        place_piece(board, current_player, row, col)

        # Check if there is a winner
        winner = check_winner(board)
        if winner:
            print(f"{winner} wins!")
            break

        # Change the current player
        current_player = "O" if current_player == "X" else "X"

    # Ask the user if they want to play again
    while True:
        play_again = input("Play again? (y/n): ")
        if play_again == "y":
            play_game()
        elif play_again == "n":
            break
        else:
            print("Invalid input. Please enter 'y' to play again or 'n' to quit.")

if __name__ == "__main__":
    play_game()
