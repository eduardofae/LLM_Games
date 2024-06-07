def jdv():
    """
    A simple game of tic-tac-toe.

    The game is played on a 3x3 grid. Players take turns placing their pieces in a free space.
    The first player to make a line of three of their pieces wins. If there are no more free spaces, the game is declared a draw.
    """

    # Create a game board.
    game_board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    # Create a list of player symbols.
    players = ["X", "O"]

    # Keep track of the current player.
    current_player_symbol = "X"

    # Keep track of the number of moves made.
    num_moves = 0

    # Game loop.
    while True:
        # Get the player's move.
        try:
            row, col = input("Enter your move (row, column): ").split()
            row = int(row) - 1
            col = int(col) - 1
        except ValueError:
            print("Invalid move. Please try again.")
            continue

        # Check if the move is valid.
        if not (0 <= row < 3 and 0 <= col < 3 and game_board[row][col] == " "):
            print("Invalid move. Please try again.")
            continue

        # Place the player's piece on the board.
        game_board[row][col] = current_player_symbol

        # Check if the player has won.
        if check_win(game_board, current_player_symbol):
            print(f"{current_player_symbol} wins!")
            break

        # Check if the game is a draw.
        if num_moves == 9:
            print("Draw!")
            break

        # Switch to the other player.
        current_player_symbol = "X" if current_player_symbol == "O" else "O"

        # Increment the number of moves.
        num_moves += 1


def check_win(game_board, player_symbol):
    """
    Checks if the player has won.

    Args:
        game_board: The game board.
        player_symbol: The player's symbol.

    Returns:
        True if the player has won, False otherwise.
    """

    # Check if the player has won horizontally.
    for row in game_board:
        if all(x == player_symbol for x in row):
            return True

    # Check if the player has won vertically.
    for col in range(3):
        if all(x == player_symbol for x in [game_board[0][col], game_board[1][col], game_board[2][col]]):
            return True

    # Check if the player has won diagonally.
    if all(x == player_symbol for x in [game_board[0][0], game_board[1][1], game_board[2][2]]):
        return True
    if all(x == player_symbol for x in [game_board[0][2], game_board[1][1], game_board[2][0]]):
        return True

    # The player has not won.
    return False


if __name__ == "__main__":
    jdv()
