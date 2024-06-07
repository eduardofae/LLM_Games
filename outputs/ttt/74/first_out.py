import numpy as np

# Create a 3x3 game board
board = np.zeros((3, 3))

# Define the players
player1 = 'X'
player2 = 'O'

# Define the current player
current_player = player1

# Define the winning combinations
winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                         (0, 3, 6), (1, 4, 7), (2, 5, 8),
                         (0, 4, 8), (2, 4, 6)]

# Main game loop
while True:
    # Print the game board
    print(board)

    # Get the player's move
    move = int(input("Enter your move (1-9): "))

    # Check if the move is valid
    if move < 1 or move > 9 or board[move-1] != 0:
        print("Invalid move. Try again.")
        continue

    # Place the player's piece on the board
    board[move-1] = current_player

    # Check if the player has won
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] != 0:
            print(f"{current_player} wins!")
            break

    # Check if there are no more free spaces
    if np.all(board != 0):
        print("Draw!")
        break

    # Switch the current player
    current_player = player2 if current_player == player1 else player1
