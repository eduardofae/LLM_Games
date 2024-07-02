import numpy as np
import random
import pygame

# Define the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

# Define the game board
board = np.zeros((3, 3))

# Define the players
players = ['X', 'O']

# Define the difficulty levels
difficulty_levels = ['easy', 'medium', 'hard']

# Define the game modes
game_modes = ['singleplayer', 'multiplayer']

# Start the game
while True:
  # Get the game mode from the user
  game_mode = input("Choose a game mode (singleplayer, multiplayer): ")

  # Check if the game mode is valid
  if game_mode not in game_modes:
    print("Invalid game mode. Please choose singleplayer or multiplayer.")
    continue

  # Get the difficulty level from the user (if singleplayer)
  if game_mode == 'singleplayer':
    difficulty_level = input("Choose a difficulty level (easy, medium, hard): ")

    # Check if the difficulty level is valid
    if difficulty_level not in difficulty_levels:
      print("Invalid difficulty level. Please choose easy, medium, or hard.")
      continue

    # Set the computer player's algorithm based on the difficulty level
    if difficulty_level == 'easy':
      computer_algorithm = get_random_move
    elif difficulty_level == 'medium':
      computer_algorithm = get_best_move
    elif difficulty_level == 'hard':
      computer_algorithm = get_optimal_move
    else:
      print("Invalid difficulty level. Please choose easy, medium, or hard.")
      continue

  # Initialize the Pygame window
  pygame.init()
  screen = pygame.display.set_mode((300, 300))
  pygame.display.set_caption('Jdv')

  # Main game loop
  while True:
    # Handle events
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
      elif event.type == pygame.MOUSEBUTTONDOWN:
        # Get the mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Convert the mouse position to a row and column on the game board
        row = mouse_y // 100
        column = mouse_x // 100

        # Check if the move is valid
        if board[row, column] != 0:
          print("Invalid move. Please try again.")
          continue

        # Place the player's piece on the board
        board[row, column] = players[0]

        # Check if the player has won
        if check_win(board, players[0]):
          print(f"Player {players[0]} has won!")
          pygame.quit()
          sys.exit()

        # Check if the game is a draw
        if np.all(board != 0):
          print("The game is a draw.")
          pygame.quit()
          sys.exit()

        # Switch to the other player
        players = players[1:]

        # If the game mode is singleplayer, get the computer's move
        if game_mode == 'singleplayer':
          row, column = computer_algorithm(board)

          # Place the computer's piece on the board
          board[row, column] = players[0]

          # Check if the computer has won
          if check_win(board, players[0]):
            print(f"Player {players[0]} has won!")
            pygame.quit()
            sys.exit()

          # Check if the game is a draw
          if np.all(board != 0):
            print("The game is a draw.")
            pygame.quit()
            sys.exit()

          # Switch to the other player
          players = players[1:]

    # Draw the game board
    screen.fill(WHITE)
    for row in range(3):
      for column in range(3):
        if board[row, column] == 'X':
          pygame.draw.line(screen, RED, (column * 100, row * 100), (column * 100 + 100, row * 100 + 100), 5)
          pygame.draw.line(screen, RED, (column * 100 + 100, row * 100), (column * 100, row * 100 + 100), 5)
        elif board[row, column] == 'O':
          pygame.draw.circle(screen, BLUE, (column * 100 + 50, row * 100 + 50), 50, 5)

    # Update the display
    pygame.display.update()
