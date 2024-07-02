import numpy as np
import pygame
import socketIO_client

# Create a 3x3 grid
grid = np.zeros((3, 3), dtype=int)

# Define the players
players = [1, 2]

# Define the current player
current_player = players[0]

# Define the winning combinations
winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

# Create the game window
pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("jdv")

# Define the game colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Define the game font
font = pygame.font.SysFont("Arial", 32)

# Create the SocketIO client
socketIO = socketIO_client.SocketIO('localhost', 3000)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position
            pos = pygame.mouse.get_pos()

            # Calculate the grid coordinates
            x = pos[0] // 133
            y = pos[1] // 133

            # Check if the move is valid
            if grid[x, y] == 0:
                # Place the player's piece on the grid
                grid[x, y] = current_player

                # Send the move to the server
                socketIO.emit('move', {'x': x, 'y': y})

                # Check if the player has won
                for combination in winning_combinations:
                    if grid[combination[0] // 3, combination[0] % 3] == grid[combination[1] // 3, combination[1] % 3] == grid[combination[2] // 3, combination[2] % 3] != 0:
                        print(f"Player {current_player} wins!")
                        running = False
                        break

                # Check if there are no more free spaces
                if np.all(grid != 0):
                    print("Draw!")
                    running = False
                    break

                # Switch the current player
                current_player = players[(players.index(current_player) + 1) % len(players)]

    # Draw the game board
    screen.fill(BLACK)
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(screen, WHITE, (i * 133, j * 133, 133, 133), 1)

    # Draw the player's pieces
    for i in range(3):
        for j in range(3):
            if grid[i, j] == 1:
                pygame.draw.circle(screen, RED, (i * 133 + 67, j * 133 + 67), 50)
            elif grid[i, j] == 2:
                pygame.draw.circle(screen, BLUE, (i * 133 + 67, j * 133 + 67), 50)

    # Update the display
    pygame.display.update()

# Quit the game
pygame.quit()
