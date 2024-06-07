import numpy as np

# Constants
BOARD_SIZE = 3
PLAYER1 = 1
PLAYER2 = 2

def check_game_status(board):
    # Check rows
    if np.any(np.all(board == row[0], axis=1)) and row[0] != 0:
        return row[0]

    # Check columns
    if np.any(np.all(board == col[0], axis=0)) and col[0] != 0:
        return col[0]

    # Check diagonals
    diag1 = np.array([[board[i, i] for i in range(BOARD_SIZE)]])
    diag2 = np.array([[board[i, BOARD_SIZE - 1 - i] for i in range(BOARD_SIZE)]])
    if np.all(diag1 == diag1[0, 0]) or np.all(diag2 == diag2[0, 0]):
        return diag1[0, 0]

    # Check for draw
    if np.all(board != 0):
        return -1  # Draw

    # No winner yet
    return 0

def get_player_move(player):
    while True:
        try:
            move = tuple(map(int, input(f"Player {player}, enter your move (row, column): ").split()))
            if not (0 <= move[0] < BOARD_SIZE and 0 <= move[1] < BOARD_SIZE):
                print("Invalid move. Please enter a valid row and column.")
                continue
            return move
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")

def play_jdv():
    # Create the game board
    board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)

    # Set the players
    players = [PLAYER1, PLAYER2]

    # Game loop
    while True:
        # Get the current player
        player = players[0]

        # Get the player's move
        move = get_player_move(player)

        # Handle invalid moves
        if board[move] != 0:
            print("Invalid move. This space is already occupied.")
            continue

        # Place the player's piece on the board
        board[move] = player

        # Check if the game has ended
        winner = check_game_status(board)
        if winner != 0:
            if winner == -1:
                print("Draw!")
            else:
                print(f"Player {winner} wins!")
            break

        # Switch players
        players = players[1:] + players[:1]

    # Ask the user if they want to play again
    while True:
        play_again = input("Do you want to play again? (y/n) ")
        if play_again.lower() == "y":
            # Reset the game board and player's turn
            board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)
            players = [PLAYER1, PLAYER2]
            play_jdv()
            break
        elif play_again.lower() == "n":
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

# Play the game
play_jdv()
