import numpy as np

def main():
    # Create the game board
    board = np.zeros((10, 10), dtype=int)

    # Create the players
    players = [1, -1]

    # Play the game
    while True:
        # Get the player's move
        for player in players:
            print(board)
            move = int(input(f"Player {player}, enter a column (0-9): "))

            # Check if the move is valid
            if move < 0 or move > 9 or board[9, move] != 0:
                print("Invalid move.")
                continue

            # Place the player's piece on the board
            for i in range(9, -1, -1):
                if board[i, move] == 0:
                    board[i, move] = player
                    break

            # Check if the player has won
            if check_win(board, player):
                print(f"Player {player} wins!")
                return

        # Check if the game is a draw
        if np.all(board != 0):
            print("Draw!")
            return

# Check if the player has won
def check_win(board, player):
    # Check the rows
    for i in range(10):
        if np.all(board[i, :] == player):
            return True

    # Check the columns
    for i in range(10):
        if np.all(board[:, i] == player):
            return True

    # Check the diagonals
    for i in range(6):
        for j in range(6):
            if np.all(board[i:i+3, j:j+3] == player):
                return True

    for i in range(3, 10):
        for j in range(6):
            if np.all(board[i:i+3, j:j+3] == player):
                return True

    return False

if __name__ == "__main__":
    main()
