import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

def jdv():
  """
  JdV game.

  Two players take turns placing their pieces in a free space of a 3x3 grid, until one of them makes a line with 3 (horizontally, vertically or diagonally) adjacent pieces, in which case the person that made the line loses, and the opponent is the winner. 
  If there are no more free spaces, the game is declared a draw.
  """

  # Initialize the game board
  board = np.zeros((3, 3), dtype=int)

  # Initialize the player turn
  player = 1

  # Create an AI opponent
  ai = AI()

  # Create the graphical user interface
  root = tk.Tk()
  root.title("JdV game")

  canvas = tk.Canvas(root, width=300, height=300)
  canvas.pack()

  def draw_board():
    """
    Draw the game board.
    """

    for row in range(3):
      for col in range(3):
        if board[row, col] == 1:
          canvas.create_oval(col * 100 + 10, row * 100 + 10, col * 100 + 90, row * 100 + 90, fill="red")
        elif board[row, col] == 2:
          canvas.create_oval(col * 100 + 10, row * 100 + 10, col * 100 + 90, row * 100 + 90, fill="blue")

  def get_human_move(event):
    """
    Get the human player's move.

    Args:
      event: The event object.
    """

    row = event.y // 100
    col = event.x // 100

    if 0 <= row < 3 and 0 <= col < 3 and board[row, col] == 0:
      board[row, col] = player
      draw_board()

      # Check if the player has won
      if check_win(board, player):
        print("Player {} wins!".format(player))
        root.destroy()
      elif np.all(board != 0):
        print("Draw!")
        root.destroy()

      # Switch to the other player
      player = 3 - player

      # Get the AI's move
      row, col = ai.get_move(board, difficulty)

      # Update the game board
      board[row, col] = player

      # Draw the board
      draw_board()

      # Check if the AI has won
      if check_win(board, player):
        print("Player {} wins!".format(player))
        root.destroy()
      elif np.all(board != 0):
        print("Draw!")
        root.destroy()

  # Bind the mouse click event to the get_human_move function
  canvas.bind("<Button-1>", get_human_move)

  # Choose the difficulty level
  difficulty = input("Choose the difficulty level (easy, medium, hard): ")

  # Draw the initial board
  draw_board()

  # Start the game loop
  root.mainloop()

def check_win(board, player):
  """
  Check if the player has won.

  Args:
    board: The game board.
    player: The player to check.

  Returns:
    True if the player has won, False otherwise.
  """

  # Check for horizontal wins
  for row in range(3):
    if np.all(board[row, :] == player):
      return True

  # Check for vertical wins
  for col in range(3):
    if np.all(board[:, col] == player):
      return True

  # Check for diagonal wins
  if np.all(np.diag(board) == player) or np.all(np.diag(np.flip(board, axis=0)) == player):
    return True

  # No win
  return False

class AI:
  """
  AI opponent for the JdV game.
  """

  def __init__(self):
    self.player = 2  # The AI always plays as player 2

  def get_move(self, board, difficulty):
    """
    Get the AI's move.

    Args:
      board: The game board.
      difficulty: The difficulty level.

    Returns:
      A tuple (row, column) representing the AI's move.
    """

    if difficulty == "easy":
      # Choose a random move
      while True:
        row = np.random.randint(0, 3)
        col = np.random.randint(0, 3)
        if board[row, col] == 0:
          return row, col
    elif difficulty == "medium":
      # Check if the AI can win in one move
      for row in range(3):
        for col in range(3):
          if board[row, col] == 0:
            board[row, col] = self.player
            if check_win(board, self.player):
              board[row, col] = 0
              return row, col

      # Check if the human player can win in one move
      for row in range(3):
        for col in range(3):
          if board[row, col] == 0:
            board[row, col] = 3 - self.player
            if check_win(board, 3 - self.player):
              board[row, col] = 0
              return row, col

      # Choose a random move
      while True:
        row = np.random.randint(0, 3)
        col = np.random.randint(0, 3)
        if board[row, col] == 0:
          return row, col
    elif difficulty == "hard":
      # Use the minimax algorithm to find the best move
      best_score = -np.inf
      best_move = None

      for row in range(3):
        for col in range(3):
          if board[row, col] == 0:
            board[row, col] = self.player
            score = self.minimax(board, 3 - self.player, False)
            board[row, col] = 0
            if score > best_score:
              best_score = score
              best_move = (row, col)

      return best_move

  def minimax(self, board, player, maximizing):
    """
    Use the minimax algorithm to find the best move.

    Args:
      board: The game board.
      player: The player to check.
      maximizing: True if the player is maximizing their score, False otherwise.

    Returns:
      The best score for the player.
    """

    # Check if the game is over
    if check_win(board, player):
      return 1 if maximizing else -1
    elif np.all(board != 0):
      return 0

    # Find the best move for the player
    best_score = -np.inf if maximizing else np.inf

    for row in range(3):
      for col in range(3):
        if board