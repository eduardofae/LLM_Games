import numpy as np
import pygame
import pickle

# Initialize Pygame
pygame.init()

# Set the game screen size
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Define the game colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define the player's symbols
player1_symbol = 'X'
player2_symbol = 'O'

# Define the game difficulty levels
EASY = 1
MEDIUM = 2
HARD = 3

# Set the game difficulty level
difficulty = EASY

# Create a 3x3 grid
grid = np.zeros((3, 3), dtype=int)

# Create a scoreboard
scoreboard = {
    player1_symbol: 0,
    player2_symbol: 0
}

# Load the sound effects
move_sound = pygame.mixer.Sound('move.wav')
win_sound = pygame.mixer.Sound('win.wav')
draw_sound = pygame.mixer.Sound('draw.wav')

# Keep track of whose turn it is
turn = 1

# Keep track of the number of moves made
moves = 0

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

            # Convert the mouse position to a row and column on the grid
            row = mouse_y // 200
            col = mouse_x // 200

            # Check if the player's move is valid
            if 0 <= row < 3 and 0 <= col < 3 and grid[row, col] == 0:
                # Place the player's piece in the grid
                if turn == 1:
                    grid[row, col] = player1_symbol
                else:
                    grid[row, col] = player2_symbol

                # Play the move sound
                move_sound.play()

                # Check if the player has won
                if check_win(grid, player1_symbol) or check_win(grid, player2_symbol):
                    # Play the win sound
                    win_sound.play()

                    # Update the scoreboard
                    if turn == 1:
                        scoreboard[player1_symbol] += 1
                    else:
                        scoreboard[player2_symbol] += 1

                    # Display the win message
                    print(f"Player {turn} wins!")

                    # Reset the game
                    grid = np.zeros((3, 3), dtype=int)
                    moves = 0
                    turn = 1

                # Check if the game is a draw
                moves += 1
                if moves == 9:
                    # Play the draw sound
                    draw_sound.play()

                    # Display the draw message
                    print("Draw!")

                    # Reset the game
                    grid = np.zeros((3, 3), dtype=int)
                    moves = 0
                    turn = 1

                # Change turns
                turn = 3 - turn
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                # Save the game to a file
                with open('game.dat', 'wb') as f:
                    pickle.dump((grid, scoreboard, turn, moves), f)
            elif event.key == pygame.K_l:
                # Load the game from a file
                with open('game.dat', 'rb') as f:
                    grid, scoreboard, turn, moves = pickle.load(f)

    # Draw the game board
    screen.fill(BLACK)
    for i in range(3):
        for j in range(3):
            if grid[i, j] == player1_symbol:
                pygame.draw.rect(screen, RED, (j * 200, i * 200, 200, 200))
            elif grid[i, j] == player2_symbol:
                pygame.draw.rect(screen, GREEN, (j * 200, i * 200, 200, 200))

    # Draw the scoreboard
    font = pygame.font.SysFont('Arial', 30)
    text_surface1 = font.render(f"Player 1: {scoreboard[player1_symbol]}", True, WHITE)
    text_surface2 = font.render(f"Player 2: {scoreboard[player2_symbol]}", True, WHITE)
    screen.blit(text_surface1, (10, 10))
    screen.blit(text_surface2, (10, 50))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
