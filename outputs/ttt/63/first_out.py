# Create the game board
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

# Create a function to check if a player has won
def check_win(board):
  # Check for horizontal wins
  for row in board:
    if row[0] == row[1] == row[2] and row[0] != " ":
      return True

  # Check for vertical wins
  for col in range(3):
    if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
      return True

  # Check for diagonal wins
  if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
    return True
  if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
    return True

  # Return False if no player has won
  return False

# Create a function to check if the game is a draw
def check_draw(board):
  # Check if there are any empty spaces left on the board
  for row in board:
    for space in row:
      if space == " ":
        return False

  # Return True if the game is a draw
  return True

# Create a function to get the player's move
def get_move(player):
  # Get the player's input
  move = input(f"Player {player}, enter your move (row, column): ")

  # Validate the player's input
  while not move.isdigit() or int(move) < 1 or int(move) > 3:
    move = input("Invalid move. Please enter a valid move (row, column): ")

  # Convert the player's input to a row and column
  row = int(move.split(",")[0]) - 1
  col = int(move.split(",")[1]) - 1

  # Return the player's move
  return row, col

# Create a function to place a piece on the board
def place_piece(board, player, row, col):
  # Place the player's piece on the board
  board[row][col] = player

# Create a function to play the game
def play_game():
  # Set the current player to 1
  current_player = 1

  # While the game is not over
  while not check_win(board) and not check_draw(board):
    # Get the player's move
    row, col = get_move(current_player)

    # Place the player's piece on the board
    place_piece(board, current_player, row, col)

    # Switch the current player
    current_player = 3 - current_player

  # Check if the game is a win or a draw
  if check_win(board):
    print(f"Player {current_player} wins!")
  elif check_draw(board):
    print("Draw!")

# Play the game
play_game()
