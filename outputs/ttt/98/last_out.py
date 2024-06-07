import numpy as np
import pygame
import socket

# Create a socket for multiplayer support
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5000))
server_socket.listen()

# Initialize the Pygame library
pygame.init()

# Set the game screen size
screen_width = 600
screen_height = 600

# Create the game screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the game title
pygame.display.set_caption("JDV")

# Define the colors to be used in the game
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define the game grid size
grid_size = 3

# Create the game grid
grid = np.zeros((grid_size, grid_size), dtype=int)

# Set the current player to "X"
player = "X"

# Create a loop that runs until there is a winner or a draw
while True:
    # Check for events
    for event in pygame.event.get():
        # Handle the quit event
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Handle the mouse click event
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Convert the mouse position to grid coordinates
            row = mouse_y // (screen_height // grid_size)
            col = mouse_x // (screen_width // grid_size)

            # Check if the move is valid
            if not is_valid_move(grid, row, col):
                print("Invalid move.")
                continue

            # Place the player's piece in the grid
            grid[row, col] = player

            # Check if the current player has won
            if check_win(grid, player):
                print("Player {} wins!".format(player))
                break

            # Switch to the other player
            player = "O" if player == "X" else "X"

    # Check if there is a draw
    if np.all(grid != 0):
        print("Draw!")
        break

    # Draw the game board
    draw_board(grid)

    # Update the display
    pygame.display.update()

# Function to check if a move is valid
def is_valid_move(grid, row, col):
    return grid[row, col] == 0 and 0 <= row < grid_size and 0 <= col < grid_size

# Function to check if a player has won
def check_win(grid, player):
    # Check the rows for a win
    for row in grid:
        if np.all(row == player):
            return True

    # Check the columns for a win
    for col in grid.T:
        if np.all(col == player):
            return True

    # Check the diagonals for a win
    if np.all(grid.diagonal() == player) or np.all(np.flip(grid).diagonal() == player):
        return True

    # No win yet
    return False

# Function to draw the game board
def draw_board(grid):
    # Clear the screen
    screen.fill(WHITE)

    # Draw the grid lines
    for i in range(grid_size):
        pygame.draw.line(screen, BLACK, (0, i * (screen_height // grid_size)), (screen_width, i * (screen_height // grid_size)), 2)
        pygame.draw.line(screen, BLACK, (i * (screen_width // grid_size), 0), (i * (screen_width // grid_size), screen_height), 2)

    # Draw the player pieces
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i, j] == "X":
                pygame.draw.circle(screen, RED, ((i + 0.5) * (screen_width // grid_size), (j + 0.5) * (screen_height // grid_size)), 50, 2)
            elif grid[i, j] == "O":
                pygame.draw.circle(screen, BLUE, ((i + 0.5) * (screen_width // grid_size), (j + 0.5) * (screen_height // grid_size)), 50, 2)

# Main game loop
if __name__ == "__main__":
    # Get the game mode (single-player or multiplayer)
    game_mode = input("Enter game mode (single-player or multiplayer): ")

    # Create the game grid
    grid = np.zeros((grid_size, grid_size), dtype=int)

    # Set the current player to "X"
    player = "X"

    # Create a loop that runs until there is a winner or a draw
    while True:
        # Check for events
        for event in pygame.event.get():
            # Handle the quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Handle the mouse click event
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get the mouse position
                mouse_x, mouse_y = pygame.mouse.get_pos()

                # Convert the mouse position to grid coordinates
                row = mouse_y // (screen_height // grid_size)
                col = mouse_x // (screen_width // grid_size)

                # Check if the move is valid
                if not is_valid_move(grid, row, col):
                    print("Invalid move.")
                    continue

                # Place the player's piece in the grid
                grid[row, col] = player

                # Check if the current player has won
                if check_win(grid, player):
                    print("Player {} wins!".format(player))
                    break

                # Switch to the other player
                player = "O" if player == "X" else "X"

        # Check if there is a draw
        if np.all(grid != 0):
            print("Draw!")
            break

        # Draw the game board
        draw_board(grid)

        # Update the display
        pygame.display.update()
