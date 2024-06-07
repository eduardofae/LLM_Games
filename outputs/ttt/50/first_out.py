import numpy as np

def print_board(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=" ")
        print()

def check_winner(board):
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            return board[i][0]

    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != 0:
            return board[0][j]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != 0:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != 0:
        return board[0][2]

    return 0

def get_player_input(player):
    while True:
        try:
            row = int(input(f"Player {player}, enter row (1-3): "))
            col = int(input(f"Player {player}, enter column (1-3): "))
            if 1 <= row <= 3 and 1 <= col <= 3 and board[row-1][col-1] == 0:
                return row-1, col-1
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input. Enter integers only.")

# Create a 3x3 board
board = np.zeros((3, 3), dtype=int)

# Main game loop
while True:
    # Get player 1's move
    row, col = get_player_input(1)
    board[row][col] = 1

    # Print the board
    print_board(board)

    # Check if player 1 has won
    winner = check_winner(board)
    if winner == 1:
        print("Player 1 wins!")
        break

    # Check if there are any more free spaces
    if np.all(board != 0):
        print("Draw!")
        break

    # Get player 2's move
    row, col = get_player_input(2)
    board[row][col] = 2

    # Print the board
    print_board(board)

    # Check if player 2 has won
    winner = check_winner(board)
    if winner == 2:
        print("Player 2 wins!")
        break
