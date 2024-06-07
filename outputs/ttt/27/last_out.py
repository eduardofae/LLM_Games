import numpy as np

def check_winner(board):
    # Check rows
    for row in board:
        if np.all(row == row[0]) and row[0] != 0:
            return row[0]

    # Check columns
    for col in board.T:
        if np.all(col == col[0]) and col[0] != 0:
            return col[0]

    # Check diagonals
    if np.all(board.diagonal() == board[0,0]) and board[0,0] != 0:
        return board[0,0]
    if np.all(np.flip(board).diagonal() == board[0,2]) and board[0,2] != 0:
        return board[0,2]

    # Check draw
    if np.all(board != 0):
        return -1

    # Continue playing
    return 0

def play_jdv():
    # Initialize the game board
    board = np.zeros((3,3), dtype=int)

    # Initialize the players
    players = [1, 2]

    # Play the game
    while True:
        try:
            # Get the current player
            player = players[0]

            # Get the player's move
            move = input(f"Player {player}, enter your move (row, column): ")
            row, col = [int(x) for x in move.split()]

            # Check if the move is valid
            if row < 0 or row > 2 or col < 0 or col > 2 or board[row, col] != 0:
                print("Invalid move. Please choose an empty space.")
                continue

            # Place the player's piece on the board
            board[row, col] = player

            # Check if the player has won
            winner = check_winner(board)
            if winner != 0:
                print(f"Player {winner} wins!")
                break

            # Switch to the other player
            players = players[1:] + players[:1]

        except ValueError:
            print("Invalid input. Please enter the move in the format 'row, column'.")

if __name__ == "__main__":
    play_jdv()
