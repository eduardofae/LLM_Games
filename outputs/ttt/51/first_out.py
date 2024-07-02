# Initialize the game board
board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

# Initialize the players' turns
player1_turn = True
player2_turn = False

# Get the players' names
player1_name = input("Enter player 1's name: ")
player2_name = input("Enter player 2's name: ")

# Game loop
while True:
    # Print the game board
    for row in board:
        print(' '.join(row))

    # Get the player's move
    if player1_turn:
        move = input(f"{player1_name}'s turn (row, column): ")
    else:
        move = input(f"{player2_name}'s turn (row, column): ")

    # Check if the move is valid
    if not move or len(move) != 2:
        print("Invalid move. Please enter a row and column number, separated by a space.")
        continue

    row, column = move.split()
    row = int(row) - 1
    column = int(column) - 1

    if row < 0 or row > 2 or column < 0 or column > 2:
        print("Invalid move. Please enter a row and column number between 1 and 3.")
        continue

    if board[row][column] != ' ':
        print("Invalid move. That space is already taken.")
        continue

    # Place the player's piece on the board
    if player1_turn:
        board[row][column] = 'X'
    else:
        board[row][column] = 'O'

    # Check if the player has won
    if check_win(board, player1_turn):
        if player1_turn:
            print(f"{player1_name} wins!")
        else:
            print(f"{player2_name} wins!")
        break

    # Check if there are no more free spaces
    if check_draw(board):
        print("Draw!")
        break

    # Switch the player's turns
    player1_turn = not player1_turn
    player2_turn = not player2_turn

# Function to check if the player has won
def check_win(board, player_turn):
    symbol = 'X' if player_turn else 'O'

    # Check for horizontal wins
    for row in board:
        if all(x == symbol for x in row):
            return True

    # Check for vertical wins
    for column in range(3):
        if all(board[row][column] == symbol for row in range(3)):
            return True

    # Check for diagonal wins
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        return True
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        return True

    # No win yet
    return False

# Function to check if there are no more free spaces
def check_draw(board):
    return all(x != ' ' for row in board for x in row)