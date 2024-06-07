import numpy as np

def play_jdv(board_size=3, num_players=2, starting_player=1, game_mode="normal"):
  """
  Plays a game of jdv.

  Args:
    board_size: The size of the game board (default is 3).
    num_players: The number of players (default is 2).
    starting_player: The player who starts the game (default is 1).
    game_mode: The game mode (default is "normal").

  Returns:
    The winner of the game, or None if the game is a draw.
  """

  # Error handling
  if board_size < 3 or board_size > 10:
    raise ValueError("Invalid board size. Please choose a board size between 3 and 10.")
  if num_players < 2 or num_players > 4:
    raise ValueError("Invalid number of players. Please choose a number of players between 2 and 4.")
  if starting_player < 1 or starting_player > num_players:
    raise ValueError("Invalid starting player. Please choose a starting player between 1 and the number of players.")
  if game_mode not in ["normal", "timed", "moves"]:
    raise ValueError("Invalid game mode. Please choose a game mode from normal, timed, or moves.")

  # Welcome message
  print("Welcome to jdv! This is a game where two players take turns placing their pieces in a free space of a board, until one of them makes a line with 3 (horizontally, vertically or diagonally) adjacent pieces, in which case the person that made the line loses, and the opponent is the winner. If there are no more free spaces, the game is declared a draw.")

  # Create a board
  board = np.zeros((board_size, board_size), dtype=int)

  # Get the names of the players
  players = []
  for i in range(num_players):
    player = input(f"Player {i + 1}, enter your name: ")
    players.append(player)

  # Initialize the number of wins for each player
  player_wins = {player: 0 for player in players}

  # Start the game
  turn = starting_player
  num_moves = 0
  while True:
    # Get the player's move
    player = players[turn - 1]

    move = input(f"{player}, enter your move (row, column): ")
    try:
      row, column = map(int, move.split(","))
    except ValueError:
      print("Invalid move. Please try again.")
      continue

    # Check if the move is valid
    if not (0 <= row < board_size and 0 <= column < board_size):
      print("Invalid move. Please try again.")
      continue
    if board[row, column] != 0:
      print("Invalid move. Please try again.")
      continue

    # Place the player's piece on the board
    board[row, column] = turn
    num_moves += 1

    # Check if the player has won
    if check_win(board, turn):
      print(f"{player} wins!")
      player_wins[player] += 1
      return turn

    # Check if the game is a draw
    if num_moves == board_size ** 2:
      print("Draw!")
      return None

    # Switch turns
    turn = 3 - turn

def check_win(grid, turn):
  """
  Checks if the given player has won the game.

  Args:
    grid: The game grid.
    turn: The player's turn (1 or 2).

  Returns:
    True if the player has won, False otherwise.
  """

  # Check for a win in each row
  for row in range(grid.shape[0]):
    if np.all(grid[row, :] == turn):
      return True

  # Check for a win in each column
  for column in range(grid.shape[1]):
    if np.all(grid[:, column] == turn):
      return True

  # Check for a win in each diagonal
  if np.all(grid.diagonal() == turn):
    return True
  if np.all(np.flip(grid).diagonal() == turn):
    return True

  # No win yet
  return False


if __name__ == "__main__":
  while True:
    winner = play_jdv()
    if winner is not None:
      print(f"{winner} wins!")
    else:
      print("Draw!")

    play_again = input("Do you want to play again? (y/n) ")
    if play_again == "n":
      break
