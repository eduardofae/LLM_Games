import numpy as np
import random

# Define the game board
board = np.zeros((3, 3))

# Define the players
players = ["X", "O"]

# Keep track of the current player
current_player = 0

# Main game loop
while True:
    # Get the player's move
    while True:
        try:
            move = input(f"Player {players[current_player]}, please enter your move (row, column) or 'quit' to exit: ")
            if move == 'quit':
                print("Exiting the game.")
                exit()
            row, column = map(int, move.split(","))

            # Check if the move is valid
            if not (0 <= row < 3 and 0 <= column < 3):
                raise ValueError("Invalid move: row or column index is out of range")
            if board[row, column] != 0:
                raise ValueError("Invalid move: cell is not empty")

            break
        except ValueError as e:
            print(e)

    # Place the player's piece on the board
    board[row, column] = players[current_player]

    # Check if the player has won
    if np.any(np.all(board == players[current_player], axis=0)) or \
       np.any(np.all(board == players[current_player], axis=1)) or \
       np.all(board.diagonal() == players[current_player]) or \
       np.all(np.flip(board).diagonal() == players[current_player]):
        print(f"Player {players[current_player]} wins!")
        break

    # Check if the game is a draw
    if np.all(board != 0):
        print("Draw!")
        break

    # Switch to the other player
    current_player = (current_player + 1) % 2

# Print the final game board
print(board)

# Add a way to play against a computer AI
def computer_move():
    # Get all possible moves
    possible_moves = [(row, column) for row in range(3) for column in range(3) if board[row, column] == 0]

    # Choose a random move
    move = random.choice(possible_moves)

    # Place the computer's piece on the board
    board[move[0], move[1]] = players[current_player]

# Add a way to play against a human opponent
def human_move():
    # Get the player's move
    while True:
        try:
            move = input(f"Player {players[current_player]}, please enter your move (row, column) or 'quit' to exit: ")
            if move == 'quit':
                print("Exiting the game.")
                exit()
            row, column = map(int, move.split(","))

            # Check if the move is valid
            if not (0 <= row < 3 and 0 <= column < 3):
                raise ValueError("Invalid move: row or column index is out of range")
            if board[row, column] != 0:
                raise ValueError("Invalid move: cell is not empty")

            break
        except ValueError as e:
            print(e)

    # Place the player's piece on the board
    board[row, column] = players[current_player]

# Play against the computer or a human opponent
while True:
    # Get the player's move
    if current_player == 0:
        computer_move()
    else:
        human_move()

    # Check if the player has won
    if np.any(np.all(board == players[current_player], axis=0)) or \
       np.any(np.all(board == players[current_player], axis=1)) or \
       np.all(board.diagonal() == players[current_player]) or \
       np.all(np.flip(board).diagonal() == players[current_player]):
        print(f"Player {players[current_player]} wins!")
        break

    # Check if the game is a draw
    if np.all(board != 0):
        print("Draw!")
        break

    # Switch to the other player
    current_player = (current_player + 1) % 2
