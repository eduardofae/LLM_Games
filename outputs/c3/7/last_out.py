import numpy as np

# Create the game board
board = np.zeros((10, 10))

# Create the players
player1 = 1
player2 = -1

# Create a list of the columns
columns = [i for i in range(10)]

# Create a list of the diagonals
diagonals = [[(i, j) for i in range(10) for j in range(10) if i == j],
              [(i, j) for i in range(10) for j in range(10) if i + j == 9]]

# Create a list of the rows
rows = [[(i, j) for i in range(10) for j in range(10) if i == k] for k in range(10)]

# Create a list of all the winning combinations
winning_combinations = rows + columns + diagonals

# Create a function to check if a player has won
def check_win(player):
    for combination in winning_combinations:
        if all(board[i, j] == player for i, j in combination):
            return True
    return False

# Create a function to place a piece on the board
def place_piece(player, column):
    if column not in columns:
        raise ValueError("Invalid column number")

    for i in range(9, -1, -1):
        if board[i, column] == 0:
            board[i, column] = player
            break
    else:
        raise ValueError("Column is already full")

# Create a function to check if the game is over
def check_over():
    return all(board[i, j] != 0 for i in range(10) for j in range(10))

# Create a function to play the game
def play_game():
    # Set the current player to player 1
    current_player = player1

    # While the game is not over
    while not check_over():
        try:
            # Get the column where the player wants to place their piece
            column = int(input(f"Player {current_player}, choose a column (0-9): "))

            # Check if the input is a valid integer
            if not isinstance(column, int) or column not in range(10):
                raise ValueError("Invalid column number")

            # Place the piece on the board
            place_piece(current_player, column)

            # Check if the current player has won
            if check_win(current_player):
                # Print the winning message
                print(f"Player {current_player} wins!")

                # Break out of the loop
                break

            # Switch the current player
            current_player = -current_player
        except ValueError as e:
            print(e)

    # If the game is over and no one has won
    if check_over():
        # Print the draw message
        print("Draw!")

# Create a function to display the game board
def display_board():
    for row in board:
        print(" ".join([str(cell) for cell in row]))

# Play the game
play_game()

# Display the game board
display_board()
