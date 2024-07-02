import numpy as np
import pygame
from pygame.locals import *

# Define the game board
board = np.zeros((10, 10), dtype=int)

# Define the players
players = [1, -1]

# Define the game state
game_over = False
draw = False
current_player = players[0]

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Define the screen size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Create the game board surface
board_surface = pygame.Surface((400, 400))
board_surface.fill(WHITE)
for i in range(10):
    pygame.draw.line(board_surface, BLACK, (i * 40, 0), (i * 40, 400), 1)
    pygame.draw.line(board_surface, BLACK, (0, i * 40), (400, i * 40), 1)

# Create the player pieces
player_pieces = [pygame.Surface((40, 40)) for _ in range(2)]
player_pieces[0].fill(RED)
player_pieces[1].fill(YELLOW)

# Create the AI opponent
ai_opponent = AIopponent()

# Main game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            game_over = True
        elif event.type == MOUSEBUTTONDOWN:
            # Get the column of the mouse click
            column = event.pos[0] // 40

            # Check if the column is valid and has an empty space
            if 0 <= column < 10 and board[9][column] == 0:
                # Drop the player's piece
                for i in range(9, -1, -1):
                    if board[i][column] == 0:
                        board[i][column] = current_player
                        break

                # Check if the player has won
                if check_win(board, current_player):
                    game_over = True
                    print("Player {} wins!".format(current_player))
                else:
                    # Switch to the other player
                    current_player = players[1 - players.index(current_player)]

                    # Get the AI opponent's move
                    ai_move = ai_opponent.get_move(board)

                    # Drop the AI opponent's piece
                    for i in range(9, -1, -1):
                        if board[i][ai_move] == 0:
                            board[i][ai_move] = current_player
                            break

                    # Check if the AI opponent has won
                    if check_win(board, current_player):
                        game_over = True
                        print("AI opponent wins!")

                # Check if the game is a draw
                if np.all(board != 0):
                    game_over = True
                    draw = True
                    print("Draw!")

    # Draw the game board
    screen.fill(BLACK)
    screen.blit(board_surface, (100, 100))

    # Draw the player pieces
    for i in range(10):
        for j in range(10):
            if board[i][j] != 0:
                screen.blit(player_pieces[board[i][j] - 1], (100 + j * 40, 100 + i * 40))

    # Update the display
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)

# Game over
if draw:
    print("Draw!")
else:
    print("Player {} wins!".format(current_player))

# Quit Pygame
pygame.quit()
