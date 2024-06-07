import pygame

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
RED =   (255,   0,   0)

# Define the dimensions of the game board
BOARD_WIDTH = 700
BOARD_HEIGHT = 700

# Define the number of rows and columns in the game board
NUM_ROWS = 10
NUM_COLS = 10

# Define the size of each cell in the game board
CELL_SIZE = BOARD_WIDTH // NUM_COLS

# Define the players' symbols
PLAYER1_SYMBOL = 'X'
PLAYER2_SYMBOL = 'O'

# Define the current player
current_player = PLAYER1_SYMBOL

# Define the game state
game_state = 'IN_PROGRESS'

# Create the game board
board = [[' ' for _ in range(NUM_COLS)] for _ in range(NUM_ROWS)]

# Initialize Pygame
pygame.init()

# Create the game window
screen = pygame.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))

# Set the window title
pygame.display.set_caption("Connect Four")

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Run the game loop
while game_state == 'IN_PROGRESS':
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_state = 'QUIT'
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the column that the player clicked on
            column = event.pos[0] // CELL_SIZE

            # Check if the column is valid
            if column < 0 or column > NUM_COLS:
                continue

            # Check if the column is full
            if all(space != ' ' for space in board[column]):
                continue

            # Find the lowest free space in the column
            row = NUM_ROWS - 1
            while row >= 0 and board[row][column] != ' ':
                row -= 1

            # Place the player's piece in the grid
            board[row][column] = current_player

            # Check if the player has won
            if check_for_win(board, current_player):
                game_state = f"{current_player} WINS!"

            # Check if the game is a draw
            if all(space != ' ' for space in [space for row in board for space in row]):
                game_state = "DRAW!"

            # Switch to the other player
            if current_player == PLAYER1_SYMBOL:
                current_player = PLAYER2_SYMBOL
            else:
                current_player = PLAYER1_SYMBOL

    # Draw the game board
    screen.fill(BLACK)

    for row in range(NUM_ROWS):
        for column in range(NUM_COLS):
            # Draw the cell
            pygame.draw.rect(screen, WHITE, (column * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

            # Draw the player's piece, if any
            if board[row][column] != ' ':
                if board[row][column] == PLAYER1_SYMBOL:
                    color = BLUE
                else:
                    color = RED
                pygame.draw.circle(screen, color, (column * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2), CELL_SIZE // 2 - 2)

    # Draw the game state
    font = pygame.font.SysFont('Arial', 32)
    text = font.render(game_state, True, WHITE)
    text_rect = text.get_rect()
    text_rect.center = (BOARD_WIDTH // 2, BOARD_HEIGHT // 2)
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.update()

    # Limit the frame rate to 60 FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()

# Define the function to check for a win
def check_for_win(board, player_symbol):
    # Check for a horizontal win
    for row in board:
        if all(space == player_symbol for space in row):
            return True

    # Check for a vertical win
    for column in range(NUM_COLS):
        if all(board[row][column] == player_symbol for row in range(NUM_ROWS)):
            return True

    # Check for a diagonal win (top-left to bottom-right)
    for i