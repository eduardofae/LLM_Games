import numpy as np
import pygame

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

# Define the dimensions of the game board
BOARD_WIDTH = 10
BOARD_HEIGHT = 10

# Define the size of each cell in the game board
CELL_SIZE = 50

# Define the winning conditions
winning_conditions = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)],
]

# Define the players' turns
player1 = 1
player2 = -1

# Create the game board
board = np.zeros((BOARD_WIDTH, BOARD_HEIGHT), dtype=int)

# Initialize the PyGame library
pygame.init()

# Set the screen size
screen = pygame.display.set_mode((BOARD_WIDTH * CELL_SIZE, BOARD_HEIGHT * CELL_SIZE))

# Set the window title
pygame.display.set_caption("Pong")

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Add sound effects to the game
click_sound = pygame.mixer.Sound("click.wav")
win_sound = pygame.mixer.Sound("win.wav")
draw_sound = pygame.mixer.Sound("draw.wav")

# Add a timer to the game
timer = pygame.time.Clock()

# Add a menu to the game
menu_font = pygame.font.SysFont("Arial", 24)
menu_options = ["Play against a friend", "Play against the computer"]
menu_selected_option = 0
menu_running = True

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse click is in the menu
            if menu_running:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if mouse_x >= 10 and mouse_x <= 290 and mouse_y >= 10 and mouse_y <= 50:
                    menu_selected_option = 0
                elif mouse_x >= 10 and mouse_x <= 370 and mouse_y >= 60 and mouse_y <= 100:
                    menu_selected_option = 1

            # Check if the mouse click is on the game board
            else:
                # Get the position of the mouse click
                pos = pygame.mouse.get_pos()

                # Convert the mouse click to a cell on the game board
                cell_x = pos[0] // CELL_SIZE
                cell_y = pos[1] // CELL_SIZE

                # Check if the cell is empty
                if board[cell_x, cell_y] == 0:
                    # Play the click sound
                    click_sound.play()

                    # Place the player's piece on the cell
                    board[cell_x, cell_y] = player1

                    # Check if the player has won
                    for condition in winning_conditions:
                        if all(board[x, y] == player1 for x, y in condition):
                            # Play the win sound
                            win_sound.play()

                            print("Player 1 wins!")
                            running = False
                            break
                    else:
                        # Check if the game is a draw
                        if np.all(board != 0):
                            # Play the draw sound
                            draw_sound.play()

                            print("Draw!")
                            running = False
                            break

                        # Switch the player's turns
                        player1 = -player1

    # Update the timer
    time_remaining = timer.tick(1000) / 1000

    # Draw the game board
    screen.fill(BLACK)
    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            # Draw the cell
            pygame.draw.rect(screen, WHITE, (x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE))

            # Draw the player's piece
            if board[x, y] == player1:
                pygame.draw.circle(screen, BLUE, (x * CELL_SIZE + CELL_SIZE //