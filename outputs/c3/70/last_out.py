import numpy as np
import pygame
import socket

# Create a 10x10 grid
grid = np.zeros((10, 10), dtype=int)

# Define the players' turns
player1_turn = True
player2_turn = False

# Define the winning combinations
winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                       (0, 3, 6), (1, 4, 7), (2, 5, 8),
                       (0, 4, 8), (2, 4, 6)]

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

# Load the game assets
player1_piece = pygame.image.load("player1_piece.png")
player2_piece = pygame.image.load("player2_piece.png")

# Initialize the network
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("localhost", 5000))
sock.listen(1)
conn, addr = sock.accept()

# Initialize the AI
ai = AI()

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the column number of the mouse click
            column = event.pos[0] // 60

            # Check if the move is valid
            if move not in range(0, 10) or grid[0][int(move)] != 0:
                continue

            # Place the player's piece in the grid
            for i in range(9, -1, -1):
                if grid[i][int(column)] == 0:
                    if player1_turn:
                        grid[i][int(column)] = 1
                    else:
                        grid[i][int(column)] = 2
                    break

            # Send the move to the other player
            conn.sendall(str(column).encode())

            # Check if the player has won
            for combination in winning_combinations:
                if grid[combination[0]][combination[1]][combination[2]] == grid[combination[0]][combination[1]][combination[2]] != 0:
                    if player1_turn:
                        print("Player 1 wins!")
                    else:
                        print("Player 2 wins!")
                    break

            # Check if the game is a draw
            if np.all(grid != 0):
                print("Draw!")
                break

            # Switch the player's turns
            player1_turn = not player1_turn
            player2_turn = not player2_turn

    # If it's the AI's turn, make a move
    if player2_turn and not player1_turn:
        move = ai.choose_move(grid)
        for i in range(9, -1, -1):
            if grid[i][int(move)] == 0:
                grid[i][int(move)] = 2
                break

    # Draw the game board
    screen.fill((0, 0, 0))

    for i in range(10):
        for j in range(10):
            if grid[i][j] == 1:
                screen.blit(player1_piece, (j * 60, i * 60))
            elif grid[i][j] == 2:
                screen.blit(player2_piece, (j * 60, i * 60))

    # Update the display
    pygame.display.update()

    # Clock tick
    clock.tick(60)

# Quit Pygame
pygame.quit()
