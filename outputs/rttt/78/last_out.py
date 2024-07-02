import numpy as np
import pygame

def play_jdv():
  """
  Plays a game of jdv, a 3x3 grid game where players take turns placing their pieces until one of them makes a line of 3 adjacent pieces.

  Returns:
    The winner of the game, or None if the game is a draw.
  """

  # Initialize the PyGame display
  pygame.init()
  screen = pygame.display.set_mode((600, 600))
  clock = pygame.time.Clock()

  # Create a 3x3 grid
  grid = np.array([[" ", " ", " "] for _ in range(3)])

  # Get the names of the two players
  player1 = input("Player 1, what is your name? ")
  player2 = input("Player 2, what is your name? ")

  # Determine who goes first
  current_player = player1

  # Create the game history
  game_history = []

  # Main game loop
  running = True
  while running:
    # Handle events
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      elif event.type == pygame.MOUSEBUTTONDOWN:
        # Get the mouse position
        pos = pygame.mouse.get_pos()

        # Convert the mouse position to a row and column on the grid
        row = pos[1] // 200
        col = pos[0] // 200

        # Check if the selected cell is empty
        if grid[row, col] == " ":
          # Place the current player's piece in the grid
          grid[row, col] = current_player

          # Add the move to the game history
          game_history.append((row, col))

          # Check if the current player has won
          if is_winner(grid, current_player):
            print(f"{current_player} wins!")
            running = False

          # Check if there is a draw
          if is_draw(grid):
            print("The game is a draw.")
            running = False

          # Switch to the other player
          current_player = player2 if current_player == player1 else player1

    # Draw the game board
    draw_board(screen, grid)

    # Flip the display
    pygame.display.flip()

    # Tick the clock
    clock.tick(60)

def draw_board(screen, grid):
  """
  Draws the game board on the screen.

  Args:
    screen: The PyGame display surface.
    grid: The game grid.
  """

  # Clear the screen
  screen.fill((255, 255, 255))

  # Draw the grid lines
  for i in range(1, 3):
    pygame.draw.line(screen, (0, 0, 0), (200 * i, 0), (200 * i, 600))
    pygame.draw.line(screen, (0, 0, 0), (0, 200 * i), (600, 200 * i))

  # Draw the player pieces
  for row in range(3):
    for col in range(3):
      if grid[row, col] == "X":
        pygame.draw.circle(screen, (255, 0, 0), (200 * col + 100, 200 * row + 100), 50)
      elif grid[row, col] == "O":
        pygame.draw.circle(screen, (0, 0, 255), (200 * col + 100, 200 * row + 100), 50)

def is_winner(grid, player):
  """
  Checks if the given player has won the game.

  Args:
    grid: The game grid.
    player: The player to check.

  Returns:
    True if the player has won, False otherwise.
  """

  # Check for horizontal wins
  for row in grid:
    if all(row == player):
      return True

  # Check for vertical wins
  for col in range(3):
    if all(grid[:, col] == player):
      return True

  # Check for diagonal wins
  if all(grid.diagonal() == player) or all(np.flip(grid).diagonal() == player):
    return True

  # No wins found
  return False

def is_draw(grid):
  """
  Checks if the game is a draw.

  Args:
    grid: The game grid.

  Returns:
    True if the game is a draw, False otherwise.
  """

  # Check if there are any empty spaces left
  return not any(grid == " ")

if __name__ == "__main__":
  play_jdv()
