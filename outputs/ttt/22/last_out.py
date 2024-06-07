import pygame

# Define the game board
board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

# Define the players
players = ['X', 'O']

# Define the current player
current_player = 0

# Define the game state
game_state = 'playing'

# Define the AI player
ai_player = 'O'

# Define the AI difficulty
ai_difficulty = 1

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

# Define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Define the font
font = pygame.font.SysFont('Arial', 30)

# Define the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Get the mouse position
            pos = pygame.mouse.get_pos()
            
            # Convert the mouse position to row and column indices
            row = pos[1] // 100
            col = pos[0] // 100
            
            # Check if the move is valid
            if is_valid_move(row, col):
                # Make the move
                make_move(players[current_player], row, col)
                
                # Check if there is a winner
                winner = check_winner()
                
                # Check if there is a winner
                if winner is not None:
                    if winner == 'draw':
                        print("The game is a draw.")
                    else:
                        print(f"{winner} wins!")
                    game_state = 'finished'
                
                # Switch to the other player
                current_player = (current_player + 1) % len(players)
    
    # Make the AI move
    if current_player == ai_player and game_state == 'playing':
        # Get the best move
        row, col = get_best_move(board, ai_player, ai_difficulty)
        
        # Make the move
        make_move(ai_player, row, col)
        
        # Check if there is a winner
        winner = check_winner()
        
        # Check if there is a winner
        if winner is not None:
            if winner == 'draw':
                print("The game is a draw.")
            else:
                print(f"{winner} wins!")
            game_state = 'finished'
        
        # Switch to the other player
        current_player = (current_player + 1) % len(players)
    
    # Draw the game board
    screen.fill(BLACK)
    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                pygame.draw.line(screen, RED, (col * 100, row * 100), (col * 100 + 100, row * 100 + 100), 5)
                pygame.draw.line(screen, RED, (col * 100, row * 100 + 100), (col * 100 + 100, row * 100), 5)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, BLUE, (col * 100 + 50, row * 100 + 50), 50, 5)
    
    # Update the screen
    pygame.display.update()

# Quit Pygame
pygame.quit()
