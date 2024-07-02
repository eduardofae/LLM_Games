import pygame
import numpy as np
import pickle

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Define the dimensions of the grid
WIDTH = 7
HEIGHT = 6

# Create the game board
grid = np.zeros((HEIGHT, WIDTH), dtype=int)

# Define the players
players = [1, 2]

# Initialize Pygame
pygame.init()

# Set the screen size
screen = pygame.display.set_mode((WIDTH * 100, HEIGHT * 100))

# Set the background color
screen.fill(WHITE)

# Draw the grid
for i in range(WIDTH):
    for j in range(HEIGHT):
        pygame.draw.rect(screen, BLACK, (i * 100, j * 100, 100, 100), 1)

# Load the sound effects
drop_sound = pygame.mixer.Sound("drop.wav")
win_sound = pygame.mixer.Sound("win.wav")
draw_sound = pygame.mixer.Sound("draw.wav")

# Create the AI opponent
ai = AI()

# Game loop
while True:
    # Get the current player
    player = players[0]

    # Get the player's move
    if player == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                column = pos[0] // 100
                if column < WIDTH and grid[0, column] == 0:
                    for i in range(HEIGHT - 1, -1, -1):
                        if grid[i, column] == 0:
                            grid[i, column] = player
                            drop_sound.play()
                            break
    else:
        # Get the AI's move
        move = ai.get_move(grid, player)
        grid[move, column] = player

    # Check if the player has won
    if check_win(grid, player):
        win_sound.play()
        print(f"Player {player} wins!")
        break

    # Check if the game is a draw
    if np.all(grid != 0):
        draw_sound.play()
        print("Draw!")
        break

    # Switch players
    players = players[1:] + players[:1]

    # Update the screen
    screen.fill(WHITE)
    for i in range(WIDTH):
        for j in range(HEIGHT):
            if grid[j, i] == 1:
                pygame.draw.circle(screen, RED, (i * 100 + 50, j * 100 + 50), 40)
            elif grid[j, i] == 2:
                pygame.draw.circle(screen, YELLOW, (i * 100 + 50, j * 100 + 50), 40)

    pygame.display.update()

# Function to check if a player has won
def check_win(grid, player):
    # Check for horizontal wins
    for i in range(HEIGHT):
        if np.all(grid[i,