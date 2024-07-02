import numpy as np

# Initialize the game board
board = np.zeros((3, 3), dtype=int)

# Define the player symbols
player1 = "X"
player2 = "O"

# Define the game state
game_over = False
winner = None

# Start the game loop
while not game_over:
    # Get the current player's move
    if player1 is not None:
        row, col = map(int, input("Player 1's move (row, col): ").split())
    else:
        row, col = map(int, input("Player 2's move (row, col): ").split())

    # Check if the move is valid
    if board[row, col] == 0:
        # Place the player's piece on the board
        board[row, col] = player1 if player1 is not None else player2

        # Check if the player has won
        if (board[row, :] == player1 or
            board[:, col] == player1 or
            (row == col and board.diagonal() == player1) or
            (row + col == 2 and np.flip(board).diagonal() == player1)):
            winner = player1
            game_over = True
        elif (board[row, :] == player2 or
            board[:, col] == player2 or
            (row == col and board.diagonal() == player2) or
            (row + col == 2 and np.flip(board).diagonal() == player2)):
            winner = player2
            game_over = True

        # Check if the game is a draw
        if not np.any(board == 0):
            winner = "draw"
            game_over = True
    else:
        print("Invalid move. Please try again.")

    # Swap the player symbols
    player1, player2 = player2, player1

# Print the game board
print(board)

# Print the winner
if winner is not None:
    print(f"{winner} wins!")
else:
    print("Game over. It's a draw.")
