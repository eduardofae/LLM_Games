import numpy as np

# Create the game board
board = np.zeros((3, 3))

# Define the players
players = ['X', 'O']

# Define the game status
game_status = 'ongoing'

# Start the game loop
while game_status == 'ongoing':
    
    # Get the current player
    current_player = players[0]

    # Get the player's move
    row, col = map(int, input(f'{current_player}, enter your move (row, col): ').split())

    # Check if the move is valid
    if board[row, col] != 0:
        print('Invalid move. Please try again.')
        continue

    # Place the player's piece on the board
    board[row, col] = current_player

    # Check if the player has won
    if check_win(board, current_player):
        game_status = 'win'
        print(f'{current_player} wins!')
        break

    # Check if the game is a draw
    if np.all(board != 0):
        game_status = 'draw'
        print('The game is a draw.')
        break

    # Switch the current player
    players.reverse()

# Print the final game board
print(board)

# Check if there is a winner
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

    # No winner yet
    return False
