import numpy as np

def jdv():
    # Create the game board
    board = np.zeros((3, 3))

    # Define the players
    players = [1, 2]

    # Start the game
    while True:
        # Get the current player
        player = players[0]

        # Get the player's move
        move = input(f"Player {player}, enter your move (row, column): ")
        row, col = map(int, move.split(","))

        # Check if the move is valid
        if board[row, col] != 0:
            print("Invalid move. Please try again.")
            continue

        # Place the player's piece on the board
        board[row, col] = player

        # Check if the player has won
        if check_win(board, player):
            print(f"Player {player} wins!")
            break

        # Check if the game is a draw
        if np.all(board != 0):
            print("It's a draw!")
            break

        # Switch to the other player
        players = [players[1], players[0]]

def check_win(board, player):
    # Check for a win in each row
    for row in range(3):
        if np.all(board[row, :] == player):
            return True

    # Check for a win in each column
    for col in range(3):
        if np.all(board[:, col] == player):
            return True

    # Check for a win in each diagonal
    if np.all(np.diag(board) == player):
        return True
    if np.all(np.diag(np.flip(board)) == player):
        return True

    # No win yet
    return False

if __name__ == "__main__":
    jdv()
