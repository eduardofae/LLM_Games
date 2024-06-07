import pygame
import numpy as np

# Initialize pygame
pygame.init()

# Set the game screen size
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Create the game board
board = np.zeros((10, 10))

# Create a list of the players
players = [1, 2]

# Set the current player to player 1
current_player = 0

# Set the game state to "ongoing"
game_state = "ongoing"

# Create a font object
font = pygame.font.SysFont("Arial", 32)

# Main game loop
while game_state == "ongoing":
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # Convert the mouse position to a column number
            column = mouse_x // 60

            # Check if the column is valid
            if column < 0 or column > 9:
                continue

            # Check if the column is full
            if board[0][column] != 0:
                continue

            # Place the player's piece in the column
            for i in range(9, -1, -1):
                if board[i][column] == 0:
                    board[i][column] = players[current_player]
                    break

            # Check if the player has won
            if check_for_win(board, players[current_player]):
                print("Player {} wins!".format(players[current_player]))
                game_state = "finished"
            else:
                # Check if there are any more free spaces
                if np.all(board != 0):
                    print("Draw!")
                    game_state = "finished"
                else:
                    # Switch to the other player
                    current_player = (current_player + 1) % len(players)

    # Draw the game board
    screen.fill((0, 0, 0))
    for i in range(10):
        for j in range(10):
            if board[i][j] == 0:
                pygame.draw.rect(screen, (255, 255, 255), (j * 60, i * 60, 60, 60))
            elif board[i][j] == 1:
                pygame.draw.rect(screen, (255, 0, 0), (j * 60, i * 60, 60, 60))
            elif board[i][j] == 2:
                pygame.draw.rect(screen, (0, 0, 255), (j * 60, i * 60, 60, 60))

    # Update the display
    pygame.display.update()


def check_for_win(board, player):
    # Check for a horizontal win
    for i in range(10):
        if np.all(board[i] == player):
            return True

    # Check for a vertical win
    for i in range(10):
        if np.all(board[:, i] == player):
            return True

    # Check for a diagonal win
    for i in range