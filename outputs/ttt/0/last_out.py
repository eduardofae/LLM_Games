
# Import the necessary libraries.
import numpy as np

# Define the game board.
board = np.zeros((3, 3))

# Define the players.
players = ["X", "O"]

# Define the game loop function.
def game_loop():
    while True:
        # Get the current player.
        player = players[0]

        # Get the player's move.
        while True:
            try:
                move = input(f"Player {player}, enter your move (row, column): ").split(',')
                move = [int(x) for x in move]
                if 0 <= move[0] < 3 and 0 <= move[1] < 3 and board[move[0], move[1]] == 0:
                    break
                else:
                    print("Invalid move. The space is already occupied.")
            except ValueError:
                print("Invalid input. Please enter two integers separated by a comma.")

        # Place the player's piece on the board.
        board[move[0], move[1]] = player

        # Print the game board.
        print(board)

        # Check if the player has won.
        if (
            (board[move[0], 0] == player and board[move[0], 1] == player and board[move[0], 2] == player)
            or (board[0, move[1]] == player and board[1, move[1]] == player and board[2, move[1]] == player)
            or (board[0, 0] == player and board[1, 1] == player and board[2, 2] == player)
            or (board[0, 2] == player and board[1, 1] == player and board[2, 0] == player)
        ):
            print(f"Player {player} wins!")
            break

        # Check if the game is a draw.
        if np.all(board != 0):
            print("Draw!")
            break

        # Switch to the next player.
        players = players[1:]

# Add a way to reset the game.
def reset_game():
    global board
    board = np.zeros((3, 3))

# Add a way to handle ties.
def check_tie():
    if np.all(board != 0) and not (
        (board[0, 0] == board[0, 1] == board[0, 2] != 0)
        or (board[0, 0] == board[1, 0] == board[2, 0] != 0)
        or (board[0, 0] == board[1, 1] == board[2, 2] != 0)
        or (board[0, 2] == board[1, 2] == board[2, 2] != 0)
        or (board[1, 0] == board[1, 1] == board[1, 2] != 0)
        or (board[2, 0] == board[2, 1] == board[2, 2] != 0)
    ):
        return True
    else:
        return False

# Start the game loop.
while True:
    game_loop()
    if check_tie():
        print("Tie!")
    choice = input("Do you want to play again? (y/n): ")
    if choice == "n":
        break
    else:
        reset_game()
