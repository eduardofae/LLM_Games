import numpy as np

# Create the game board
board = np.zeros((10, 10))

# Define the players
players = ['X', 'O']

# Define the game state
state = 'ongoing'

# Main game loop
while state == 'ongoing':
    # Get the current player
    player = players[0]

    # Get the player's move
    try:
        column = int(input('Player {}, choose a column (0-9): '.format(player)))
    except ValueError:
        print('Invalid input. Please enter a number between 0 and 9.')
        continue

    # Check if the move is valid
    if column < 0 or column > 9 or board[9, column] != 0:
        print('Invalid move. Please choose an empty column.')
        continue

    # Place the player's piece on the board
    for i in range(9, -1, -1):
        if board[i, column] == 0:
            board[i, column] = player
            break

    # Check if the player has won
    if check_win(board, player):
        state = 'win'

    # Check if the game is a draw
    if np.all(board != 0):
        state = 'draw'

    # Switch players
    players = players[1:] + players[:1]

# Print the game board
print(board)

# Print the game state
if state == 'win':
    print('Player {} wins!'.format(player))
elif state == 'draw':
    print('Draw!')

# Define the function to check if the player has won
def check_win(board, player):
    # Check for horizontal win
    for i in range(10):
        if np.all(board[i, :] == player):
            return True

    # Check for vertical win
    for j in range(10):
        if np.all(board[:, j] == player):
            return True

    # Check for diagonal win (from top left to bottom right)
    if np.all(np.diagonal(board) == player):
        return True

    # Check for diagonal win (from bottom left to top right)
    if np.all(np.flipud(np.diagonal(board)) == player):
        return True

    # No win found
    return False
