import numpy as np

# Define game constants
PLAYER_1 = 'X'
PLAYER_2 = 'O'
EMPTY_CELL = ' '

# Create a 3x3 game board
board = np.full((3, 3), EMPTY_CELL, dtype=str)

# Function to print the game board
def print_board(board):
    for row in board:
        print(' | '.join(row))

# Function to check if a player has won
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2-i] == player for i in range(3)):
        return True

    return False

# Function to get player input
def get_player_input(player):
    while True:
        try:
            row = int(input(f"Player {player}, enter row (1-3): "))
            col = int(input(f"Player {player}, enter column (1-3): "))
            if 1 <= row <= 3 and 1 <= col <= 3 and board[row-1][col-1] == EMPTY_CELL:
                return row-1, col-1
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter integers only.")

# Function to check if the game board is full
def is_board_full(board):
    return np.all(board != EMPTY_CELL)

# Main game loop
while True:
    # Print the game board
    print_board(board)

    # Get player 1's move
    row, col = get_player_input(PLAYER_1)
    board[row][col] = PLAYER_1

    # Check if player 1 has won
    if check_winner(board, PLAYER_1):
        print("Player 1 wins!")
        break

    # Check if the board is full
    if is_board_full(board):
        print("Draw!")
        break

    # Get player 2's move
    row, col = get_player_input(PLAYER_2)
    board[row][col] = PLAYER_2

    # Check if player 2 has won
    if check_winner(board, PLAYER_2):
        print("Player 2 wins!")
        break
