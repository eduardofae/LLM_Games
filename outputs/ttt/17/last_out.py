import numpy as np

def jdv():
  """
  This function implements the jdv game.
  """

  # Get the size of the game board.
  size = int(input("Enter the size of the game board: "))

  # Create the game board.
  board = np.zeros((size, size))

  # Get the players' names.
  players = []
  for i in range(1, size + 1):
    player = input(f"Player {i}, enter your name: ")
    players.append(player)

  # Set the current player to player 1.
  current_player = players[0]

  # Set the players' scores to 0.
  scores = {player: 0 for player in players}

  # Play the game until someone wins or there is a draw.
  while True:
    # Get the current player's move.
    move = input(f"{current_player}, enter your move (row, column): ")

    # Convert the move to a row and column.
    row, column = map(int, move.split(","))

    # Check if the move is valid.
    if not (0 <= row < size and 0 <= column < size and board[row, column] == 0):
      print("Invalid move.")
      continue

    # Place the current player's piece on the board.
    board[row, column] = players.index(current_player) + 1

    # Check if the current player has won.
    if check_win(board, current_player):
      print(f"{current_player} wins!")
      scores[current_player] += 1
      break

    # Check if there is a draw.
    if np.all(board != 0):
      print("Draw!")
      break

    # Switch to the next player.
    current_player = players[(players.index(current_player) + 1) % len(players)]

  # Print the scores.
  print("Scores:")
  for player, score in scores.items():
    print(f"{player}: {score}")

  # Ask the players if they want to play again.
  play_again = input("Do you want to play again? (y/n) ")

  if play_again == "y":
    # Reset the game board.
    board = np.zeros((size, size))

    # Reset the players' scores.
    scores = {player: 0 for player in players}

    # Start a new game.
    jdv()
  else:
    # Exit the game.
    print("Goodbye!")


def check_win(board, player):
  """
  This function checks if the given player has won the game.

  Args:
    board: The game board.
    player: The player to check.

  Returns:
    True if the player has won, False otherwise.
  """

  # Check the rows.
  for row in range(board.shape[0]):
    if np.all(board[row, :] == player):
      return True

  # Check the columns.
  for column in range(board.shape[1]):
    if np.all(board[:, column] == player):
      return True

  # Check the diagonals.
  if np.all(board.diagonal() == player) or np.all(np.flip(board).diagonal() == player):
    return True

  return False


if __name__ == "__main__":
  jdv()
