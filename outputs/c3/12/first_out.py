import numpy as np

# Define the game board
board = np.zeros((10, 10))

# Define the players
players = ['X', 'O']

# Define the current player
current_player = 0

# Define the game loop
while True:
    # Get the column from the current player
    column = int(input('Player {}: Choose a column (0-9): '.format(players[current_player])))

    # Check if the column is valid
    if column < 0 or column > 9:
        print('Invalid column')
        continue

    # Check if the column is full
    if board[:, column].max() != 0:
        print('Column is full')
        continue

    # Place the piece on the board
    row = np.where(board[:, column] == 0)[0][-1]
    board[row, column] = players[current_player]

    # Check if the current player has won
    if check_winner(board, players[current_player]):
        print('Player {} wins!'.format(players[current_player]))
        break

    # Check if the game is a draw
    if np.all(board != 0):
        print('Draw!')
        break

    # Switch to the other player
    current_player = (current_player + 1) % 2

# Define the function to check for a winner
def check_winner(board, player):
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
        if np.all(board.diagonal(i) == player) or np.all(np.flip(board).diagonal(i) == player):
            return True

    # No winner yet
    return False
