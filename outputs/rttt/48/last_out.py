import numpy as np

def check_winner(board):
    """Checks if there is a winner in the given board.

    Args:
        board: A 3x3 numpy array representing the game board.

    Returns:
        The player who won the game, or None if there is no winner yet.
    """
    # Check for horizontal wins
    for row in range(3):
        if np.all(board[row] == board[row][0]) and board[row][0] != 0:
            return board[row][0]

    # Check for vertical wins
    for col in range(3):
        if np.all(board[:, col] == board[0, col]) and board[0, col] != 0:
            return board[0, col]

    # Check for diagonal wins
    if np.all(np.diag(board) == board[0, 0]) and board[0, 0] != 0:
        return board[0, 0]
    if np.all(np.diag(np.flipud(board)) == board[0, 2]) and board[0, 2] != 0:
        return board[0, 2]

    # No winner yet
    return None


def check_draw(board):
    """Checks if the game is a draw.

    Args:
        board: A 3x3 numpy array representing the game board.

    Returns:
        True if the game is a draw, False otherwise.
    """
    return np.all(board != 0)


def play_jdv():
    """Plays a game of jdv."""

    # Create a 3x3 game board
    board = np.zeros((3, 3), dtype=int)

    # Get the player names
    player1 = input("Player 1 name: ")
    player2 = input("Player 2 name: ")

    # Set the current player to player 1
    current_player = 1

    # Game state: ongoing, won, draw
    game_state = "ongoing"

    # Loop until the game is over
    while game_state == "ongoing":

        # Display the game board
        print_board(board)

        # Get the player's move
        try:
            row = int(input(f"{player1}'s turn. Row: "))
            col = int(input(f"{player1}'s turn. Column: "))
        except ValueError:
            print("Invalid input: please enter an integer value.")
            continue

        # Check if the move is valid
        if row < 0 or row > 2 or col < 0 or col > 2 or board[row, col] != 0:
            print("Invalid move. Please choose an empty space.")
            continue

        # Place the player's piece on the board
        board[row, col] = current_player

        # Check if there is a winner
        winner = check_winner(board)
        if winner is not None:
            game_state = "won"
            print(f"{winner} wins!")

        # Check if there is a draw
        draw = check_draw(board)
        if draw:
            game_state = "draw"
            print("Draw!")

        # Switch to the other player
        current_player = 2 if current_player == 1 else 1


def print_board(board):
    """Prints the current state of the game board.

    Args:
        board: A 3x3 numpy array representing the game board.
    """
    for row in board:
        print("|".join(['X' if x == 1 else 'O' if x == 2 else ' ' for x in row]))


# Main game function
if __name__ == "__main__":
    while True:
        # Play a game of jdv
        play_jdv()

        # Ask the players if they want to play again
        play_again = input("Play again (y/n): ")
        if play_again.lower() != "y":
            break

# Additional features to consider for future development:

def play_against_ai():
    """Plays a game of jdv against an AI opponent."""

    # Implement the AI opponent's logic here

def create_different_game_modes():
    """Creates different game modes with variations in the rules or board size."""

    # Implement different game modes here, such as:
    # - Multiple pieces per turn
    # - Larger board size
    # - Timed matches

def enable_online_multiplayer():
    """Enables online multiplayer mode."""

    # Implement the online multiplayer functionality here, such as:
    # - Server-client architecture
    # - Matchmaking system
    # - Real-time game updates
