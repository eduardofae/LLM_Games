import numpy as np

# Create the game board
board = np.zeros((10, 10), dtype=int)

# Create a list of players
players = [1, 2]

# Create a variable to keep track of the current player
current_player = 0

# Create a variable to keep track of the game state
game_over = False

# Create a variable to keep track of the winner
winner = None

# Main game loop
while not game_over:
    # Get the player's move
    move = input("Player {}'s turn. Enter a column number (1-10): ".format(players[current_player]))

    # Check if the move is valid
    if not (1 <= int(move) <= 10):
        print("Invalid move. Please enter a column number between 1 and 10.")
        continue

    # Check if the column is full
    if board[:, int(move)-1].all():
        print("Column {} is full. Please choose another column.".format(move))
        continue

    # Place the player's piece on the board
    board[board[:, int(move)-1] == 0, int(move)-1] = players[current_player]

    # Check if the player has won
    if np.any(np.sum(board, axis=0) == 3 * players[current_player]) or np.any(np.sum(board, axis=1) == 3 * players[current_player]) or np.any(np.sum(np.diag(board)) == 3 * players[current_player]) or np.any(np.sum(np.flipud(board), axis=1) == 3 * players[current_player]):
        winner = players[current_player]
        game_over = True
    
    # Check if the game is a draw
    if np.all(board != 0):
        game_over = True

    # Switch to the other player
    current_player = (current_player + 1) % 2

# Print the game board
print(board)

# Print the winner
if winner is not None:
    print("Player {} wins!".format(winner))
else:
    print("The game is a draw.")
