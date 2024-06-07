import os
import random

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
    # Print the menu
    print("Menu:")
    print("1. Play against a human")
    print("2. Play against a computer")
    print("3. Quit")

    # Get the player's choice
    choice = input("Enter your choice: ")

    # Play against a human
    if choice == '1':
        while True:
            # Get the player's move
            player1_move = input(f"{player1_name}, enter your move (row, column): ")
            row1, col1 = map(int, player1_move.split(','))
    
            # Check if the move is valid
            if not (0 <= row1 <= 2 and 0 <= col1 <= 2):
                print("Invalid move. Please try again.")
                continue
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
            if not (0 <= row2 <= 2 and 0 <= col2 <= 2):
                print("Invalid move. Please try again.")
                continue
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
    
    # Play against a computer
    elif choice == '2':
        while True:
            # Get the player's move
            player1_move = input(f"{player1_name}, enter your move (row, column): ")
            row1, col1 = map(int, player1_move.split(','))
    
            # Check if the move is valid
            if not (0 <= row1 <= 2 and 0 <= col1 <= 2):
                print("Invalid move. Please try again.")
                continue
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

            # Get the computer's move
            computer_move = get_computer_move(board)

            # Place the computer's piece on the board
            board[computer_move[0]][computer_move[1]] = player2

            # Check if the computer has won
            if check_win(board, player2):
                print("Computer wins!")
                break

            # Check if there are no more free spaces
            if check_draw(board):
                print("Draw!")
                break
    
    # Quit the game
    elif choice == '3':
        break
    
    # Print the game board
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

# Define the function to get the computer's move
def get_computer_move(board):
    # Get the list of all possible moves
    possible_moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                possible_moves.append((row, col))

    # Choose a random move from the list of possible moves
    return random.choice(possible_moves)
