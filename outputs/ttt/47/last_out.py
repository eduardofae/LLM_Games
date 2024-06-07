import numpy as np

def jdv():
  """
  Plays a game of JDV.

  Returns:
    The winner of the game, or None if the game is a draw.
  """

  # Create a 3x3 grid.
  board = np.zeros((3, 3), dtype=int)

  # Set the current player to 1.
  player = 1

  # Set the players' names and pieces.
  player1_name = input("Player 1's name: ")
  player1_piece = input("Player 1's piece: ")
  player2_name = input("Player 2's name: ")
  player2_piece = input("Player 2's piece: ")

  # Keep track of the number of moves that have been made.
  number_of_moves = 0

  # Keep track of the number of wins for each player.
  player1_wins = 0
  player2_wins = 0

  # Loop until the game is over.
  while True:
    # Print the game board.
    print_board(board)

    # Get the player's move.
    try:
      row, col = map(int, input("{}'s move (row, col): ".format(player1_name if player == 1 else player2_name)).split())
    except ValueError:
      print("Invalid input. Please enter two integers separated by a comma (e.g. 0, 1).")
      continue

    # Check if the move is valid.
    if not is_valid_move(board, row, col):
      print("Invalid move. Try again.")
      continue

    # Place the player's piece on the grid.
    board[row, col] = player

    # Increment the number of moves.
    number_of_moves += 1

    # Check if the player has won.
    if check_win(board, player):
      if player == 1:
        player1_wins += 1
      else:
        player2_wins += 1
      print("{} wins!".format(player1_name if player == 1 else player2_name))
      return player

    # Check if the game is a draw.
    if number_of_moves == 9:
      print("Draw!")
      return None

    # Switch to the other player.
    player = 3 - player

def is_valid_move(board, row, col):
  """
  Checks if a move is valid.

  Args:
    board: The game board.
    row: The row of the move.
    col: The column of the move.

  Returns:
    True if the move is valid, False otherwise.
  """

  return board[row, col] == 0 and number_of_moves < 9

def check_win(board, player):
  """
  Checks if the player has won the game.

  Args:
    board: The game board.
    player: The player to check.

  Returns:
    True if the player has won, False otherwise.
  """

  # Check for a horizontal win.
  for row in range(3):
    if np.all(board[row, :] == player):
      return True

  # Check for a vertical win.
  for col in range(3):
    if np.all(board[:, col] == player):
      return True

  # Check for a diagonal win.
  if np.all(np.diagonal(board) == player):
    return True

  if np.all(np.flipud(board).diagonal() == player):
    return True

  # No win found.
  return False

def print_board(board):
  """
  Prints the game board.

  Args:
    board: The game board.
  """

  for row in board:
    for col in row:
      if col == 0:
        print(" ", end=" ")
      elif col == 1:
        print(player1_piece, end=" ")
      elif col == 2:
        print(player2_piece, end=" ")
    print()

def reset_game():
  """
  Resets the game.
  """

  # Create a new 3x3 grid.
  board = np.zeros((3, 3), dtype=int)

  # Set the current player to 1.
  player = 1

  # Reset the number of moves that have been made.
  number_of_moves = 0

  # Reset the number of wins for each player.
  player1_wins = 0
  player2_wins = 0

def save_game(board, player, number_of_moves, player1_wins, player2_wins):
  """
  Saves the game to a file.

  Args:
    board: The game board.
    player: The current player.
    number_of_moves: The number of moves that have been made.
    player1_wins: The number of wins for player 1.
    player2_wins: The number of wins for player 2.
  """

  with open("game.txt", "w") as f:
    f.write(str(board))
    f.write("\n")
    f.write(str(player))
    f.write("\n")
    f.write(str(number_of_moves))
    f.write("\n")
    f.write(str(player1_wins))
    f.write("\n")
    f.write(str(player2_wins))

def load_game():
  """
  Loads a game from a file.

  Returns:
    The game board, the current player, the number of moves that have been made, the number of wins for player 1, and the number of wins for player 2.
  """

  with open("game.txt", "r") as f:
    board = np.array(eval(f.readline()))
    player = int(f.readline())
    number_of_moves = int(f.readline())
    player1_wins = int(f.readline())
    player2_wins = int(f.readline())

  return board, player, number_of_moves, player1_wins, player2_wins

if __name__ == "__main__":
  while True:
    # Print the menu.
    print("1. Play game")
    print("2. Reset game")
    print("3. Save game")
    print("4. Load game")
    print("5. Quit")

    # Get the player's choice.
    choice = input("Enter your choice: ")

    # Handle the player's choice.
    if choice == "1":
      jdv()
    elif choice == "2":
      reset_game()
    elif choice == "3":
      save_game(board, player, number_of_moves, player1_wins, player2_wins)
    elif choice == "4":
      board, player, number_of_moves, player1_wins, player2_wins = load_game()
    elif choice == "5":
      break
    else:
      print("Invalid choice. Please try again.")
