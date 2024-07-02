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
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
  ]

  # Main game loop.
  while not game_over:

    # Display the game board.
    print("Current board:")
    for row in board:
      print(" ".join(row))

    # Get the current player's move.
    move = input(f"{current_player}'s turn. Enter row and column (e.g. 1 2): ")

    # Convert the move to a tuple of integers.
    row, column = map(int, move.split())

    # Check if the move is valid.
    if not (0 <= row < 3 and 0 <= column < 3 and board[row][column] == " "):
      print("Invalid move. Try again.")
      continue

    # Place the player's piece on the board.
    board[row][column] = current_player[0]

    # Check if the player has won.
    for combination in winning_combinations:
      if all(board[row][column] == current_player[0] for row, column in combination):
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
  if game_over:
    if all(board[row][column] == current_player[0] for row, column in combination):
      print(f"{current_player} wins!")
    else:
      print("Draw!")

jdv()