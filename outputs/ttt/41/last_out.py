import numpy as np
import pygame
import sys

# Create the game board.
board = np.zeros((4, 4))

# Create the two players.
players = [1, 2]

# Keep track of the current player.
current_player = 0

# Create the game window.
window = pygame.display.set_mode((400, 400))
pygame.display.set_caption("jdv")

# Create the game clock.
clock = pygame.time.Clock()

# Create the game font.
font = pygame.font.SysFont("Arial", 20)

# Create the game over surface.
game_over_surface = pygame.Surface((400, 400))
game_over_surface.fill((0, 0, 0))
game_over_text = font.render("Game Over", True, (255, 255, 255))
game_over_surface.blit(game_over_text, (150, 150))

# Create the leaderboard surface.
leaderboard_surface = pygame.Surface((400, 400))
leaderboard_surface.fill((0, 0, 0))
leaderboard_text = font.render("Leaderboard", True, (255, 255, 255))
leaderboard_surface.blit(leaderboard_text, (150, 150))

# Create the chat surface.
chat_surface = pygame.Surface((400, 100))
chat_surface.fill((0, 0, 0))
chat_text = font.render("Chat", True, (255, 255, 255))
chat_surface.blit(chat_text, (150, 50))

# Main game loop.
while True:
  # Handle events.
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
      # Get the mouse position.
      mouse_x, mouse_y = pygame.mouse.get_pos()

      # Convert the mouse position to a board position.
      board_x = mouse_x // 100
      board_y = mouse_y // 100

      # Check if the move is valid.
      if not (0 <= board_x < 4 and 0 <= board_y < 4):
        print("Invalid move.")
        continue

      # Check if the space is already occupied.
      if board[board_x, board_y] != 0:
        print("Space already occupied.")
        continue

      # Place the player's piece on the board.
      board[board_x, board_y] = players[current_player]

      # Check if the player has won.
      if check_win(board, players[current_player]):
        print("Player {} wins!".format(players[current_player]))
        window.blit(game_over_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(3000)
        pygame.quit()
        sys.exit()

      # Check if there is a draw.
      if np.all(board != 0):
        print("Draw!")
        window.blit(game_over_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(3000)
        pygame.quit()
        sys.exit()

      # Switch to the other player.
      current_player = (current_player + 1) % 2

  # Draw the game board.
  window.fill((255, 255, 255))
  for i in range(4):
    for j in range(4):
      if board[i, j] == 1:
        pygame.draw.circle(window, (255, 0, 0), (i * 100 + 50, j * 100 + 50), 40)
      elif board[i, j] == 2:
        pygame.draw.circle(window, (0, 0, 255), (i * 100 + 50, j * 100 + 50), 40)

  # Draw the chat surface.
  window.blit(chat_surface, (0, 300))

  # Update the display.
  pygame.display.update()

  # Clock tick.
  clock.tick(60)


def check_win(board, player):
  """
  This function checks if the player has won the game.

  Args:
    board: The game board.
    player: The player to check.

  Returns:
    True if the player has won, False otherwise.
  """

  # Check the rows.
  for row in board:
    if np.all(row == player):
      return True

  # Check the columns.
  for column in board.T:
    if np.all(column == player):
      return True

  # Check the diagonals.
  if np.all(board.diagonal() == player):
    return True

  if np.all(np.flip(board).diagonal() == player):
    return True

  # No win.
  return False
