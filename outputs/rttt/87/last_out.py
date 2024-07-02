import numpy as np

# Create the game board
board = np.zeros((3, 3))

# Create a dictionary to map player numbers to their symbols
players = {1: 'X', 2: 'O'}

# Create a variable to keep track of the current player
current_player = 1

# Create a variable to keep track of the game status
game_status = 'in progress'

# Create a variable to keep track of the players' scores
player_scores = {1: 0, 2: 0}

# Create a variable to keep track of the players' moves
player_moves = {1: [], 2: []}

# Create a function to print the game board
def print_board():
  for row in board:
    print(' '.join(row))

# Create a function to check if a player has won
def check_win(player):
  # Check if the player has won horizontally
  for row in board:
    if np.all(row == player):
      return True

  # Check if the player has won vertically
  for col in range(3):
    if np.all(board[:, col] == player):
      return True

  # Check if the player has won diagonally
  if np.all(np.diag(board) == player) or np.all(np.diag(np.flip(board)) == player):
    return True

  # If the player has not won, return False
  return False

# Create a function to get the player's move
def get_move(player):
  # Get the player's input
  move = input(f"Player {player}, enter your move (row, column): ")

  # Convert the player's input to a tuple
  move = tuple(int(x) for x in move.split(','))

  # Check if the player's move is valid
  if move[0] < 0 or move[0] > 2 or move[1] < 0 or move[1] > 2 or board[move] != 0:
    print("Invalid move")
    return get_move(player)

  # Return the player's move
  return move

# Create a function to play the game
def play_game():
  # Loop until the game is over
  while game_status == 'in progress':
    # Get the current player's move
    move = get_move(current_player)

    # Place the current player's piece on the game board
    board[move] = current_player

    # Add the current player's move to the list of moves
    player_moves[current_player].append(move)

    # Print the game board
    print_board()

    # Check if the current player has won
    if check_win(current_player):
      # If the current player has won, end the game
      game_status = 'over'
      print(f"Player {current_player} wins!")
      player_scores[current_player] += 1
    else:
      # If the current player has not won, switch to the next player
      current_player = 3 - current_player

  # Check if the game is a draw
  if np.all(board != 0) and not check_win(current_player):
    # If the game is a draw, end the game
    game_status = 'over'
    print("Draw!")

# Customizing the game board size
board_size = input("Enter the size of the game board (n x n): ")
board = np.zeros((int(board_size), int(board_size)))

# Get the players' names
player1_name = input("Enter player 1's name: ")
player2_name = input("Enter player 2's name: ")

# Play the game
play_game()

# Print the players' scores
print("Player 1's score:", player_scores[1])
print("Player 2's score:", player_scores[2])

# Print the players' moves
print("Player 1's moves:", player_moves[1])
print("Player 2's moves:", player_moves[2])

# Ask the players if they want to play again
play_again = input("Do you want to play again? (y/n) ")

# If the players want to play again, reset the game board and start a new game
if play_again == 'y':
  board = np.zeros((3, 3))
  current_player = 1
  game_status = 'in progress'
  player_moves = {1: [], 2: []}
  play_game()
