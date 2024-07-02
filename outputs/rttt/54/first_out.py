import numpy as np

def jdv():
  # Create the game board
  board = np.zeros((3, 3))

  # Get the player's names
  player1_name = input("Player 1 name: ")
  player2_name = input("Player 2 name: ")

  # Set the current player to player 1
  current_player = 1

  # Game loop
  while True:
    # Get the player's move
    if current_player == 1:
      move = input(f"{player1_name}, enter your move (row, column): ")
    else:
      move = input(f"{player2_name}, enter your move (row, column): ")

    # Check if the move is valid
    if not (0 <= move[0] < 3 and 0 <= move[1] < 3 and board[move[0], move[1]] == 0):
      print("Invalid move. Please try again.")
      continue

    # Place the player's piece on the board
    board[move[0], move[1]] = current_player

    # Check if the player has won
    if check_win(board, current_player):
      if current_player == 1:
        print(f"{player1_name} wins!")
      else:
        print(f"{player2_name} wins!")
      break

    # Check if the game is a draw
    if np.all(board != 0):
      print("Draw!")
      break

    # Switch the current player
    current_player = 3 - current_player

# Function to check if a player has won
def check_win(board, player):
  # Check for a win in each row
  for row in range(3):
    if np.all(board[row, :] == player):
      return True

  # Check for a win in each column
  for col in range(3):
    if np.all(board[:, col] == player):
      return True

  # Check for a win in each diagonal
  if np.all(board.diagonal() == player) or np.all(np.fliplr(board).diagonal() == player):
    return True

  # No win yet
  return False

# Play the game
jdv()
