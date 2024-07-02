import numpy as np

# Game board
board = np.zeros((10, 10), dtype=int)

# Players
players = [1, 2]

# Game loop
while True:
    # Get player input
    player = players[0]
    column = int(input(f"Player {player}, choose a column (0-9): "))

    # Check if column is valid
    if column < 0 or column > 9:
        print("Invalid column")
        continue

    # Check if column is full
    if board[:, column].max() == 2:
        print("Column is full")
        continue

    # Place piece
    row = np.where(board[:, column] == 0)[0][-1]
    board[row, column] = player

    # Check for win
    if np.any(np.sum(board, axis=0) == 3 * player) or np.any(np.sum(board, axis=1) == 3 * player):
        print(f"Player {player} wins!")
        break

    # Check for draw
    if np.all(board != 0):
        print("Draw")
        break

    # Switch players
    players = players[1:] + players[:1]
