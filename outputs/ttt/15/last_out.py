def jdv():
  """
  This function implements the jdv game.
  """

  # Create the game board.
  board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
  ]

  # Get the player names.
  player1_name = input("Enter the name of player 1: ")
  player2_name = input("Enter the name of player 2: ")

  # Set the current player to player 1.
  current_player = player1_name

  # Set the game over flag to False.
  game_over = False

  # Create a list of the possible winning combinations.
  winning_combinations = [
    [(row, col) for col in range(3)] for row in range(3)
  ] + [
    [(row, col) for row in range(3)] for col in range(3)
  ] + [
    [(row, row) for row in range(3)],
    [(row, 2 - row) for row in range(3)]
  ]

  # Main game loop.
  while not game_over:

    # Display the game board.
    print("Current board:")
    for row in board:
      print(" ".join(row))

    # Get the current player's move.
    while True:
      move = input(f"{current_player}'s turn. Enter row and column (e.g. 1 2): ")

      try:
        row, column = map(int, move.split())
        if 0 <= row < 3 and 0 <= column < 3 and board[row][column] == " ":
          break
      except ValueError:
        pass

      print("Invalid move. Try again.")

    # Place the player's piece on the board.
    board[row][column] = current_player[0]

    # Check if the player has won.
    for combination in winning_combinations:
      if all(board[row][col] == current_player[0] for row, col in combination):
        game_over = True
        break

    # Check if the game is a draw.
    if not any(" " in row for row in board) and not game_over:
      game_over = True

    # Switch the current player.
    if current_player == player1_name:
      current_player = player2_name
    else:
      current_player = player1_name

  # Display the game result.
  if all(board[row][column] == current_player[0] for row, column in combination):
    print(f"{current_player} wins!")
  else:
    print("Draw!")

jdv()
