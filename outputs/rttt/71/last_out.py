import numpy as np
import pygame

# Define the game board size.
BOARD_SIZE = 3

# Define the colors used in the game.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Create the game board.
board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)

# Set the current player.
currentPlayer = 1

# Create the pygame window.
screen = pygame.display.set_mode((400, 400))

# Set the pygame window title.
pygame.display.set_caption("jdv")

# Create the pygame clock.
clock = pygame.time.Clock()

# Create the computer opponent.
computer = ComputerOpponent()

# Run the game loop.
running = True
while running:
    # Handle events.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position.
            pos = pygame.mouse.get_pos()

            # Convert the mouse position to a row and column on the game board.
            row = pos[1] // 100
            col = pos[0] // 100

            # Check if the move is valid.
            if not isValidMove(row, col):
                continue

            # Place the player's piece on the board.
            board[row, col] = currentPlayer

            # Check if the player has won.
            if checkWin(board, currentPlayer):
                running = False

            # Switch the current player.
            currentPlayer = 3 - currentPlayer

            # Check if the computer has won.
            if checkWin(board, computer.player):
                running = False

            # Get the computer's move.
            move = computer.getMove(board)

            # Place the computer's piece on the board.
            board[move[0], move[1]] = computer.player

            # Check if the computer has won.
            if checkWin(board, computer.player):
                running = False

            # Switch the current player.
            currentPlayer = 3 - currentPlayer

    # Draw the game board.
    screen.fill(WHITE)
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            if board[row, col] == 1:
                pygame.draw.circle(screen, RED, (col * 100 + 50, row * 100 + 50), 40)
            elif board[row, col] == 2:
                pygame.draw.circle(screen, BLUE, (col * 100 + 50, row * 100 + 50), 40)

    # Update the pygame display.
    pygame.display.update()

    # Tick the pygame clock.
    clock.tick(60)

# Print the winner.
if winner is None:
    print("Draw")
else:
    print("Player {} wins".format(winner))
