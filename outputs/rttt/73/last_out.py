import os

def clear_console():
    """
    Clears the console.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def display_board(board):
    """
    Displays the game board.

    Args:
        board: The game board.
    """

    print("\n")
    for row in board:
        for cell in row:
            print(cell, end=" ")
        print("\n")


def get_player_input(player):
    """
    Gets the player's input.

    Args:
        player: The player's number (1 or 2).

    Returns:
        The player's move.
    """

    while True:
        try:
            move = input("Player {}: Enter your move (row, column): ".format(player))
            row, column = move.split(",")
            row = int(row)
            column = int(column)
            if not (0 <= row < 3 and 0 <= column < 3):
                raise ValueError
            return row, column
        except ValueError:
            print("Invalid move. Please try again.")


def check_winner(board):
    """
    Checks if there is a winner in the given board.

    Args:
        board: The game board.

    Returns:
        The winner's number (1 or 2), or 0 if there is no winner yet.
    """

    # Check for a winner in each row.
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    # Check for a winner in each column.
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check for a winner in each diagonal.
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    # No winner yet.
    return 0


def play_game():
    """
    Plays the game.
    """

    # Create the game board.
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    # Get the names of the two players.
    player1_name = input("Player 1, enter your name: ")
    player2_name = input("Player 2, enter your name: ")

    # Determine who goes first.
    first_player = input("Who goes first? (1 or 2): ")

    # Keep track of the current player.
    current_player = first_player

    # Keep track of the number of moves that have been made.
    num_moves = 0

    # Play the game until someone wins or there is a draw.
    while True:
        # Clear the console.
        clear_console()

        # Display the game board.
        display_board(board)

        # Announce the current player's turn.
        print("Player {}'s turn.".format(current_player))

        # Get the current player's move.
        if current_player == "1":
            move = get_player_input(1)
        else:
            move = get_player_input(2)

        # Make the move.
        board[move[0]][move[1]] = current_player

        # Increment the number of moves.
        num_moves += 1

        # Check if there is a winner.
        winner = check_winner(board)
        if winner != 0:
            # Clear the console.
            clear_console()

            # Display the game board.
            display_board(board)

            # Announce the winner.
            if winner == "1":
                print("Congratulations, {}!".format(player1_name))
            else:
                print("Congratulations, {}!".format(player2_name))
            break

        # Check if there is a draw.
        if num_moves == 9:
            # Clear the console.
            clear_console()

            # Display the game board.
            display_board(board)

            # Announce the draw.
            print("Draw!")
            break

        # Switch to the other player.
        if current_player == "1":
            current_player = "2"
        else:
            current_player = "1"


if __name__ == "__main__":
    print("Welcome to jdv! Let's play.")
    play_game()
