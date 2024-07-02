import numpy as np

def check_winner(board):
    # Check if there is a line of 3 adjacent pieces
    for player in [1, 2]:
        for i in range(3):
            # Check rows
            if board[i, :].sum() == 3*player:
                return player

            # Check columns
            if board[:, i].sum() == 3*player:
                return player

        # Check diagonals
        if board[0, 0] + board[1, 1] + board[2, 2] == 3*player:
            return player
        if board[0, 2] + board[1, 1] + board[2, 0] == 3*player:
            return player

    # If there is no winner, return 0
    return 0

def print_board(board):
    for i in range(3):
        for j in range(3):
            print(board[i, j], end=" ")
        print()

if __name__ == "__main__":
    # Create the game board
    board = np.zeros((3, 3), dtype=int)

    # Set the current player
    current_player = 1

    # Game loop
    while True:
        # Print the board
        print_board(board)

        # Get the player's move
        move = int(input(f"Player {current_player}, enter your move (1-9): "))

        # Convert the move to a row and column index
        row = (move - 1) // 3
        col = (move - 1) % 3

        # Check if the move is valid
        if board[row, col] != 0:
            print("Invalid move. Please try again.")
            continue

        # Place the player's piece on the board
        board[row, col] = current_player

        # Check if the player has won
        winner = check_winner(board)
        if winner != 0:
            print(f"Player {winner} has won!")
            break

        # Check if the game is a draw
        if np.all(board != 0):
            print("Draw!")
            break

        # Switch the current player
        current_player = 3 - current_player
