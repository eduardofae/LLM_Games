import numpy as np

# Create the game board
board = np.zeros((3, 3))

# Create a list of the possible winning combinations
winning_combinations = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]

# Define the players
players = ["X", "O"]

# Start the game
player_turn = 0
while True:
    # Check if the game is already over
    if np.any(board != 0) and not any(np.all(board[combination] == players[player_turn]) for combination in winning_combinations):
        # Game is not over, continue with the player's turn
        while True:
            try:
                move = int(input(f"Player {players[player_turn]}, enter your move (1-9): ")) - 1
                if move < 0 or move > 8:
                    raise ValueError("Invalid move. Please enter a number between 1 and 9.")
                if board[move] != 0:
                    raise ValueError("Invalid move. That space is already occupied.")
                break
            except ValueError as e:
                print(e)

        # Place the player's piece on the board
        board[move] = players[player_turn]
    else:
        # Game is over, declare the winner or draw
        if np.all(board != 0):
            print("The game is a draw.")
        else:
            print(f"Player {players[player_turn]} wins!")
        break

    # Check if the player has won
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] != 0:
            print(f"Player {players[player_turn]} wins!")
            break

    # Switch to the other player's turn
    player_turn = (player_turn + 1) % 2
