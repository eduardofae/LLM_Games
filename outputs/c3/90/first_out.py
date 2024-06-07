import numpy as np

# Create the game board
board = np.zeros((10, 10))

# Create a list of players
players = ['Player 1', 'Player 2']

# Keep track of the current player
currentPlayer = 0

# Keep track of the winner
winner = None

# Main game loop
while winner is None:
    # Get the current player's move
    row, col = map(int, input('Player {}, enter your move (row, col): '.format(currentPlayer + 1)).split())

    # Check if the move is valid
    if row < 0 or row >= 10 or col < 0 or col >= 10 or board[row, col] != 0:
        print('Invalid move. Try again.')
        continue

    # Place the player's piece on the board
    board[row, col] = currentPlayer + 1

    # Check if the player has won
    if check_win(board, currentPlayer + 1):
        winner = players[currentPlayer]
        break

    # Switch to the other player
    currentPlayer = (currentPlayer + 1) % 2

# Print the winner
if winner is not None:
    print('{} wins!'.format(winner))
else:
    print('Draw!')

# Define a function to check if a player has won
def check_win(board, player):
    # Check for a horizontal win
    for row in range(10):
        if np.all(board[row, :] == player):
            return True

    # Check for a vertical win
    for col in range(10):
        if np.all(board[:, col] == player):
            return True

    # Check for a diagonal win
    for i in range(10):
        if np.all(board[i, i] == player) or np.all(board[i, 9 - i] == player):
            return True

    # No win yet
    return False
