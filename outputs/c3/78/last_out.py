import numpy as np

def play_connect_four():
    # Create the game board
    game_board = np.zeros((10, 10), dtype=int)

    # Set the current player's turn
    current_player = 1

    # Game loop
    while True:
        # Get the player's input
        column = get_player_input()

        # Check if the move is valid
        if not is_move_valid(game_board, column):
            print("Invalid move. Please choose a different column.")
            continue

        # Find the lowest free space in the column
        row = get_lowest_free_space(game_board, column)

        # Place the player's piece
        game_board[row, column] = current_player

        # Display the game board
        display_game_board(game_board)

        # Check if the player has won
        if check_for_win(game_board, current_player):
            print("Player {} wins!".format(current_player))
            break

        # Check if the game is a draw
        if np.all(game_board != 0):
            print("Draw!")
            break

        # Switch players
        current_player = 3 - current_player

def get_player_input():
    while True:
        try:
            column = int(input("Player {}: Enter the column (1-10): ".format(current_player))) - 1

            if not (0 <= column <= 9):
                raise ValueError("Invalid column")

            return column
        except ValueError as e:
            print(e)

def is_move_valid(game_board, column):
    # Check if the column is within the bounds of the board
    if not (0 <= column <= 9):
        return False

    # Check if the column is full
    if game_board[0, column] != 0:
        return False

    return True

def get_lowest_free_space(game_board, column):
    # Find the lowest free space in the column
    for row in range(9, -1, -1):
        if game_board[row, column] == 0:
            return row

def check_for_win(game_board, player):
    # Check rows, columns, and diagonals
    for i in range(10):
        # Check rows
        if np.all(game_board[i, :3] == player) or np.all(game_board[i, 3:6] == player) or np.all(game_board[i, 6:9] == player):
            return True

        # Check columns
        if np.all(game_board[:3, i] == player) or np.all(game_board[3:6, i] == player) or np.all(game_board[6:9, i] == player):
            return True

    # Check diagonals
    for i in range(8):
        if np.all(game_board[i:i+3, i:i+3] == player) or np.all(game_board[i:i+3, 9-i-2:9-i+1] == player):
            return True

    return False

def display_game_board(game_board):
    # Print the game board
    print("-" * 22)
    for row in range(10):
        print("|", end=" ")
        for col in range(10):
            if game_board[row, col] == 0:
                print(" ", end=" ")
            elif game_board[row, col] == 1:
                print("X", end=" ")
            else:
                print("O", end=" ")
        print("|")
    print("-" * 22)

if __name__ == "__main__":
    play_connect_four()
