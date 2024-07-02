import numpy as np

def jdv():
  # Create the game board
  game_board = np.zeros((3, 3))

  # Get the player's names
  player1_name = input("Player 1 name: ")
  player2_name = input("Player 2 name: ")

  # Set the current player to player 1
  current_player = 1

  # Game loop
  while True:
    # Get the player's move
    if current_player == 1:
      move = get_move(player1_name, game_board)
    else:
      move = get_move(player2_name, game_board)

    # Check if the move is valid
    if not is_valid_move(move, game_board):
      print("Invalid move. Please try again.")
      continue

    # Place the player's piece on the board
    game_board[move[0], move[1]] = current_player

    # Check if the player has won
    if is_winner(game_board, current_player):
      if current_player == 1:
        print(f"{player1_name} wins!")
      else:
        print(f"{player2_name} wins!")
      break

    # Check if the game is a draw
    if np.all(game_board != 0):
      print("Draw!")
      break

    # Switch the current player
    current_player = 3 - current_player

# Function to get the player's move
def get_move(player_name, game_board):
  while True:
    try:
      move = input(f"{player_name}, enter your move (row, column): ")
      move = [int(x) for x in move.split(",")]
      if not is_valid_move(move, game_board):
        raise ValueError
      return move
    except ValueError:
      print("Invalid move. Please try again.")

# Function to check if a move is valid
def is_valid_move(move, game_board):
  return 0 <= move[0] < 3 and 0 <= move[1] < 3 and game_board[move[0], move[1]] == 0

# Function to check if a player has won
def is_winner(game_board, player):
  # Check for a win in each row
  for row in range(3):
    if np.all(game_board[row, :] == player):
      return True

  # Check for a win in each column
  for col in range(3):
    if np.all(game_board[:, col] == player):
      return True

  # Check for a win in each diagonal
  if np.all(game_board.diagonal() == player) or np.all(np.fliplr(game_board).diagonal() == player):
    return True

  # No win yet
  return False

# Play the game
if __name__ == "__main__":
  jdv()
