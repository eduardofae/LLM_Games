def check_winner(board):
    """
    Check if there is a winner in the given board.

    Args:
        board (list): A list of lists representing the game board.

    Returns:
        int: The player number of the winner, or 0 if there is no winner yet.
    """

    # Check for horizontal wins
    for row in board:
        if len(set(row)) == 1 and row[0] != 0:
            return row[0]

    # Check for vertical wins
    for col in range(len(board)):
        column = [row[col] for row in board]
        if len(set(column)) == 1 and column[0] != 0:
            return column[0]

    # Check for diagonal wins
    diagonal1 = [board[i][i] for i in range(len(board))]
    diagonal2 = [board[i][len(board)-i-1] for i in range(len(board))]
    if len(set(diagonal1)) == 1 and diagonal1[0] != 0:
        return diagonal1[0]
    if len(set(diagonal2)) == 1 and diagonal2[0] != 0:
        return diagonal2[0]

    # Check for tie
    if all(all(row) for row in board):
        return -1

    # No winner yet
    return 0


def play_jdv():
    """
    Play a game of jdv.
    """

    # Get the game board size from the user
    board_size = int(input("Enter the game board size (e.g. 3 for a 3x3 board): "))

    # Initialize the game board
    board = [[0 for _ in range(board_size)] for _ in range(board_size)]

    # Set the current player to 1
    player = 1

    # Set the number of wins for each player
    wins = {1: 0, 2: 0}

    # Game loop
    while True:
        # Display the game board
        for row in board:
            print(" ".join(str(cell) for cell in row))
        print()

        # Get the player's move
        try:
            row, col = map(int, input("Player {}'s turn (row, column): ".format(player)).split())
        except ValueError:
            print("Invalid input. Please try again.")
            continue

        # Check if the move is valid
        if not (0 <= row < board_size and 0 <= col < board_size):
            print("Invalid move. Please try again.")
            continue
        if board[row][col] != 0:
            print("Invalid move. Please try again.")
            continue

        # Place the player's piece on the board
        board[row][col] = player

        # Check for a winner or tie
        winner = check_winner(board)
        if winner != 0:
            if winner == -1:
                print("Tie!")
            else:
                print("Player {} wins!".format(winner))
                wins[winner] += 1
            break

        # Switch to the other player
        player = 3 - player

    # Print the number of wins for each player
    print("Player 1 wins:", wins[1])
    print("Player 2 wins:", wins[2])

    # Ask if the players want to play again
    play_again = input("Do you want to play again? (y/n) ")
    if play_again == "y":
        play_jdv()
    else:
        print("Thanks for playing!")


# Play the game
play_jdv()
