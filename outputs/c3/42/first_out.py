import numpy as np

# Create the game board
board = np.zeros((10, 10), dtype=int)

# Define the players
players = [1, 2]

# Define the current player
current_player = players[0]

# Define the game status
game_status = "ongoing"

# Game loop
while game_status == "ongoing":
    # Print the game board
    print(board)

    # Get the player's move
    move = int(input(f"Player {current_player}, enter a column (1-10): "))

    # Check if the move is valid
    if move < 1 or move > 10 or board[9, move - 1] != 0:
        print("Invalid move. Try again.")
        continue

    # Place the player's piece on the board
    for i in range(9, -1, -1):
        if board[i, move - 1] == 0:
            board[i, move - 1] = current_player
            break

    # Check if the player has won
    if check_win(board, current_player):
        game_status = "win"
        print(f"Player {current_player} wins!")
    elif np.all(board != 0):
        game_status = "draw"
        print("Draw!")

    # Switch to the other player
    current_player = players[(players.index(current_player) + 1) % 2]

# Print the final game board
print(board)

def check_win(board, player):
    # Check for horizontal win
    for i in range(10):
        if np.all(board[i, :] == player):
            return True

    # Check for vertical win
    for j in range(10):
        if np.all(board[:, j] == player):
            return True

    # Check for diagonal win
    for i in range(10):
        for j in range(10):
            if i + 2 < 10 and j + 2 < 10 and board[i, j] == player and board[i + 1, j + 1] == player and board[i + 2, j + 2] == player:
                return True
            if i + 2 < 10 and j - 2 >= 0 and board[i, j] == player and board[i + 1, j - 1] == player and board[i + 2, j - 2] == player:
                return True

    return False
