# Create the game board
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

# Create a function to check if a player has won
def check_win(board):
  for row in board:
    if row[0] == row[1] == row[2] and row[0] != " ":
      return True
  for col in range(3):
    if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
      return True
  if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
    return True
  if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
    return True
  return False

# Create a function to check if the game is a draw
def check_draw(board):
  for row in board:
    for space in row:
      if space == " ":
        return False
  return True

# Create a function to get the player's move
def get_move(player):
  while True:
    try:
      move = input(f"Player {player}, enter your move (row, column): ")
      row, col = [int(x) - 1 for x in move.split(",")]
      if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
        return row, col
      else:
        print("Invalid move. Please enter a valid move (row, column).")
    except ValueError:
      print("Invalid move. Please enter a valid move (row, column).")

# Create a function to place a piece on the board
def place_piece(board, player, row, col):
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
