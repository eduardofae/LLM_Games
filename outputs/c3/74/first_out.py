import numpy as np

# Create the game board
board = np.zeros((10, 10))

# Define the players
player1 = 1
player2 = 2

# Define the game state
game_over = False
draw = False

# Main game loop
while not game_over:
    # Get the player's move
    print("Player", player1, "turn:")
    column = int(input("Choose a column (1-10): "))
    
    # Check if the column is valid
    if column < 1 or column > 10:
        print("Invalid column")
        continue
    
    # Check if the column is full
    if board[:, column - 1].min() != 0:
        print("Column is full")
        continue
    
    # Place the player's piece on the board
    board[board[:, column - 1] == 0, column - 1] = player1
    
    # Check if the player has won
    if np.any(np.sum(board, axis=0) == 3 * player1) or np.any(np.sum(board, axis=1) == 3 * player1) or np.any(np.diagonal(board) == 3 * player1):
        print("Player", player1, "wins!")
        game_over = True
        break
    
    # Check if the game is a draw
    if not np.any(board == 0):
        print("Draw!")
        game_over = True
        draw = True
        break
    
    # Switch to the other player
    player1, player2 = player2, player1

# Print the final game board
print(board)

# Print the game result
if not draw:
    print("Player", player2, "wins!")
else:
    print("Game Over")
