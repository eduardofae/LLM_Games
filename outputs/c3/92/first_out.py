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
    move = int(input(f"Player {current_player}, choose a column (1-10): ")) - 1
    
    # Check if the move is valid
    if move < 0 or move > 9 or board[9, move] != 0:
        print("Invalid move. Please try again.")
        continue

    # Place the player's piece on the board
    for i in range(9, -1, -1):
        if board[i, move] == 0:
            board[i, move] = current_player
            break

    # Check if the player has won
    if check_win(board, current_player):
        game_state = 'won'
        print(f"Player {current_player} has won!")
    
    # Check if the game is a draw
    elif np.all(board != 0):
        game_state = 'draw'
        print("The game is a draw.")

    # Switch to the next player
    players = players[1:] + players[:1]

# Print the final game board
print(board)

def check_win(board, player):
    
    # Check for horizontal wins
    for row in range(10):
        if np.all(board[row, :] == player):
            return True

    # Check for vertical wins
    for col in range(10):
        if np.all(board[:, col] == player):
            return True

    # Check for diagonal wins
    for i in range(10):
        if np.all(board.diagonal()[i::10] == player):
            return True
        if np.all(np.flip(board).diagonal()[i::10] == player):
            return True

    # No wins found
    return False
