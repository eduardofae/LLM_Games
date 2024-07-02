import numpy as np
import pygame

# Initialize Pygame
pygame.init()

# Set game constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
CELL_SIZE = 200
BOARD_SIZE = 3

# Create the game screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("JDV")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Create the game board
board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)

# Initialize the current player
current_player = 1

# Create the AI opponent
ai_opponent = MinimaxAI(board, current_player)

# Initialize game state variables
game_over = False
winner = None

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the player's move
            mouse_x, mouse_y = pygame.mouse.get_pos()
            row = mouse_y // CELL_SIZE
            column = mouse_x // CELL_SIZE

            # Check if the move is valid
            if not (0 <= row < BOARD_SIZE and 0 <= column < BOARD_SIZE):
                print("Invalid move. Please enter a valid row and column.")
                continue
            if board[row, column] != 0:
                print("Invalid move. Please choose an empty space.")
                continue

            # Place the player's piece on the grid
            board[row, column] = current_player

            # Check if the player has won
            if check_win(board, current_player):
                winner = current_player
                game_over = True
                break

            # Check if the game is a draw
            if np.all(board != 0):
                game_over = True
                break

            # Switch to the AI opponent's turn
            current_player = 3 - current_player
            ai_move = ai_opponent.get_move()
            board[ai_move[0], ai_move[1]] = current_player

            # Check if the AI opponent has won
            if check_win(board, current_player):
                winner = current_player
                game_over = True
                break

            # Check if the game is a draw
            if np.all(board != 0):
                game_over = True
                break

    # Draw the game board
    draw_board(screen, board)

    # Update the display
    pygame.display.update()

    # Check if the game is over
    if game_over:
        if winner is not None:
            print(f"Player {winner} wins!")
        else:
            print("Draw!")

        # Ask the players if they want to replay the game
        while True:
            replay = input("Do you want to replay the game? (y/n) ")
            if replay in ["y", "Y"]:
                # Reset the game
                board = np.zeros((BOARD_SIZE, BOARD_SIZE), dtype=int)
                current_player = 1
                game_over = False
                winner = None
                break
            elif replay in ["n", "N"]:
                running = False
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

# Quit Pygame
pygame.quit()
