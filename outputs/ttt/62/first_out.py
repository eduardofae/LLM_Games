# Initialize the game board
board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

# Initialize the player's turn
turn = 'X'

# Create a function to check if a player has won
def check_win(board, player):
    # Check for horizontal wins
    for row in board:
        if all(row[i] == player for i in range(3)):
            return True

    # Check for vertical wins
    for col in range(3):
        if all(board[i][col] == player for i in range(3)):
            return True

    # Check for diagonal wins
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    # Otherwise, return False
    return False

# Create a function to print the game board
def print_board(board):
    for row in board:
        print(' '.join(row))

# Main game loop
while True:
    # Print the game board
    print_board(board)

    # Get the player's move
    move = input(f"{turn}'s turn. Enter a row and column (e.g. 1 2): ")

    # Parse the player's move
    row, col = map(int, move.split())

    # Check if the move is valid
    if row < 1 or row > 3 or col < 1 or col > 3 or board[row - 1][col - 1] != ' ':
        print("Invalid move. Please try again.")
        continue

    # Place the player's piece on the board
    board[row - 1][col - 1] = turn

    # Check if a player has won
    if check_win(board, turn):
        # Print the winning board
        print_board(board)

        # Print the winning player
        print(f"{turn} wins!")

        # Break out of the game loop
        break

    # Check if the game is a draw
    if all(all(space != ' ' for space in row) for row in board):
        # Print the draw board
        print_board(board)

        # Print that the game is a draw
        print("Draw!")

        # Break out of the game loop
        break

    # Switch to the other player's turn
    turn = 'X' if turn == 'O' else 'O'
