import numpy as np

# Create the game board
board = np.zeros((10, 10))

# Define the players' symbols
player1_symbol = "X"
player2_symbol = "O"

# Define the current player
current_player = player1_symbol

# Define winning combinations
winning_combinations = [(0, 0, 0, 1, 0, 2),  # Horizontal
                        (0, 0, 1, 0, 2, 0),
                        (0, 0, 2, 0, 3, 0),
                        (0, 0, 3, 0, 4, 0),
                        (0, 1, 1, 1, 2, 1),  # Vertical
                        (0, 2, 1, 2, 2, 2),
                        (0, 3, 1, 3, 2, 3),
                        (0, 4, 1, 4, 2, 4),
                        (0, 0, 1, 1, 2, 2),  # Diagonal
                        (0, 2, 1, 3, 2, 4),
                        (0, 4, 1, 3, 2, 2),
                        (0, 6, 1, 5, 2, 4),
                        (0, 6, 1, 7, 2, 8),  # Diagonal
                        (0, 8, 1, 7, 2, 6),
                        (0, 4, 1, 5, 2, 6),
                        (0, 2, 1, 1, 2, 0)]

# Start the game loop
while True:
    # Get the current player's input
    print(f"It's {current_player}'s turn.")
    column = int(input("Choose a column (0-9): "))

    # Check if the column is valid
    if column < 0 or column > 9:
        print("Invalid column. Please choose a column between 0 and 9.")
        continue

    # Check if the column is full
    if board[0, column] != 0:
        print("This column is full. Please choose another column.")
        continue

    # Place the player's piece in the column
    row = 0
    while board[row, column] == 0:
        row += 1
    board[row, column] = current_player

    # Check if the player has won
    for combination in winning_combinations:
        if board[combination[0], combination[1]] == current_player and \
           board[combination[2], combination[3]] == current_player and \
           board[combination[4], combination[5]] == current_player:
            print(f"{current_player} wins!")
            break

    # Check if the game is a draw
    if np.all(board != 0):
        print("It's a draw!")
        break

    # Switch to the other player
    if current_player == player1_symbol:
        current_player = player2_symbol
    else:
        current_player = player1_symbol

    # Print the game board
    print(board)
