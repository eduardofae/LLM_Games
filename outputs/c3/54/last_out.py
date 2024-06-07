import numpy as np
import pygame
import pickle

# Define the game board size
BOARD_WIDTH = 10
BOARD_HEIGHT = 10

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Define the players' turns
player1_turn = True

# Define the winning states
winning_states = [
    [[1, 1, 1], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [1, 1, 1], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [1, 1, 1]],
    [[1, 0, 0], [1, 0, 0], [1, 0, 0]],
    [[0, 1, 0], [0, 1, 0], [0, 1, 0]],
    [[0, 0, 1], [0, 0, 1], [0, 0, 1]],
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]],
    [[0, 0, 1], [0, 1, 0], [1, 0, 0]],
]

# Initialize the PyGame window
pygame.init()
screen = pygame.display.set_mode((BOARD_WIDTH * 50, BOARD_HEIGHT * 50))
clock = pygame.time.Clock()

# Create the game board
board = np.zeros((BOARD_HEIGHT, BOARD_WIDTH))

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Convert the mouse position to a column index
            column = mouse_x // 50

            # Check if the move is valid
            if column < 0 or column > BOARD_WIDTH - 1 or board[9, column] != 0:
                continue

            # Drop the piece
            row = 9
            while row >= 0 and board[row, column] == 0:
                row -= 1

            board[row + 1, column] = 1 if player1_turn else 2

            # Check if the game is over
            for winning_state in winning_states:
                if np.array_equal(board, winning_state):
                    print("Player" + ("1" if player1_turn else "2") + " wins!")
                    running = False
                    break

            if np.all(board != 0):
                print("Draw!")
                running = False
                break

            # Switch the player's turn
            player1_turn = not player1_turn

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_u:
                # Undo the last move
                if player1_turn:
                    board[board == 1] = 0
                else:
                    board[board == 2] = 0
                player1_turn = not player1_turn
            elif event.key == pygame.K_r:
                # Restart the game
                board = np.zeros((BOARD_HEIGHT, BOARD_WIDTH))
                player1_turn = True

    # Draw the game board
    screen.fill(BLACK)
    for row in range(BOARD_HEIGHT):
        for column in range(BOARD_WIDTH):
            if board[row, column] == 1:
                pygame.draw.circle(screen, RED, (column * 50 + 25, row * 50 + 25), 25)
            elif board[row, column] == 2:
                pygame.draw.circle(screen, BLUE, (column * 50 + 25, row * 50 + 25), 25)

    # Update the display
    pygame.display.update()

    # Tick the clock
    clock.tick(60)

# Quit the game
pygame.quit()
