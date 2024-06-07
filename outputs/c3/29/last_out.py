import numpy as np
import pygame

# Define the game board
board = np.zeros((10, 10))

# Define the players
players = [1, 2]

# Define the game state
game_over = False
winner = None

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Initialize the Pygame window
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Main game loop
while not game_over:
    # Get the current player
    player = players[0]

    # Get the player's move
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Convert the mouse position to a column index
            column = int(mouse_x / 80)

            # Check if the column is full
            if board[:, column].any():
                print("Column is full.")
                continue

            # Place the player's piece on the board
            board[board[:, column] == 0, column] = player

    # Check if the player has won
    if check_win(board, player):
        winner = player
        game_over = True
        break

    # Check if the game is a draw
    if board.all():
        game_over = True
        break

    # Switch to the other player
    players = players[1:]

    # Draw the game board
    screen.fill(BLACK)
    for row in range(10):
        for col in range(10):
            if board[row, col] == 1:
                pygame.draw.circle(screen, RED, (col * 80 + 40, row * 60 + 30), 30)
            elif board[row, col] == 2:
                pygame.draw.circle(screen, BLUE, (col * 80 + 40, row * 60 + 30), 30)

    # Flip the display
    pygame.display.flip()

    # Tick the clock
    clock.tick(60)

# Print the winner
if winner:
    print("Player {} wins!".format(winner))
else:
    print("Draw.")

# Quit the Pygame window
pygame.quit()


def check_win(board, player):
    """
    Checks if the player has won the game.

    Args:
    board: The game board.
    player: The player to check.

    Returns:
    True if the player has won, False otherwise.
    """

    # Check for a horizontal win
    for row in range(10):
        if np.all(board[row, :] == player):
            return True

    # Check for a vertical win
    for col in range(10):
        if np.all(board[:, col] == player):
            return True

    # Check for a diagonal win
    for i in range(10):
        # Check the main diagonal
        if np.all(board[i, :10-i] == player):
            return True

        # Check the secondary diagonal
        if np.all(board[i, i:] == player):
            return True

    return False
