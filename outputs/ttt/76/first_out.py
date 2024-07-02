# Initialize the game board
board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

# Initialize the player's turn
player = 1

# Game loop
while True:
    # Get the player's move
    move = input("Player {}'s turn (row, column): ".format(player))
    row, column = map(int, move.split())

    # Check if the move is valid
    if board[row][column] != ' ':
        print("Invalid move. Try again.")
        continue

    # Place the player's piece on the board
    board[row][column] = 'X' if player == 1 else 'O'

    # Check if the player has won
    if check_winner(board) == player:
        print("Player {} wins!".format(player))
        break

    # Check if the board is full
    if all(all(cell != ' ' for cell in row) for row in board):
        print("It's a draw.")
        break

    # Switch the player's turn
    player = 2 if player == 1 else 1

# Check if the player has won
def check_winner(board):
    # Check the rows
    for row in board:
        if all(cell == row[0] for cell in row) and row[0] != ' ':
            return row[0]

    # Check the columns
    for column in range(3):
        if all(board[row][column] == board[0][column] for row in range(3)) and board[0][column] != ' ':
            return board[0][column]

    # Check the diagonals
    if all(board[row][row] == board[0][0] for row in range(3)) and board[0][0] != ' ':
        return board[0][0]
    if all(board[row][2-row] == board[0][2] for row in range(3)) and board[0][2] != ' ':
        return board[0][2]

    # No winner yet
    return None
