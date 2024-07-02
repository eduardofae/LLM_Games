import numpy as np

def jdv():
    """
    Plays a game of JDV.
    """

    # Create a 3x3 game board.
    board = np.zeros((3, 3), dtype=int)

    # Get the starting player.
    starting_player = get_starting_player()

    # Set the current player to the starting player.
    current_player = starting_player

    # Play the game until a winner is determined or the game is a draw.
    while True:
        try:
            # Get the next player's move.
            move = get_move(board)

            # Place the player's piece on the board.
            board[move[0], move[1]] = current_player

            # Print the game board.
            print_board(board)

            # Check if the game is over.
            winner = check_winner(board)
            if winner is not None:
                break

            # Switch to the other player's turn.
            current_player = -current_player

        except ValueError:
            print("Invalid move. Please try again.")

    # Print the winner.
    if winner is not None:
        print("Player {} wins!".format(winner))
    else:
        print("The game is a draw.")

    # Ask the players if they want to play again.
    play_again = input("Do you want to play again? (y/n) ")
    if play_again == "y":
        # Reset the game board and start a new game.
        board = np.zeros((3, 3), dtype=int)
        jdv()
    else:
        # Exit the game.
        print("Thanks for playing!")


def get_starting_player():
    """
    Gets the starting player.

    Returns:
        The starting player, either 1 or -1.
        The game randomly choose which player is 1 and which is -1
    """

    # Get the player's input.
    player1 = input("Player 1, enter your name: ")
    player2 = input("Player 2, enter your name: ")
    players = [player1, player2]
    import random
    random.shuffle(players)
    
    print(f"{players[0]} goes first!")
    if players[0]==player1:
      return 1
    else:
      return -1

def get_move(board):
    """
    Gets the next player's move.

    Args:
        board: A 3x3 numpy array representing the game board.

    Returns:
        A tuple representing the player's move.
    """

    # Get the player's input.
    move = input("Enter your move (row, col): ")

    # Convert the input to a tuple of integers.
    row, col = map(int, move.split(","))

    # Check if the move is valid.
    if board[row, col] != 0:
        raise ValueError("Invalid move. Please try again.")

    # Return the player's move.
    return (row, col)


def print_board(board):
    """
    Prints the given game board.

    Args:
        board: A 3x3 numpy array representing the game board.
    """

    for row in board:
        for col in row:
            if col == 0:
                print(" ", end=" ")
            elif col == 1:
                print("X", end=" ")
            else:
                print("O", end=" ")
        print()


# Play the game.
jdv()
