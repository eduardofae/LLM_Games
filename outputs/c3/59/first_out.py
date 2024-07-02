import numpy as np
import random

# Initialize the game board
board = np.zeros((10, 10))

# Define the players
players = ["Player 1", "Player 2"]

# Define the game state
game_state = "ongoing"

# Define the winning combinations
winning_combinations = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)],
]

# Define the current player
current_player = random.choice(players)

# Main game loop
while game_state == "ongoing":
    # Get the player's move
    column = int(input(f"{current_player}'s turn. Choose a column (0-9): "))

    # Check if the move is valid
    if column < 0 or column > 9 or board[9][column] != 0:
        print("Invalid move. Please choose another column.")
        continue

    # Place the player's piece on the board
    for i in range(9, -1, -1):
        if board[i][column] == 0:
            board[i][column] = 1 if current_player == players[0] else 2
            break

    # Check if the player has won
    for winning_combination in winning_combinations:
        if all(board[x][y] == board[winning_combination[0][0]][winning_combination[0][1]] for x, y in winning_combination):
            game_state = "won"
            winner = current_player
            break

    # Check if the game is a draw
    if np.all(board != 0):
        game_state = "draw"

    # Switch to the other player
    current_player = players[1] if current_player == players[0] else players[0]

# Print the game board
print(board)

# Print the game state
if game_state == "won":
    print(f"{winner} wins!")
elif game_state == "draw":
    print("It's a draw!")
