def jdv():
    """
    It's a game named jdv. In this game, 2 players take turns placing their pieces in a free space of a 3x3 grid, until one of them makes a line with 3 (horizontally, vertically or diagonally) adjacent pieces, in which case the person that made the line loses, and the opponent is the winner.
    If there are no more free spaces, the game is declared a draw.
    """
    # Create the board
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

    # Create a list of the players
    players = ["X", "O"]

    # Set the current player to the first player
    current_player = 0

    # Game loop
    while True:
        # Get the current player's move
        move = input(f"{players[current_player]}'s turn: ")

        # Check if the move is valid
        if not (move[0].isdigit() and move[1].isdigit() and 0 <= int(move[0]) < 3 and 0 <= int(move[1]) < 3 and board[int(move[0])][int(move[1])] == " "):
            print("Invalid move. Try again.")
            continue

        # Place the current player's piece on the board
        board[int(move[0])][int(move[1])] = players[current_player]

        # Check if the current player has won
        if check_win(board, players[current_player]):
            print(f"{players[current_player]} wins!")
            break

        # Check if there are no more free spaces
        if check_draw(board):
            print("Draw!")
            break

        # Switch to the other player
        current_player = (current_player + 1) % 2

def check_win(board, player):
    """
    Check if the given player has won the game.

    Args:
        board (list): The game board.
        player (str): The player to check.

    Returns:
        bool: True if the player has won, False otherwise.
    """
    # Check the rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check the columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check the diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    # No win yet
    return False


def check_draw(board):
    """
    Check if the game is a draw.

    Args:
        board (list): The game board.

    Returns:
        bool: True if the game is a draw, False otherwise.
    """
    return all(cell != " " for cell in board[0] + board[1] + board[2])

if __name__ == "__main__":
    jdv()
