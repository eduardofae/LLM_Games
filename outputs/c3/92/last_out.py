import numpy as np

# Create the game board
board = np.zeros((10, 10))

# Define the players
players = ['X', 'O']

# Define the game state
game_state = 'ongoing'

# Start the game
while game_state == 'ongoing':

    # Get the current player
    current_player = players[0]

    # Get the player's move
    while True:
        try:
            column = int(input(f"Player {current_player}, choose a column (1-10): ")) - 1
            if column < 0 or column > 9 or board[9, column] != 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid move. Please try again.")

    # Place the player's piece on the board
    for i in range(9, -1, -1):
        if board[i, column] == 0:
            board[i, column] = current_player
            break

    # Check if the player has won
    if check_win(board, current_player):
        game_state = 'won'
        print(f"Game over! Player {current_player} has won!")

    # Check if the game is a draw
    elif np.all(board != 0):
        game_state = 'draw'
        print("Game over! It's a draw!")

    # Switch to the next player
    players = players[1:] + players[:1]

# Print the final game board
print(board)

def check_win(board, player):

    # Check for horizontal wins
    if any(np.all(board[row, :] == player) for row in range(10)):
        return True

    # Check for vertical wins
    if any(np.all(board[:, col] == player) for col in range(10)):
        return True

    # Check for diagonal wins
    if any(np.all(board.diagonal()[i::10] == player) for i in range(10)):
        return True
    if any(np.all(np.flip(board).diagonal()[i::10] == player) for i in range(10)):
        return True

    # No wins found
    return False
