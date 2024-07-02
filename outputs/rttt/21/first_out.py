
import os

# Initialize game board
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

# Initialize player turn
player_turn = 'X'

# Game loop
while True:
    # Print game board
    print('Current board:')
    for row in board:
        print(' '.join(row))

    # Get player input
    row = int(input('Enter row (1-3): ')) - 1
    col = int(input('Enter column (1-3): ')) - 1

    # Check if move is valid
    if board[row][col] != ' ':
        print('Invalid move. Space already occupied.')
        continue

    # Place player's piece on board
    board[row][col] = player_turn

    # Check if player has won
    if check_win(board, player_turn):
        print(f'{player_turn} wins!')
        break

    # Check if game is a draw
    if check_draw(board):
        print('Draw!')
        break

    # Switch player turn
    if player_turn == 'X':
        player_turn = 'O'
    else:
        player_turn = 'X'

# Function to check if a player has won
def check_win(board, player):
    # Check for horizontal wins
    for row in board:
        if all(x == player for x in row):
            return True

    # Check for vertical wins
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check for diagonal wins
    if board[0][0] == board[1][1] == board[2][2] == player or board[0][2] == board[1][1] == board[2][0] == player:
        return True

    # No win found
    return False

# Function to check if the game is a draw
def check_draw(board):
    # Check if there are any empty spaces
    for row in board:
        for col in row:
            if col == ' ':
                return False

    # No empty spaces found, game is a draw
    return True
