import numpy as np

# Create the game board
board = np.zeros((3, 3))

# Define the players
players = ["X", "O"]

# Define the game state
game_state = "ongoing"

# Get the player's input
def get_player_input(player):
    while True:
        try:
            row = int(input(f"Player {player}, enter the row (1-3): "))
            col = int(input(f"Player {player}, enter the column (1-3): "))
            if row < 1 or row > 3 or col < 1 or col > 3:
                print("Invalid input. Please enter a valid row and column.")
            elif board[row - 1][col - 1] != 0:
                print("Space already taken. Please choose another space.")
            else:
                return row - 1, col - 1
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Check if the game is over
def check_game_over(board):
    # Check for a win
    for i in range(3):
        if np.all(board[i, :] == board[i, 0]) and board[i, 0] != 0:
            return True, board[i, 0]
        if np.all(board[:, i] == board[0, i]) and board[0, i] != 0:
            return True, board[0, i]

    # Check for a diagonal win
    if np.all(board.diagonal() == board[0, 0]) and board[0, 0] != 0:
        return True, board[0, 0]
    if np.all(np.flip(board).diagonal() == board[0, 2]) and board[0, 2] != 0:
        return True, board[0, 2]

    # Check for a draw
    if np.all(board != 0):
        return True, "draw"

    # The game is still ongoing
    return False, None

# Play the game
while game_state == "ongoing":
    for player in players:
        # Get the player's input
        row, col = get_player_input(player)

        # Place the player's piece on the board
        board[row, col] = player

        # Check if the game is over
        game_over, winner = check_game_over(board)

        # Print the game board
        print(board)

        if game_over:
            if winner == "draw":
                print("The game is a draw.")
            else:
                print(f"Player {winner} wins!")
            break
