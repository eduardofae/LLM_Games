import numpy as np
import pygame
import socket
import threading

# Define constants
GRID_SIZE = 10
WIN_LENGTH = 3
CELL_SIZE = 50

# Create a 10x10 grid
grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)

# Define the players
players = [1, 2]

# Define the game state
PLAYING = 0
WON = 1
DRAW = 2
game_state = PLAYING

# Initialize the Pygame window
pygame.init()
screen = pygame.display.set_mode((GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE))
pygame.display.set_caption("Connect Four")

# Create the game board
board_surface = pygame.Surface((GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE))
board_surface.fill((0, 0, 0))
for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        pygame.draw.rect(board_surface, (255, 255, 255), (i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

# Create the player pieces
player1_piece = pygame.Surface((CELL_SIZE, CELL_SIZE))
player1_piece.fill((255, 0, 0))
player2_piece = pygame.Surface((CELL_SIZE, CELL_SIZE))
player2_piece.fill((0, 0, 255))

# Create the AI opponent
ai_opponent = AI()

# Start the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the current player
            player = players[0]

            # Get the column of the mouse click
            col = event.pos[0] // CELL_SIZE

            # Check if the column is valid and has an empty space at the top
            if col in range(GRID_SIZE) and grid[0][col] == 0:
                # Place the player's piece in the grid
                for i in range(GRID_SIZE-1, -1, -1):
                    if grid[i][col] == 0:
                        grid[i][col] = player
                        break

                # Check if the player has won
                if check_win(grid, player):
                    game_state = WON
                    break

                # Check if the game is a draw
                if np.all(grid != 0):
                    game_state = DRAW
                    break

                # Switch to the other player
                players.reverse()

        # Handle AI opponent's turn
        if player == 2 and game_state == PLAYING:
            col = ai_opponent.get_move(grid)
            for i in range(GRID_SIZE-1, -1, -1):
                if grid[i][col] == 0:
                    grid[i][col] = player
                    break
            if check_win(grid, player):
                game_state = WON
                break
            if np.all(grid != 0):
                game_state = DRAW
                break
            players.reverse()

    # Draw the game board
    screen.fill((0, 0, 0))
    screen.blit(board_surface, (0, 0))

    # Draw the player pieces
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if grid[i][j] == 1:
                screen.blit(player1_piece, (j * CELL_SIZE, i * CELL_SIZE))
            elif grid[i][j] == 2:
                screen.blit(player2_piece, (j * CELL_SIZE, i * CELL_SIZE))

    # Update the display
    pygame.display.update()

    # Check if the game is over
    if game_state == WON:
        print(f"Player {player} wins!")
        running = False
    elif game_state == DRAW:
        print("It's a draw!")
        running = False

# Quit the game
pygame.quit()

# Define the function to check if a player has won
def check_win(grid, player):
    # Check for a horizontal win
    for i in range(GRID_SIZE):
        if np.all(grid[i, :] == player):
            return True

    # Check for a vertical win
    for j in range(GRID_SIZE):
        if np.all(grid[:, j] == player):
            return True

    # Check for a diagonal win
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if i + WIN_LENGTH - 1 < GRID_SIZE and j + WIN_LENGTH - 1 < GRID_SIZE and np.all(grid[i:i+WIN_LENGTH, j:j+WIN_LENGTH] == player):
                return True
            if i + WIN_LENGTH - 1 < GRID_SIZE and j - WIN_LENGTH + 1 >= 0 and np.all