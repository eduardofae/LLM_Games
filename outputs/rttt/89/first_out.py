# Initialize the game board
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

# Initialize the players
player1 = 'X'
player2 = 'O'

# Function to print the game board
def print_board():
  for row in board:
    print(' '.join(row))

# Function to check if a player has won
def check_winner(player):
  # Check for horizontal wins
  for row in board:
    if row[0] == row[1] == row[2] == player:
      return True

  # Check for vertical wins
  for col in range(3):
    if board[0][col] == board[1][col] == board[2][col] == player:
      return True

  # Check for diagonal wins
  if board[0][0] == board[1][1] == board[2][2] == player:
    return True
  if board[0][2] == board[1][1] == board[2][0] == player:
    return True

  # No winner yet
  return False

# Function to get the player's move
def get_move(player):
  while True:
    try:
      row, col = map(int, input(f"Player {player}, enter your move (row, col): ").split())
      if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
        return row, col
      else:
        print("Invalid move. Please try again.")
    except ValueError:
      print("Invalid input. Please enter two integers.")

# Main game loop
while True:
  # Print the game board
  print_board()

  # Get player 1's move
  row, col = get_move(player1)
  board[row][col] = player1

  # Check if player 1 has won
  if check_winner(player1):
    print("Player 1 wins!")
    break

  # Check if there are no more free spaces
  if all(all(cell != ' ' for cell in row) for row in board):
    print("Draw!")
    break

  # Get player 2's move
  row, col = get_move(player2)
  board[row][col] = player2

  # Check if player 2 has won
  if check_winner(player2):
    print("Player 2 wins!")
    break
