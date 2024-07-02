import numpy as np

# Create the game board
board = np.zeros((10, 10))

# Define the players' turns
player1_turn = True

# Define the winning states
winning_states = [
    [[1, 1, 1], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [1, 1, 1], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [1, 1, 1]],
    [[1, 0, 0], [1, 0, 0], [1, 0, 0]],
    [[0, 1, 0], [0, 1, 0], [0, 1, 0]],
    [[0, 0, 1], [0, 0, 1], [0, 0, 1]],
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
    [[0, 0, 1], [0, 1, 0], [1, 0, 0]],
]

# Define the game loop
while True:
    # Print the game board
    print(board)

    # Get the player's move
    if player1_turn:
        column = int(input("Player 1, choose a column (0-9): "))
    else:
        column = int(input("Player 2, choose a column (0-9): "))

    # Check if the move is valid
    if column < 0 or column > 9 or board[9, column] != 0:
        print("Invalid move")
        continue

    # Drop the piece
    row = 9
    while row >= 0 and board[row, column] == 0:
        row -= 1

    board[row + 1, column] = 1 if player1_turn else 2

    # Check if the game is over
    for winning_state in winning_states:
        if np.array_equal(board, winning_state):
            print("Player" + ("1" if player1_turn else "2") + " wins!")
            break

    if np.all(board != 0):
        print("Draw!")
        break

    # Switch the player's turn
    player1_turn = not player1_turn
