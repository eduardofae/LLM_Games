import numpy as np

def jdv():
    # Initialize the game board
    board = np.zeros((3, 3))

    # Initialize the turn counter
    turn = 0

    # Initialize the game status
    game_over = False

    # Main game loop
    while not game_over:
        # Print the game board
        print(board)

        # Get the player's move
        if turn % 2 == 0:
            player = 1
        else:
            player = 2

        move = int(input(f"Player {player}, enter your move (1-9): "))

        # Check if the move is valid
        if move < 1 or move > 9 or board[move // 3, move % 3] != 0:
            print("Invalid move. Try again.")
            continue

        # Place the player's piece on the board
        board[move // 3, move % 3] = player

        # Check if the player has won
        if check_win(board, player):
            print(f"Player {player} wins!")
            game_over = True
            break

        # Check if the game is a draw
        if np.all(board != 0):
            print("Draw!")
            game_over = True
            break

        # Increment the turn counter
        turn += 1

# Function to check if a player has won
def check_win(board, player):
    # Check the rows
    for i in range(3):
        if np.all(board[i, :] == player):
            return True

    # Check the columns
    for j in range(3):
        if np.all(board[:, j] == player):
            return True

    # Check the diagonals
    if np.all(board.diagonal() == player):
        return True
    if np.all(np.flip(board).diagonal() == player):
        return True

    # No win
    return False

# Play the game
jdv()
