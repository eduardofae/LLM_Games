import numpy as np

# Initialize the game board
board = np.zeros((10, 10), dtype=int)

# Define the players
players = [1, 2]

# Set the current player
current_player = players[0]

# Game loop
while True:

    # Get the player's move
    print(f"Player {current_player}'s turn:")
    column = int(input("Choose a column (1-10): ")) - 1

    # Check if the move is valid
    if column < 0 or column > 9 or board[9, column] != 0:
        print("Invalid move. Please choose a different column.")
        continue

    # Place the player's piece on the board
    for i in range(9, -1, -1):
        if board[i, column] == 0:
            board[i, column] = current_player
            break

    # Check if the player has won
    if check_win(board, current_player):
        print(f"Player {current_player} wins!")
        break

    # Check if the game is a draw
    if np.all(board != 0):
        print("Draw!")
        break

    # Switch to the other player
    current_player = players[(players.index(current_player) + 1) % 2]

# Print the final board
print(board)


# Function to check if a player has won
def check_win(board, player):
    
    # Check for a horizontal win
    for i in range(10):
        if np.all(board[i, :] == player):
            return True

    # Check for a vertical win
    for j in range(10):
        if np.all(board[:, j] == player):
            return True

    # Check for a diagonal win
    for i in range(10):
        for j in range(10):
            if board[i, j] == player and i + j < 10:
                if board[i + 1, j + 1] == player and board[i + 2, j + 2] == player:
                    return True
            if board[i, j] == player and i + j >= 10:
                if board[i - 1, j - 1] == player and board[i - 2, j - 2] == player:
                    return True

    # No win
    return False
