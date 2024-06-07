import numpy as np
import pygame

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Define the players
players = ['X', 'O']

# Set the current player to 'X'
current_player = 0

# Play the game until there is a winner or a draw
while True:
    # Get the column where the player wants to place their piece
    column = int(input(f"Player {players[current_player]}, enter a column (0-9): "))

    # Check if the column is valid
    if column < 0 or column > 9:
        print("Invalid column. Please enter a column between 0 and 9.")
        continue

    # Check if the column is full
    if grid[:, column].max() != 0:
        print("Column is full. Please choose another column.")
        continue

    # Place the player's piece in the lowest free space of the column
    row = np.where(grid[:, column] == 0)[0][-1]
    grid[row, column] = players[current_player]

    # Check if the player has won
    if check_for_win(grid, players[current_player]):
        print(f"Player {players[current_player]} wins!")
        break

    # Check if the game is a draw
    if grid.max() != 0:
        print("Draw!")
        break

    # Switch to the other player
    current_player = (current_player + 1) % 2

# Define a function to check if a player has won
def check_for_win(grid, player):
    # Check for horizontal wins
    for row in range(10):
        if np.all(grid[row, :] == player):
            return True

    # Check for vertical wins
    for column in range(10):
        if np.all(grid[:, column] == player):
            return True

    # Check for diagonal wins
    for i in range(10):
        if np.all(grid[i, :i] == player) or np.all(grid[i, (9-i):] == player):
            return True

    return False


# Add a graphical interface using Pygame
import pygame

# Initialize Pygame
pygame.init()

# Set the screen size
screen = pygame.display.set_mode((400, 400))

# Set the background color
screen.fill((0, 0, 0))

# Draw the grid
for i in range(10):
    pygame.draw.line(screen, (255, 255, 255), (i * 40, 0), (i * 40, 400), 1)
    pygame.draw.line(screen, (255, 255, 255), (0, i * 40), (400, i * 40), 1)

# Draw the pieces
for row in range(10):
    for column in range(10):
        if grid[row, column] == 'X':
            pygame.draw.circle(screen, (255, 0, 0), (column * 40 + 20, row * 40 + 20), 15)
        elif grid[row, column] == 'O':
            pygame.draw.circle(screen, (0, 255, 0), (column * 40 + 20, row * 40 + 20), 15)

# Update the display
pygame.display.update()

# Wait for the user to quit the game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
