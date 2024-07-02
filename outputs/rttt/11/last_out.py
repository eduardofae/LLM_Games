def play_jdv_game():
  """
  This function implements the jdv game, where 2 players place their pieces in a 3x3 grid until one of them makes a line with 3 (horizontally, vertically or diagonally) adjacent pieces.

  Args:
    None

  Returns:
    None
  """

  # Create the game board
  jdv_board = np.zeros((3, 3))

  # Create a list of the possible winning lines
  winning_lines = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
  ]

  # Get the player's input
  while True:
    try:
      # Get the player's move
      move = input("Enter your move (1-9): ")

      # Check if the move is valid
      if not move.isdigit() or int(move) < 1 or int(move) > 9 or jdv_board[int(move)-1] != 0:
        print("Invalid move. Please try again.")
        continue

      # Place the player's piece on the board
      jdv_board[int(move)-1] = 1

      # Check if the player has won
      for line in winning_lines:
        if jdv_board[line[0]] == jdv_board[line[1]] == jdv_board[line[2]] != 0:
          print("Player", jdv_board[line[0]], "wins!")
          return

      # Check if the game is a draw
      if np.all(jdv_board != 0):
        print("Draw!")
        return

      # Swap players
      jdv_board[int(move)-1] = 2

      # Check if the player has won
      for line in winning_lines:
        if jdv_board[line[0]] == jdv_board[line[1]] == jdv_board[line[2]] != 0:
          print("Player", jdv_board[line[0]], "wins!")
          return

      # Check if the game is a draw
      if np.all(jdv_board != 0):
        print("Draw!")
        return

    except ValueError:
      print("Invalid input. Please enter a number between 1 and 9.")


if __name__ == "__main__":
  play_jdv_game()
