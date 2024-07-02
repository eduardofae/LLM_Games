import numpy as np

# Define the game board
board = np.zeros((10, 10))

# Define the players
player1 = 1
player2 = 2

# Define the game status
game_status = "ongoing"

# Main game loop
while game_status == "ongoing":
    # Get the player's move
    player_move = int(input("Player {}, enter a column (1-10): ".format(player1 if player1 == 1 else player2))) - 1

    # Check if the move is valid
    if board[9, player_move] != 0:
        print("Invalid move. Please try again.")
        continue

    # Place the player's piece on the board
    for i in range(9, -1, -1):
        if board[i, player_move] == 0:
            board[i, player_move] = player1 if player1 == 1 else player2
            break

    # Check if the player has won
    if check_for_win(board, player1 if player1 == 1 else player2):
        game_status = "won"
        print("Player {} has won!".format(player1 if player1 == 1 else player2))
    else:
        # Check if there are any more free spaces
        if np.all(board != 0):
            game_status = "draw"
            print("Draw!")

    # Switch players
    player1, player2 = player2, player1

# Define the function to check for a win
def check_for_win(board, player):
    # Check for horizontal wins
    for i in range(10):
        if np.all(board[i, :] == player):
            return True

    # Check for vertical wins
    for j in range(10):
        if np.all(board[:, j] == player):
            return True

    # Check for diagonal wins
    for i in range(10):
        for j in range(10):
            if board[i, j] == player and (board[i + 1, j + 1] == player and board[i + 2, j + 2] == player) or (board[i + 1, j - 1] == player and board[i + 2, j - 2] == player):
                return True

    return False
