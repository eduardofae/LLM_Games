import numpy as np

# Create the game board
board = np.zeros((10, 10))

# Define the players
players = [1, 2]

# Set the current player
current_player = 0

# Start the game loop
while True:

    # Get the column where the player wants to place their piece
    column = int(input("Player {}: Choose a column (0-9): ".format(players[current_player])))

    # Check if the column is valid
    if column < 0 or column > 9:
        print("Invalid column. Please choose a column between 0 and 9.")
        continue

    # Check if the column is full
    if board[:, column].all():
        print("Column {} is full. Please choose another column.".format(column))
        continue

    # Place the player's piece in the column
    board[board[:, column] == 0, column] = players[current_player]

    # Check if the player has won
    if np.any(np.all(board == players[current_player], axis=0)) or \
       np.any(np.all(board == players[current_player], axis=1)) or \
       np.any(np.diag(board) == players[current_player]) or \
       np.any(np.diag(np.fliplr(board)) == players[current_player]):

        print("Player {} wins!".format(players[current_player]))
        break

    # Check if the game is a draw
    if np.all(board != 0):
        print("Draw!")
        break

    # Switch to the other player
    current_player = (current_player + 1) % 2

# Print the final board
print(board)
