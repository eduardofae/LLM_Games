# Import the necessary libraries.
import numpy as np

# Define the game board.
game_board = np.zeros((3, 3))

# Define the player symbols.
player1_symbol = 'X'
player2_symbol = 'O'

# Define the current player.
current_player = player1_symbol

# Define the number of moves that have been made.
num_moves = 0

# Define the game loop.
while True:
    # Display the game board.
    print(game_board)

    # Get the player's move.
    try:
        row, col = map(int, input("Enter your move (row, col): ").split())
    except ValueError:
        print("Invalid input. Please enter two integers separated by a comma.")
        continue

    # Check if the move is valid.
    if row < 0 or row > 2 or col < 0 or col > 2 or game_board[row, col] != 0:
        print("Invalid move. Please enter a valid row and column.")
        continue

    # Place the player's piece on the board.
    game_board[row, col] = current_player

    # Increment the number of moves.
    num_moves += 1

    # Check if the player has won.
    if check_win(game_board, current_player):
        print(f"{current_player} wins!")
        break

    # Check if the game is a draw.
    if num_moves == 9:
        print("Draw.")
        break

    # Switch to the other player.
    current_player = player2_symbol if current_player == player1_symbol else player1_symbol

# Define the function to check if a player has won.
def check_win(board, player):
    # Check for horizontal wins.
    for i in range(3):
        if np.all(board[i, :] == player):
            return True

    # Check for vertical wins.
    for j in range(3):
        if np.all(board[:, j] == player):
            return True

    # Check for diagonal wins.
    if np.all(board.diagonal() == player):
        return True
    if np.all(np.flip(board).diagonal() == player):
        return True

    # Otherwise, the player has not won.
    return False

# Ask the user if they want to play again.
while True:
    play_again = input("Do you want to play again? (y/n): ")
    if play_again == 'y':
        # Reset the game board.
        game_board = np.zeros((3, 3))

        # Reset the current player.
        current_player = player1_symbol

        # Reset the number of moves.
        num_moves = 0

        # Start the game loop.
        continue
    elif play_again == 'n':
        # Exit the program.
        break
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
