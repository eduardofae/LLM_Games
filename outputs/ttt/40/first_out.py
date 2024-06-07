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

    # Check draw
    if np.all(board != 0):
        return -1

    # No winner or draw yet
    return 0

def main():
    # Create the board
    board = np.zeros((3, 3), dtype=int)

    # Keep track of the current player
    player = 1

    # Game loop
    while True:
        # Get the player's move
        move = input(f"Player {player}, enter your move (row, column): ")
        row, col = map(int, move.split(","))

        # Check if the move is valid
        if board[row][col] != 0:
            print("Invalid move. Please try again.")
            continue

        # Place the player's piece on the board
        board[row][col] = player

        # Print the board
        print_board(board)

        # Check if there is a winner
        winner = check_winner(board)

        # If there is a winner, break out of the loop
        if winner != 0:
            if winner == -1:
                print("Draw!")
            else:
                print(f"Player {winner} wins!")
            break

        # Switch to the other player
        player = 3 - player

# Run the main function
if __name__ == "__main__":
    main()
