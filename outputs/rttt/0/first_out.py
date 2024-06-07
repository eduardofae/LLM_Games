def jdv():
    # Initialize the game board
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]

    # Initialize the players' turns
    player1_turn = True
    player2_turn = False

    # Initialize the game status
    game_over = False
    draw = False

    # Game loop
    while not game_over:
        # Print the game board
        print_board(board)

        # Get the player's input
        if player1_turn:
            move = input("Player 1, enter your move (row, column): ")
        else:
            move = input("Player 2, enter your move (row, column): ")

        # Check if the input is valid
        if not is_valid_move(move):
            print("Invalid move. Please enter a valid move.")
            continue

        # Convert the input to row and column indices
        row, column = move.split(',')
        row = int(row) - 1
        column = int(column) - 1

        # Check if the space is free
        if board[row][column] != ' ':
            print("Space already occupied. Please enter a valid move.")
            continue

        # Place the player's piece in the space
        if player1_turn:
            board[row][column] = 'X'
        else:
            board[row][column] = 'O'

        # Check if the player has won
        if has_won(board):
            if player1_turn:
                print("Player 1 wins!")
            else:
                print("Player 2 wins!")
            game_over = True

        # Check if the game is a draw
        if is_draw(board):
            print("Draw!")
            game_over = True

        # Switch the players' turns
        player1_turn = not player1_turn
        player2_turn = not player2_turn

# Function to print the game board
def print_board(board):
    for row in board:
        print(' '.join(row))

# Function to check if a move is valid
def is_valid_move(move):
    # Check if the move is in the format "row, column"
    if not isinstance(move, str) or not ',' in move:
        return False

    # Convert the move to row and column indices
    row, column = move.split(',')
    row = int(row) - 1
    column = int(column) - 1

    # Check if the row and column indices are within the range
    if row < 0 or row > 2 or column < 0 or column > 2:
        return False

    return True

# Function to check if a player has won
def has_won(board):
    # Check for horizontal wins
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return True

    # Check for vertical wins
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] != ' ':
            return True

    # Check for diagonal wins
    if board[0][0] == board[1][1] == board[2][2] != ' ' or \
       board[0][2] == board[1][1] == board[2][0] != ' ':
        return True

    return False

# Function to check if the game is a draw
def is_draw(board):
    # Check if there are any empty spaces
    for row in board:
        for space in row:
            if space == ' ':
                return False

    return True

# Function to start the game
if __name__ == "__main__":
    jdv()
