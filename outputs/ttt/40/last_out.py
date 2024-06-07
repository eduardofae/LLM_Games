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
    # Welcome message
    print("Welcome to JDV!")

    # Get player names
    player1_name = input("Player 1, enter your name: ")
    player2_name = input("Player 2, enter your name: ")

    # Get player pieces
    while True:
        player1_piece = input("Player 1, choose your piece (X or O): ").upper()
        if player1_piece not in ["X", "O"]:
            print("Invalid piece. Please try again.")
            continue
        break
    player2_piece = "O" if player1_piece == "X" else "X"

    # Create the board
    board = np.zeros((3, 3), dtype=int)

    # Keep track of the current player
    player = 1

    # Game loop
    while True:
        # Print the board
        print_board(board)

        # Get the player's move
        if player == 1:
            move = input(f"{player1_name}, enter your move (row, column): ")
        else:
            move = input(f"{player2_name}, enter your move (row, column): ")

        # Check if the move is valid
        try:
            row, col = map(int, move.split(","))
            if row < 0 or row > 2 or col < 0 or col > 2:
                raise ValueError("Invalid move. Please try again.")
            if board[row][col] != 0:
                raise ValueError("Invalid move. Please try again.")
        except ValueError:
            print("Invalid move. Please try again.")
            continue

        # Place the player's piece on the board
        board[row][col] = player

        # Check if there is a winner
        winner = check_winner(board)

        # If there is a winner, break out of the loop
        if winner != 0:
            if winner == -1:
                print("Draw!")
            else:
                if winner == 1:
                    print(f"{player1_name} wins!")
                else:
                    print(f"{player2_name} wins!")
            break

        # Switch to the other player
        player = 3 - player

# Run the main function
if __name__ == "__main__":
    main()
