import numpy as np

def jdv():
    # Create the game board
    game_board = np.zeros((3, 3))

    # Set up the players
    player1 = 'X'
    player2 = 'O'

    # Set up the game loop
    while True:
        # Get the player's move
        try:
            move = input(f"{player1}'s turn: ")
            row, col = map(int, move.split())
        except ValueError:
            print("Invalid move. Please enter a valid move in the format 'row, col'.")
            continue

        # Check if the move is valid
        if game_board[row, col] != 0:
            print("Invalid move. That space is already taken.")
            continue

        # Place the player's piece on the board
        game_board[row, col] = player1

        # Check if the player has won
        if check_win(game_board, player1):
            print(f"{player1} wins!")
            break

        # Check if there are no more free spaces
        if np.all(game_board != 0):
            print("Draw!")
            break

        # Switch players
        player1, player2 = player2, player1

    # Print the final board
    print(game_board)

    # Ask the player if they want to reset the game
    reset = input("Would you like to reset the game? (y/n) ")
    if reset == "y":
        jdv()

def check_win(game_board, player):
    # Check the rows, columns, and diagonals
    for row in range(3):
        if np.all(game_board[row, :] == player):
            return True
    for col in range(3):
        if np.all(game_board[:, col] == player):
            return True
    if np.all(game_board.diagonal() == player):
        return True
    if np.all(np.flip(game_board).diagonal() == player):
        return True

    # No win yet
    return False

if __name__ == "__main__":
    jdv()
