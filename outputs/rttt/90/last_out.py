import numpy as np

def jdv():
  """
  jdv game
  """

  # Create the game board
  board = np.zeros((3, 3))

  # Player 1 is 'X' and Player 2 is 'O'
  player1 = 'X'
  player2 = 'O'

  # Keep track of whose turn it is
  turn = player1

  # Keep track of the number of moves made
  move_count = 0

  # Keep track of the winner
  winner = None

  # Keep track of the number of wins and losses for each player
  wins = {player1: 0, player2: 0}
  losses = {player1: 0, player2: 0}

  # Game loop
  while True:
    # Print the game board
    print(board)

    # Get the player's move
    if turn == player1:
      move = input(f"{turn}'s turn. Enter a row and column (e.g. 1,2): ")
    else:
      # Get the computer opponent's move
      move = get_computer_move(board, turn)

    row, col = map(int, move.split(','))

    # Check if the move is valid
    if board[row, col] != 0:
      print("Invalid move. That space is already taken.")
      continue

    # Place the player's piece on the board
    board[row, col] = turn

    # Increment the move count
    move_count += 1

    # Check if the player has won
    if check_win(board, turn):
      winner = turn
      break

    # Check if the game is a draw
    if move_count == 9:
      break

    # Switch turns
    if turn == player1:
      turn = player2
    else:
      turn = player1

  # Print the winner
  if winner is not None:
    print(f"{winner} wins!")
    wins[winner] += 1
    losses[get_opponent(winner)] += 1
  else:
    print("Draw!")

  # Print the number of wins and losses for each player
  print("Wins:")
  for player, wins in wins.items():
    print(f"{player}: {wins}")

  print("Losses:")
  for player, losses in losses.items():
    print(f"{player}: {losses}")

def check_win(board, player):
  """
  Checks if a player has won the game.
  
  Args:
    board: The game board.
    player: The player to check for.
  
  Returns:
    True if the player has won, False otherwise.
  """

  # Check for a win in each row
  for row in board:
    if np.all(row == player):
      return True

  # Check for a win in each column
  for col in board.T:
    if np.all(col == player):
      return True

  # Check for a win in each diagonal
  if np.all(board.diagonal() == player) or np.all(np.flip(board).diagonal() == player):
    return True

  # No win yet
  return False

def get_computer_move(board, player):
  """
  Gets the computer opponent's move.
  
  Args:
    board: The game board.
    player: The player to check for.
  
  Returns:
    The computer opponent's move.
  """

  # Find all possible moves
  possible_moves = []
  for row in range(3):
    for col in range(3):
      if board[row, col] == 0:
        possible_moves.append((row, col))

  # Evaluate each possible move
  best_move = None
  best_score = -np.inf
  for move in possible_moves:
    # Make the move
    board[move[0], move[1]] = player

    # Check if the move leads to a win
    if check_win(board, player):
      return move

    # Evaluate the move
    score = minimax(board, player, 2)

    # Undo the move
    board[move[0], move[1]] = 0

    # If the move is better than the current best move, update the best move and score
    if score > best_score:
      best_move = move
      best_score = score

  # Return the best move
  return best_move

def minimax(board, player, depth):
  """
  Performs a minimax search to evaluate a move.
  
  Args:
    board: The game board.
    player: The player to check for.
    depth: The depth of the search.
  
  Returns:
    The score of the move.
  """

  # Check if the game is over
  winner = check_win(board, player)
  if winner is not None:
    if winner == player:
      return 1
    else:
      return -1

  # Check if the depth limit has been reached
  if depth == 0:
    return 0

  # Find all possible moves
  possible_moves = []
  for row in range(3):
    for col in range(3):
      if board[row, col] == 0:
        possible_moves.append((row, col))

  # Evaluate each possible move
  scores = []
  for move in possible_moves:
    # Make the move
    board[move[0], move[1]] = player

    # Evaluate the move
    score = minimax(board, player, depth - 1)

    # Undo the move
    board[move[0], move[1]] = 0

    # Store the score
    scores.append(score)

  # Return the best score
  if player == 'X':
    return max(scores)
  else:
    return min(scores)

def get_opponent(player):
  """
  Gets the opponent of the given player.
  
  Args:
    player: The player to get the opponent of.
  
  Returns:
    The opponent of the given player.
  """

  if player == 'X':
    return 'O'
  else:
    return 'X'

if __name__ == "__main__":
  jdv()
