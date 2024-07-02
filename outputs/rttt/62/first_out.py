import numpy as np

# Create the game board
board = np.zeros((3, 3))

# Define the players
player1 = 'X'
player2 = 'O'

# Define the winning conditions
winning_conditions = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

# Start the game
while True:
    # Get the player's input
    player_input = input("Enter a position (1-9): ")

    # Check if the input is valid
    if not player_input.isdigit() or int(player_input) < 1 or int(player_input) > 9:
        print("Invalid input. Please enter a number between 1 and 9.")
        continue

    # Convert the input to an index
    index = int(player_input) - 1

    # Check if the space is free
    if board[index] != 0:
        print("That space is already taken. Please choose another space.")
        continue

    # Place the player's piece on the board
    if player1 == 'X':
        board[index] = 'X'
        player1, player2 = player2, player1
    else:
        board[index] = 'O'
        player1, player2 = player1, player2

    # Check if the player has won
    for winning_condition in winning_conditions:
        if board[winning_condition[0]] == board[winning_condition[1]] == board[winning_condition[2]] != 0:
            print(f"{player1} wins!")
            break

    # Check if the game is a draw
    if np.all(board != 0):
        print("It's a draw!")
        break

    # Print the board
    print(board)
