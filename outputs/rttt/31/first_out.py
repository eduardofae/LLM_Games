import copy

def create_board():
    """Creates a 3x3 game board."""
    board = [[" ", " ", " "] for _ in range(3)]
    return board

def print_board(board):
    """Prints the game board."""
    for row in board:
        print(" ".join(row))

def check_winner(board):
    """Checks if there is a winner."""
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return False

def get_free_spaces(board):
    """Gets the free spaces on the game board."""
    free_spaces = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                free_spaces.append((i, j))
    return free_spaces

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

        # Get the free spaces
        free_spaces = get_free_spaces(board)

        # Check if there are no more free spaces
        if not free_spaces:
            print("Draw")
            break

        # Get the player's move
        move = input(f"{current_player}'s turn. Enter row and column: ")
        row, col = map(int, move.split())

        # Check if the move is valid
        if (row, col) not in free_spaces:
            print("Invalid move")
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

if __name__ == "__main__":
    play_game()
