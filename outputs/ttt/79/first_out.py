import numpy as np

def jdv():
  """
  This function implements the jdv game.

  Args:
    None

  Returns:
    None
  """

  # Create the game board
  board = np.zeros((3, 3))

  # Set the current player to 1
  current_player = 1

  # Set the game state to ongoing
  game_state = "ongoing"

  # Play the game until someone wins or there is a draw
  while game_state == "ongoing":
    # Get the player's move
    move = get_player_move(board, current_player)

    # Update the board
    board[move[0], move[1]] = current_player

    # Check if the player has won
    if check_win(board, current_player):
      game_state = "win"
      print(f"Player {current_player} wins!")
    else:
      # Check if there are any more free spaces
      if np.all(board != 0):
        game_state = "draw"
        print("Draw!")
      else:
        # Switch to the other player
        current_player = 3 - current_player

def get_player_move(board, current_player):
  """
  This function gets the player's move.

  Args:
    board: The current state of the game board.
    current_player: The current player.

  Returns:
    A tuple of the player's move.
  """

  # Get the player's input
  move = input(f"Player {current_player}, enter your move (row, column): ")

  # Convert the player's input to a tuple
  move = tuple(int(x) for x in move.split(", "))

  # Check if the player's move is valid
  while not is_valid_move(board, move):
    print("Invalid move. Please try again.")
    move = input(f"Player {current_player}, enter your move (row, column): ")
    move = tuple(int(x) for x in move.split(", "))

  # Return the player's move
  return move

def is_valid_move(board, move):
  """
  This function checks if a move is valid.

  Args:
    board: The current state of the game board.
    move: The player's move.

  Returns:
    True if the move is valid, False otherwise.
  """

  # Check if the move is within the bounds of the board
  if move[0] < 0 or move[0] > 2 or move[1] < 0 or move[1] > 2:
    return False

  # Check if the space is already occupied
  if board[move[0], move[1]] != 0:
    return False

  # The move is valid
  return True

def check_win(board, current_player):
  """
  This function checks if a player has won.

  Args:
    board: The current state of the game board.
    current_player: The current player.

  Returns:
    True if the player has won, False otherwise.
  """

  # Check for a win in the rows
  for row in range(3):
    if all(board[row, :] == current_player):
      return True

  # Check for a win in the columns
  for col in range(3):
    if all(board[:, col] == current_player):
      return True

  # Check for a win in the diagonals
  if all(board.diagonal() == current_player) or all(np.flip(board).diagonal() == current_player):
    return True

  # The player has not won
  return False

if __name__ == "__main__":
  jdv()
