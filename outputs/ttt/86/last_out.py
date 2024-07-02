import numpy as np

# Create the game board
board = np.zeros((3, 3))

# Create a list of players
players = ['X', 'O']

# Create a variable to keep track of the current player
current_player = 0

# Create a variable to keep track of the game status
game_over = False

# Create a variable to keep track of the number of wins for each player
wins = {
  'X': 0,
  'O': 0
}

# Create a variable to keep track of the number of moves each player has made
moves = {
  'X': 0,
  'O': 0
}

# Create a function to check if a player has won
def check_win(board, player):
  # Check if the player has won horizontally
  for i in range(3):
    if np.all(board[i] == player):
      return True

  # Check if the player has won vertically
  for j in range(3):
    if np.all(board[:, j] == player):
      return True

  # Check if the player has won diagonally
  if np.all(board.diagonal() == player):
    return True
  if np.all(np.flip(board).diagonal() == player):
    return True

  # If the player has not won, return False
  return False

# Create a function to play the game
def play_game():
  # While the game is not over
  while not game_over:
    # Get the current player's move
    move = input("Player {}'s move: ".format(players[current_player]))

    # Convert the move to a row and column
    row, col = map(int, move.split(','))

    # If the move is valid
    if row >= 0 and row < 3 and col >= 0 and col < 3 and board[row, col] == 0:
      # Place the player's piece on the board
      board[row, col] = players[current_player]

      # Increment the number of moves for the player
      moves[players[current_player]] += 1

      # Check if the player has won
      if check_win(board, players[current_player]):
        # If the player has won, print the winning message
        print("Player {} wins!".format(players[current_player]))

        # Increment the number of wins for the player
        wins[players[current_player]] += 1

        # Set the game over variable to True
        game_over = True
    else:
      # If the move is not valid, print an error message
      print("Invalid move. Please try again.")

    # Switch to the other player
    current_player = (current_player + 1) % 2

  # If the game is a draw
  if not game_over:
    # Print the draw message
    print("Draw!")

# Create a function to reset the game
def reset_game():
  # Reset the game board
  board[:] = 0

  # Reset the current player
  current_player = 0

  # Reset the game over variable
  game_over = False

  # Reset the number of moves for each player
  moves['X'] = 0
  moves['O'] = 0

# Create a function to play against a computer opponent
def play_against_computer():
  # While the game is not over
  while not game_over:
    # Get the player's move
    move = input("Your move: ")

    # Convert the move to a row and column
    row, col = map(int, move.split(','))

    # If the move is valid
    if row >= 0 and row < 3 and col >= 0 and col < 3 and board[row, col] == 0:
      # Place the player's piece on the board
      board[row, col] = 'X'

      # Increment the number of moves for the player
      moves['X'] += 1

      # Check if the player has won
      if check_win(board, 'X'):
        # If the player has won, print the winning message
        print("You win!")

        # Increment the number of wins for the player
        wins['X'] += 1

        # Set the game over variable to True
        game_over = True
    else:
      # If the move is not valid, print an error message
      print("Invalid move. Please try again.")

    # If the game is not over, get the computer's move
    if not game_over:
      # Get a random move from the computer
      row, col = np.random.randint(0, 3, 2)

      # While the move is not valid
      while board[row, col] != 0:
        # Get a new random move from the computer
        row, col = np.random.randint(0, 3, 2)

      # Place the computer's piece on the board
      board[row, col] = 'O'

      # Increment the number of moves for the computer
      moves['O'] += 1

      # Check if the computer has won
      if check_win(board, 'O'):
        # If the computer has won, print the losing message
        print("You lose!")

        # Increment the number of wins for the computer
        wins['O'] += 1

        # Set the game over variable to True
        game_over = True

  # If the game is a draw
  if not game_over:
    # Print the draw message
    print("Draw!")

# Play the game
while True:
  # Ask the players if they want to play against a computer opponent
  play_against_computer = input("Do you want to play against a computer opponent? (y/n): ")

  # If the players want to play against a computer opponent
  if play_against_computer == 'y':
    # Play against a computer opponent
    play_against_computer()
  else:
    # Play the game
    play_game()

  # Ask the players if they want to play again
  play_again = input("Play again? (y/n): ")

  # If the players do not want to play again, exit the program
  if play_again != 'y':
    break

  # Reset the game
  reset_game()
