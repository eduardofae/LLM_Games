# Import the necessary module
import numpy as np

# Define the game board
board = np.zeros((3, 3))

# Define the players
player1 = 'X'
player2 = 'O'

# Define the game status
game_status = 'ongoing'

# Define the winning combinations
winning_combinations = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

# Define the current player
current_player = player1

# Main game loop
while game_status == 'ongoing':
    # Print the game board
    print(board)

    # Get the player's move
    move = int(input(f"{current_player}'s turn (enter a number between 1 and 9): ")) - 1

    # Check if the move is valid
    if board[move // 3, move % 3] == 0:
        # Place the player's piece on the board
        board[move // 3, move % 3] = current_player

        # Check if the player has won
        for combination in winning_combinations:
            if board[combination[0] // 3, combination[0] % 3] == board[combination[1] // 3, combination[1] % 3] == board[combination[2] // 3, combination[2] % 3] != 0:
                game_status = 'finished'
                winner = current_player
                break

        # Check if the game is a draw
        if np.all(board != 0):
            game_status = 'draw'

        # Switch the current player
        current_player = player1 if current_player == player2 else player2
    else:
        print("Invalid move. Please try again.")

# Print the game result
if game_status == 'finished':
    print(f"{winner} wins!")
elif game_status == 'draw':
    print("Draw!")
