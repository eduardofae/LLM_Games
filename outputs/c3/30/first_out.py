import numpy as np

# Create the game board
board = np.zeros((10, 10))

# Create a list of the players
players = [1, 2]

# Set the current player to player 1
current_player = 0

# Set the game state to "ongoing"
game_state = "ongoing"

# Print the game board
print(board)

# Get the player's move
while game_state == "ongoing":
    column = int(input("Player {}'s turn. Enter a column number (0-9): ".format(players[current_player])))

    # Check if the column is valid
    if column < 0 or column > 9:
        print("Invalid column. Please try again.")
        continue

    # Check if the column is full
    if board[0][column] != 0:
        print("Column is full. Please try again.")
        continue

    # Place the player's piece in the column
    for i in range(9, -1, -1):
        if board[i][column] == 0:
            board[i][column] = players[current_player]
            break

    # Check if the player has won
    if check_for_win(board, players[current_player]):
        print("Player {} wins!".format(players[current_player]))
        game_state = "finished"
    else:
        # Check if there are any more free spaces
        if np.all(board != 0):
            print("Draw!")
            game_state = "finished"
        else:
            # Switch to the other player
            current_player = (current_player + 1) % len(players)

    # Print the game board
    print(board)

def check_for_win(board, player):
    # Check for a horizontal win
    for i in range(10):
        if np.all(board[i] == player):
            return True

    # Check for a vertical win
    for i in range(10):
        if np.all(board[:, i] == player):
            return True

    # Check for a diagonal win
    for i in range(10):
        if np.all(np.diagonal(board[i:], axis1=i, axis2=1-i) == player):
            return True
        if np.all(np.diagonal(np.flip(board[i:], axis=0)[i:], axis1=i, axis2=1-i) == player):
            return True

    # No win found
    return False
