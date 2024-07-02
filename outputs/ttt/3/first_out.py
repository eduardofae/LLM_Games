import numpy as np

def check_winner(board):
    # Check rows
    for i in range(3):
        if board[i, 0] == board[i, 1] == board[i, 2] != 0:
            return board[i, 0]

    # Check columns
    for j in range(3):
        if board[0, j] == board[1, j] == board[2, j] != 0:
            return board[0, j]

    # Check diagonals
    if board[0, 0] == board[1, 1] == board[2, 2] != 0:
        return board[0, 0]
    if board[0, 2] == board[1, 1] == board[2, 0] != 0:
        return board[0, 2]

    # Check for draw
    if np.all(board != 0):
        return -1

    # No winner yet
    return 0

def play_jdv():
    # Create the game board
    board = np.zeros((3, 3), dtype=int)

    # Set the players
    players = [1, 2]

    # Game loop
    while True:
        # Get the current player
        player = players[0]

        # Get the player's move
        while True:
            try:
                move = tuple(map(int, input(f"Player {player}, enter your move (row, column): ").split()))
                if move[0] < 0 or move[0] > 2 or move[1] < 0 or move[1] > 2:
                    print("Invalid move. Please enter a valid row and column.")
                    continue
                if board[move] != 0:
                    print("This space is already occupied. Please choose another one.")
                    continue
                break
            except ValueError:
                print("Invalid input. Please enter two integers separated by a space.")

        # Place the player's piece on the board
        board[move] = player

        # Check if the player has won
        winner = check_winner(board)
        if winner != 0:
            if winner == -1:
                print("Draw!")
            else:
                print(f"Player {winner} wins!")
            break

        # Switch players
        players = players[1:] + players[:1]

# Play the game
play_jdv()