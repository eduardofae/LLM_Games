import numpy as np

# Create the game board
board = np.zeros((10, 10))

# Create a list of the players
players = ['X', 'O']

# Create a variable to keep track of the current player
current_player = 0

# Create a variable to keep track of the number of turns
turns = 0

# Create a variable to keep track of the winner
winner = None

# Create a function to check if there is a winner
def check_winner():
    # Check the rows
    for row in board:
        if np.all(row == players[current_player]):
            return True

    # Check the columns
    for col in board.T:
        if np.all(col == players[current_player]):
            return True

    # Check the diagonals
    diagonals = [board.diagonal(), np.flip(board).diagonal()]
    for diagonal in diagonals:
        if np.all(diagonal == players[current_player]):
            return True

    return False

# Create a function to place a piece
def place_piece(col):
    # Check if the column is full
    if board[9, col] != 0:
        return False

    # Find the lowest free space in the column
    row = 9
    while board[row, col] != 0:
        row -= 1

    # Place the piece
    board[row, col] = players[current_player]

    return True

# Create a function to switch the current player
def switch_player():
    global current_player
    current_player = (current_player + 1) % 2

# Create a function to run the game
def run_game():
    global winner, turns

    # Keep track of the number of turns
    turns += 1

    # Get the column from the current player
    col = int(input("Enter a column (0-9): "))

    # Place the piece
    if not place_piece(col):
        print("Invalid move. Try again.")
        return

    # Check if there is a winner
    if check_winner():
        winner = players[current_player]
        return

    # Switch the current player
    switch_player()

# Run the game
while winner is None and turns < 100:
    run_game()

# Print the winner
if winner is not None:
    print(f"{winner} wins!")
else:
    print("Draw!")
