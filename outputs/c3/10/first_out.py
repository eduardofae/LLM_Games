import numpy as np

# Create the game board
board = np.zeros((10, 10), dtype=int)

# Define the players
players = ['Player 1', 'Player 2']

# Define the current player
current_player = 0

# Define the winning combinations
winning_combinations = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
]

# Main game loop
while True:
    # Get the player's move
    column = int(input(f"{players[current_player]}'s turn. Choose a column (0-9): "))

    # Place the player's piece on the board
    for row in range(9, -1, -1):
        if board[row][column] == 0:
            board[row][column] = current_player + 1
            break

    # Check if the player has won
    for combination in winning_combinations:
        if all(board[combination[i][0]][combination[i][1]] == current_player + 1 for i in range(3)):
            print(f"{players[current_player]} wins!")
            break

    # Check if the board is full
    if np.all(board != 0):
        print("Draw!")
        break

    # Switch to the other player
    current_player = (current_player + 1) % 2

    # Print the game board
    print(board)
