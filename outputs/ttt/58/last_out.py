import numpy as np

def check_winner(board):
    # Check if there is a line of 3 adjacent pieces
    for player in [1, 2]:
        for i in range(3):
            # Check rows
            if board[i, :].sum() == 3*player:
                return player

            # Check columns
            if board[:, i].sum() == 3*player:
                return player

        # Check diagonals
        if board[0, 0] + board[1, 1] + board[2, 2] == 3*player:
            return player
        if board[0, 2] + board[1, 1] + board[2, 0] == 3*player:
            return player

    # If there is no winner, return 0
    return 0

def print_board(board):
    for i in range(3):
        for j in range(3):
            print(board[i, j], end=" ")
        print()

if __name__ == "__main__":
    # Create the game board
    game_board = np.zeros((3, 3), dtype=int)

    # Set the current player
    current_player = 1

    # Set of all moves made
    moves = set()

    # Game loop
    while True:
        # Print the board
        print_board(game_board)

        # Get the player's move
        while True:
            try:
                move = int(input(f"Player {current_player}, enter your move (1-9): "))
                if move < 1 or move > 9:
                    raise ValueError("Invalid move. Please enter a number between 1 and 9.")
                if move in moves:
                    raise ValueError("Invalid move. That space is already occupied.")
                break
            except ValueError as e:
                print(e)

        # Add the move to the set of moves
        moves.add(move)

        # Convert the move to a row and column index
        row = (move - 1) // 3
        col = (move - 1) % 3

        # Place the player's piece on the board
        game_board[row, col] = current_player

        # Check if the player has won
        winner = check_winner(game_board)
        if winner != 0:
            print(f"Player {winner} has won!")
            break

        # Check if the game is a draw
        if ~game_board.any():
            print("Draw!")
            break

        # Switch the current player
        current_player = 3 - current_player
