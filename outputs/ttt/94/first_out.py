def jdv():
  """
  This function implements the jdv game, where two players take turns placing their pieces in a free space of a 3x3 grid, until one of them makes a line with 3 (horizontally, vertically or diagonally) adjacent pieces, in which case the person that made the line wins. If there are no more free spaces, the game is declared a draw.
  """

  # Create the game board
  board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

  # Create a list of the possible winning combinations
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

  # Create a variable to keep track of the current player
  current_player = 'X'

  # Create a variable to keep track of the number of moves that have been made
  num_moves = 0

  # Create a variable to keep track of the winner
  winner = None

  # Create a function to check if a player has won
  def check_winner(player):
    """
    This function checks if a player has won the game.

    Args:
      player: The player to check for a win.

    Returns:
      True if the player has won, False otherwise.
    """

    # Check each of the possible winning combinations to see if the player has won
    for combination in winning_combinations:
      if all(board[x][y] == player for x, y in combination):
        return True

    # If the player has not won, return False
    return False

  # Create a function to get the next move from a player
  def get_next_move(player):
    """
    This function gets the next move from a player.

    Args:
      player: The player to get the next move from.

    Returns:
      A tuple representing the next move.
    """

    # Get the player's move
    move = input(f"{player}'s turn. Enter your move (row, column): ")

    # Convert the player's move to a tuple
    move = tuple(int(x) for x in move.split(','))

    # Check if the player's move is valid
    if move[0] < 0 or move[0] > 2 or move[1] < 0 or move[1] > 2 or board[move[0]][move[1]] != ' ':
      print("Invalid move. Please try again.")
      return get_next_move(player)

    # Return the player's move
    return move

  # Play the game until someone wins or there is a draw
  while not winner and num_moves < 9:
    # Get the next move from the current player
    move = get_next_move(current_player)

    # Place the player's piece on the board
    board[move[0]][move[1]] = current_player

    # Increment the number of moves
    num_moves += 1

    # Check if the current player has won
    winner = check_winner(current_player)

    # If the current player has not won, switch to the other player
    if not winner:
      current_player = 'O' if current_player == 'X' else 'X'

  # Print the game board
  for row in board:
    print(' '.join(row))

  # Declare the winner or draw
  if winner:
    print(f"{winner} wins!")
  else:
    print("Draw!")

# Play the game
jdv()
