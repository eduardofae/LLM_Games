import random
import pygame

# Define the game board size.
BOARD_SIZE = 3

# Define the colors used in the game.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define the game pieces.
PIECES = {
    'X': pygame.image.load('x.png'),
    'O': pygame.image.load('o.png')
}

# Create the game board.
board = [[' ' for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

# Create a list of the available spaces.
available_spaces = [(row, column) for row in range(BOARD_SIZE) for column in range(BOARD_SIZE)]

# Create a dictionary of the players' pieces.
players = {
    'A': 'X',
    'B': 'O'
}

# Get the players' names.
player_a_name = input("Player A's name: ")
player_b_name = input("Player B's name: ")

# Decide who goes first.
current_player = random.choice(['A', 'B'])

# Create a dictionary to keep track of the players' scores.
scores = {
    'A': 0,
    'B': 0
}

# Start the game.
game_over = False

while not game_over:

    # Get the current player's move.
    move = input(f"{current_player}'s move: ")

    # Check if the move is valid.
    if move not in available_spaces:
        print("Invalid move.")
        continue

    # Place the current player's piece on the board.
    row, column = move
    board[row][column] = players[current_player]

    # Check if the current player has won.
    if check_for_win(board, current_player):
        game_over = True
        print(f"{current_player} wins!")
        scores[current_player] += 1

    # Check if there are no more available spaces.
    if len(available_spaces) == 0:
        game_over = True
        print("Draw!")

    # Switch to the other player.
    current_player = 'A' if current_player == 'B' else 'B'

# Print the final board.
for row in board:
    print(' '.join(row))

# Print the final scores.
print("Scores:")
for player, score in scores.items():
    print(f"{player}: {score}")


def check_for_win(board, player):
    """
    Checks if the given player has won the game.

    Args:
        board: The game board.
        player: The player to check for a win.

    Returns:
        True if the player has won, False otherwise.
    """

    # Check for a win in each row.
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check for a win in each column.
    for column in range(BOARD_SIZE):
        if all(board[row][column] == player for row in range(BOARD_SIZE)):
            return True

    # Check for a win in each diagonal.
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True

    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    # No win found.
    return False


if __name__ == "__main__":
    while True:
        jdv()
        play_again = input("Play again? (y/n): ")
        if play_again.lower() != 'y':
            break
