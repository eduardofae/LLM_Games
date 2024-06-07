import numpy as np

# Create the game board
board = np.zeros((10, 10), dtype=int)

# Define the players
players = ['Player 1', 'Player 2']

# Define the current player
current_player = 0

# Define the winning combinations
winning_combinations = [
    [(row, col), (row, col + 1), (row, col + 2)]
    for row in range(10)
    for col in range(8)
] + [
    [(row, col), (row + 1, col), (row + 2, col)]
    for row in range(8)
    for col in range(10)
] + [
    [(row, col), (row + 1, col + 1), (row + 2, col + 2)]
    for row in range(8)
    for col in range(8)
] + [
    [(row, col + 2), (row + 1, col + 1), (row + 2, col)]
    for row in range(8)
    for col in range(8)
]

# Main game loop
while True:
    # Get the player's move
    while True:
        try:
            column = int(input(f"{players[current_player]}'s turn. Choose a column (0-{board.shape[1] - 1}): "))
            if column < 0 or column >= board.shape[1]:
                raise ValueError
            if board[:, column].any():
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a number between 0 and", board.shape[1] - 1, "and choose a column that is not full.")

    # Place the player's piece on the board
    for row in range(board.shape[0] - 1, -1, -1):
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
