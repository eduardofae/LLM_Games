import numpy as np

def jdv():
    # Create a 3x3 board
    board = np.zeros((3, 3), dtype=int)

    # Get the player names
    player1 = input("Player 1 name: ")
    player2 = input("Player 2 name: ")

    # Set the current player to player 1
    current_player = player1

    # Game loop
    while True:
        # Print the board
        print(board)

        # Get the player's move
        try:
            row, col = map(int, input("Enter your move (row, col): ").split())
        except ValueError:
            print("Invalid input. Please enter two integers separated by a comma.")
            continue

        # Check if the move is valid
        if not (0 <= row < 3 and 0 <= col < 3):
            print("Invalid move. Please enter a row and column between 0 and 2.")
            continue
        if board[row, col] != 0:
            print("Invalid move. That space is already occupied. Choose a different one.")
            continue

        # Place the player's piece on the board
        board[row, col] = 1 if current_player == player1 else 2

        # Increment the number of moves made
        num_moves += 1

        # Check if the player has won
        if check_win(board, current_player):
            print(f"{current_player} wins in {num_moves} moves!")
            break

        # Check if the game is a draw
        if np.all(board != 0):
            print("Draw!")
            break

        # Switch the current player
        current_player = player2 if current_player == player1 else player1

def check_win(board, player):
    """
    Checks if the given player has won the game.

    Args:
        board: The game board.
        player: The player to check.

    Returns:
        True if the player has won, False otherwise.
    """

    # Check for a win in each row
    for row in range(3):
        if np.all(board[row, :] == player):
            return True

    # Check for a win in each column
    for col in range(3):
        if np.all(board[:, col] == player):
            return True

    # Check for a win in each diagonal
    if np.all(board.diagonal() == player) or np.all(np.flipud(board).diagonal() == player):
        return True

    return False

# Play again loop
while True:
    # Ask the players if they want to play again
    play_again = input("Do you want to play again? (y/n): ")

    # If the players don't want to play again, break out of the loop
    if play_again.lower() == "n":
        break

    # Reset the board
    board = np.zeros((3, 3), dtype=int)

    # Set the current player to player 1
    current_player = player1

    # Reset the number of moves made
    num_moves = 0

if __name__ == "__main__":
    jdv()
