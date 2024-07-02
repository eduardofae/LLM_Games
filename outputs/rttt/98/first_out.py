def jdv():
    """
    Plays a game of JDV.

    The game is played on a 3x3 grid. Two players take turns placing their pieces in a free space.
    The first player to make a line of three adjacent pieces wins. If there are no more free spaces, the game is declared a draw.
    """

    # Create the game board.
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]

    # Create a list of the players.
    players = ['X', 'O']

    # Get the first player's move.
    player = players[0]
    print(f"{player}'s turn.")
    row, col = map(int, input("Enter the row and column of your move (e.g. 1 2): ").split())

    # Place the player's piece on the board.
    board[row - 1][col - 1] = player

    # Check if the player has won.
    if check_win(board, player):
        print(f"{player} wins!")
        return

    # Switch to the other player.
    player = players[1]

    # Continue playing the game until someone wins or there are no more free spaces.
    while True:
        # Get the player's move.
        print(f"{player}'s turn.")
        row, col = map(int, input("Enter the row and column of your move (e.g. 1 2): ").split())

        # Place the player's piece on the board.
        board[row - 1][col - 1] = player

        # Check if the player has won.
        if check_win(board, player):
            print(f"{player} wins!")
            return

        # Check if there are no more free spaces.
        if not any(' ' in row for row in board):
            print("It's a draw!")
            return

        # Switch to the other player.
        player = players[0] if player == players[1] else players[1]

