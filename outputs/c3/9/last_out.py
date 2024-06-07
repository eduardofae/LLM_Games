import numpy as np
import turtle

def check_winner(board):
  """
  Checks if there is a winner in the board.

  Args:
    board: A numpy array representing the game board.

  Returns:
    The player number of the winner, or 0 if there is no winner.
  """

  # Check for horizontal wins
  for row in range(10):
    for col in range(7):
      if board[row, col] != 0 and board[row, col] == board[row, col + 1] and board[row, col] == board[row, col + 2] and board[row, col] == board[row, col + 3]:
        return board[row, col]

  # Check for vertical wins
  for col in range(10):
    for row in range(6):
      if board[row, col] != 0 and board[row, col] == board[row + 1, col] and board[row, col] == board[row + 2, col] and board[row, col] == board[row + 3, col]:
        return board[row, col]

  # Check for diagonal wins
  for row in range(6):
    for col in range(7):
      if board[row, col] != 0 and board[row, col] == board[row + 1, col + 1] and board[row, col] == board[row + 2, col + 2] and board[row, col] == board[row + 3, col + 3]:
        return board[row, col]

      if board[row, col] != 0 and board[row, col] == board[row + 1, col - 1] and board[row, col] == board[row + 2, col - 2] and board[row, col] == board[row + 3, col - 3]:
        return board[row, col]

  # No winner yet
  return 0

def print_board(board):
  """
  Prints the game board to the console.

  Args:
    board: A numpy array representing the game board.
  """

  for row in range(10):
    for col in range(10):
      if board[row, col] == 0:
        print(" ", end=" ")
      elif board[row, col] == 1:
        print("X", end=" ")
      elif board[row, col] == 2:
        print("O", end=" ")
    print()

def get_player_move(board):
  """
  Gets the player's move.

  Args:
    board: A numpy array representing the game board.

  Returns:
    The player's move.
  """

  while True:
    move = int(input("Player {}'s turn: ".format(player)))
    if move < 1 or move > 10:
      print("Invalid move. Please enter a number between 1 and 10.")
    elif board[9, move - 1] != 0:
      print("Invalid move. That column is full.")
    else:
      return move

def is_game_over(board):
  """
  Checks if the game is over.

  Args:
    board: A numpy array representing the game board.

  Returns:
    True if the game is over, False otherwise.
  """

  # Check if there are any more moves available
  if np.all(board != 0):
    return True

  # Check if there is a winner
  if check_winner(board) != 0:
    return True

  # The game is not over
  return False

def draw_board(board):
  """
  Draws the game board to the screen using the turtle module.

  Args:
    board: A numpy array representing the game board.
  """

  # Set up the turtle screen
  turtle.setup(600, 600)
  turtle.bgcolor("white")
  turtle.speed(0)

  # Draw the game board
  for row in range(10):
    for col in range(10):
      if board[row, col] == 0:
        # Draw an empty square
        turtle.penup()
        turtle.goto(col * 60, row * 60)
        turtle.pendown()
        turtle.forward(60)
        turtle.left(90)
        turtle.forward(60)
        turtle.left(90)
        turtle.forward(60)
        turtle.left(90)
        turtle.forward(60)
        turtle.left(90)
      elif board[row, col] == 1:
        # Draw an X
        turtle.penup()
        turtle.goto(col * 60 + 30, row * 60 + 30)
        turtle.pendown()
        turtle.goto(col * 60 - 30, row * 60 - 30)
        turtle.penup()
        turtle.goto(col * 60 - 30, row * 60 + 30)
        turtle.pendown()
        turtle.goto(col * 60 + 30, row * 60 - 30)
      elif board[row, col] == 2:
        # Draw an O
        turtle.penup()
        turtle.goto(col * 60 + 30, row * 60 + 30)
        turtle.pendown()
        turtle.circle(30)

  # Update the turtle screen
  turtle.update()

def play_sound(sound_file):
  """
  Plays a sound
  """