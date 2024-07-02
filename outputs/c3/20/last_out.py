def main():
    # Create the game board
    board = np.zeros((10, 10), dtype=int)

    # Create a list of players
    players = [1, 2]

    # Main game loop
    while True:
        for player in players:
            try:
                # Get the player's move
                move = input("Player {}'s turn. Enter a column number (1-10): ".format(player))

                # Check if the move is valid
                if not (1 <= int(move) <= 10):
                    raise ValueError("Invalid move. Please enter a column number between 1 and 10.")

                # Check if the column is full
                if board[:, int(move)-1].all():
                    raise ValueError("Column {} is full. Please choose another column.".format(move))

                # Place the player's piece on the board
                board[board[:, int(move)-1] == 0, int(move)-1] = player

                # Check if the player has won
                if np.any(np.sum(board, axis=0) == 3 * player) or np.any(np.sum(board, axis=1) == 3 * player) or np.any(np.sum(np.diag(board)) == 3 * player) or np.any(np.sum(np.flipud(board), axis=1) == 3 * player):
                    print("Player {} wins!".format(player))
                    return

                # Check if the game is a draw
                if np.all(board != 0):
                    print("The game is a draw.")
                    return

            except ValueError as e:
                print(e)

    # Print the game board
    print(board)

# Run the main function
if __name__ == "__main__":
    main()
