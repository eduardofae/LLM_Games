import numpy as np
import random
import socket

# Initialize the game board
board = np.zeros((10, 10))

# Define the players
players = ["Player 1", "Player 2", "AI"]

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
    if current_player == "AI":
        # AI move logic goes here
        move = random.choice([i for i in range(10) if board[9][i] == 0])
    elif current_player == "Player 1":
        # Handle player 1's move
        column = input(f"{current_player}'s turn. Choose a column (0-9): ")

        # Validate the player's input
        while not column.isdigit() or int(column) < 0 or int(column) > 9 or board[9][int(column)] != 0:
            column = input("Invalid move. Please choose another column (0-9): ")

        move = int(column)
    elif current_player == "Player 2":
        # Handle player 2's move
        # ... (similar to player 1's move handling)

    # Place the player's piece on the board
    for i in range(9, -1, -1):
        if board[i][move] == 0:
            board[i][move] = 1 if current_player == "Player 1" else 2
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
