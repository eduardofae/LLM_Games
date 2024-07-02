import numpy as np

def check_winner(board):
    # Check rows
    for i in range(3):
        if np.all(board[i,:] == board[i,0]) and board[i,0] != 0:
            return board[i,0]

    # Check columns
    for j in range(3):
        if np.all(board[:,j] == board[0,j]) and board[0,j] != 0:
            return board[0,j]

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
        # Get the current player
        player = players[0]

        # Get the player's move
        move = input(f"Player {player}, enter your move (row, column): ")
        row, col = [int(x) for x in move.split()]

        # Check if the move is valid
        if board[row, col] != 0:
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

if __name__ == "__main__":
    play_jdv()
