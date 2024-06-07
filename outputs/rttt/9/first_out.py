import numpy as np

def jdv():
    # Create the game board
    board = np.zeros((3, 3))

    # Set up the players
    player1 = 'X'
    player2 = 'O'

    # Set up the game loop
    while True:
        # Get the player's move
        move = input(f"{player1}'s turn: ")

        # Convert the move to a row and column
        row, col = map(int, move.split())

        # Check if the move is valid
        if board[row, col] != 0:
            print("Invalid move")
            continue

        # Place the player's piece on the board
        board[row, col] = player1

        # Check if the player has won
        if check_win(board, player1):
            print(f"{player1} wins!")
            break

        # Check if there are no more free spaces
        if np.all(board != 0):
            print("Draw!")
            break

        # Switch players
        player1, player2 = player2, player1

    # Print the final board
    print(board)

def check_win(board, player):
    # Check the rows
    for row in range(3):
        if np.all(board[row, :] == player):
            return True

    # Check the columns
    for col in range(3):
        if np.all(board[:, col] == player):
            return True

    # Check the diagonals
    if np.all(board.diagonal() == player):
        return True
    if np.all(np.flip(board).diagonal() == player):
        return True

    # No win yet
    return False

if __name__ == "__main__":
    jdv()
