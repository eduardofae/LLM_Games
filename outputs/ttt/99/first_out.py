
def play_jdv():
  # Initialize the game board
  board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

  # Get the names of the two players
  player1_name = input("Player 1, enter your name: ")
  player2_name = input("Player 2, enter your name: ")

  # Determine who will play first
  player1_turn = True

  # Loop until the game is over
  while True:
    # Get the current player's name
    if player1_turn:
      player_name = player1_name
    else:
      player_name = player2_name

    # Get the player's move
    move = input(f"{player_name}, enter your move (row, column): ")

    # Convert the player's move to a row and column
    row, column = map(int, move.split(","))

    # Check if the move is valid
    if not (0 <= row <= 2 and 0 <= column <= 2 and board[row][column] == ' '):
      print("Invalid move. Please try again.")
      continue

    # Place the player's piece on the board
    if player1_turn:
      board[row][column] = 'X'
    else:
      board[row][column] = 'O'

    # Check if the player has won
    if check_for_win(board):
      print(f"{player_name} wins!")
      break

    # Check if the game is a draw
    if check_for_draw(board):
      print("The game is a draw.")
      break

    # Switch turns
    player1_turn = not player1_turn


def check_for_win(board):
  # Check for a horizontal win
  for row in range(3):
    if board[row][0] == board[row][1] == board[row][2] and board[row][0] != ' ':
      return True

  # Check for a vertical win
  for column in range(3):
    if board[0][column] == board[1][column] == board[2][column] and board[0][column] != ' ':
      return True

  # Check for a diagonal win
  if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
    return True
  if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
    return True

  # No win yet
  return False


def check_for_draw(board):
  # Check if there are any empty spaces on the board
  for row in range(3):
    for column in range(3):
      if board[row][column] == ' ':
        return False

  # No empty spaces, so the game is a draw
  return True


if __name__ == "__main__":
  play_jdv()
