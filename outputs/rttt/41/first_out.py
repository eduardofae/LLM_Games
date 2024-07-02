# Create a 3x3 grid
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# Define the players
player1 = 'X'
player2 = 'O'

# Get the player's names
player1_name = input("Player 1, enter your name: ")
player2_name = input("Player 2, enter your name: ")

# Start the game
while True:
    # Get the player's move
    player1_move = input(f"{player1_name}, enter your move (row, column): ")
    row1, col1 = map(int, player1_move.split(','))
    
    # Check if the move is valid
    if board[row1][col1] != ' ':
        print("Invalid move. Please try again.")
        continue

    # Place the player's piece on the board
    board[row1][col1] = player1

    # Check if the player has won
    if check_win(board, player1):
        print(f"{player1_name} wins!")
        break

    # Check if there are no more free spaces
    if check_draw(board):
        print("Draw!")
        break

    # Get the player's move
    player2_move = input(f"{player2_name}, enter your move (row, column): ")
    row2, col2 = map(int, player2_move.split(','))
    
    # Check if the move is valid
    if board[row2][col2] != ' ':
        print("Invalid move. Please try again.")
        continue

    # Place the player's piece on the board
    board[row2][col2] = player2

    # Check if the player has won
    if check_win(board, player2):
        print(f"{player2_name} wins!")
        break

    # Check if there are no more free spaces
    if check_draw(board):
        print("Draw!")
        break

# Print the board
for row in board:
    print(' '.join(row))

# Define the function to check if a player has won
def check_win(board, player):
    # Check the rows
    for row in board:
        if all(x == player for x in row):
            return True

    # Check the columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check the diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    # No win yet
    return False

# Define the function to check if there are no more free spaces
def check_draw(board):
    # Check if there are any empty spaces
    for row in board:
        for col in row:
            if col == ' ':
                return False

    # No empty spaces, so it's a draw
    return True
