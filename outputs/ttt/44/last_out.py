import numpy as np
import pygame

# Create a 3x3 grid
grid = np.zeros((3, 3))

# Define the players
players = ['X', 'O']

# Start the game
current_player = 0

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

# Game loop
running = True
while running:
  # Handle events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
      # Get the mouse position
      pos = pygame.mouse.get_pos()

      # Convert the mouse position to a row and column index
      row = pos[1] // 100
      col = pos[0] // 100

      # Check if the move is valid
      if grid[row, col] == 0:
        # Place the player's piece on the grid
        grid[row, col] = players[current_player]

        # Check if the player has won
        for i in range(3):
          if (grid[i, 0] == grid[i, 1] == grid[i, 2] != 0 or
              grid[0, i] == grid[1, i] == grid[2, i] != 0 or
              grid[0, 0] == grid[1, 1] == grid[2, 2] != 0 or
              grid[0, 2] == grid[1, 1] == grid[2, 0] != 0):
            print("Player {} wins!".format(players[current_player]))
            running = False
            break

        # Check if the game is a draw
        if np.all(grid != 0):
          print("Draw!")
          running = False
          break

        # Switch to the other player
        current_player = (current_player + 1) % 2

  # Draw the game board
  screen.fill((0, 0, 0))
  for i in range(3):
    for j in range(3):
      if grid[i, j] == 'X':
        pygame.draw.line(screen, (255, 255, 255), (j * 100, i * 100), (j * 100 + 100, i * 100 + 100), 10)
        pygame.draw.line(screen, (255, 255, 255), (j * 100, i * 100 + 100), (j * 100 + 100, i * 100), 10)
      elif grid[i, j] == 'O':
        pygame.draw.circle(screen, (255, 255, 255), (j * 100 + 50, i * 100 + 50), 50, 10)

  # Update the display
  pygame.display.update()

  # Tick the clock
  clock.tick(60)

# Quit Pygame
pygame.quit()
