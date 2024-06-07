import os

def jdv():
  """
  A simple game of JDV.

  The game is played on a 3x3 grid. Two players take turns placing their pieces
  in a free space of the grid. The first player to get three of their pieces in
  a row, either horizontally, vertically, or diagonally, wins the game. If there
  are no more free spaces, the game is declared a draw.
  """

  # Create a 3x3 grid.
  grid = [[' ', ' ', ' '],
          [' ', ' ', ' '],
          [' ', ' ', ' ']]

  # Get the names of the two players.
  player1 = input("Player 1, what is your name? ")
  player2 = input("Player 2, what is your name? ")

  # Set the current player to player 1.
  current_player = player1

  # Set the score of the two players to 0.
  score1 = 0
  score2 = 0

  # Set the size of the grid.
  grid_size = 3

  # Set the player pieces.
  player1_piece = 'X'
  player2_piece = 'O'

  # Set the number of moves made by each player.
  moves1 = 0
  moves2 = 0

  # Set the difficulty of the game.
  difficulty = 'easy'

  # Set the number of wins and losses for each player.
  wins1 = 0
  losses1 = 0
  wins2 = 0
  losses2 = 0

  # Set the number of draws.
  draws = 0

  # Play the game until there is a winner or a draw.
  while True:
    # Get the player's move.
    row, col = map(int, input("{}, what is your move? (row, column) ".format(current_player)).split())

    # Check if the move is valid.
    if not (0 <= row < grid_size and 0 <= col < grid_size and grid[row][col] == ' '):
      print("Invalid move. Please try again.")
      continue

    # Place the player's piece on the grid.
    grid[row][col] = player1_piece if current_player == player1 else player2_piece

    # Increment the number of moves made by the current player.
    if current_player == player1:
      moves1 += 1
    else:
      moves2 += 1

    # Check if the player has won.
    if check_win(grid):
      print("{} wins!".format(current_player))
      if current_player == player1:
        score1 += 1
        wins1 += 1
        losses2 += 1
      else:
        score2 += 1
        wins2 += 1
        losses1 += 1
      break

    # Check if there are no more free spaces.
    if all(all(cell != ' ' for cell in row) for row in grid):
      print("Draw!")
      draws += 1
      break

    # Switch the current player.
    current_player = player2 if current_player == player1 else player1

  # Print the scores of the two players.
  print("Player 1: {}".format(score1))
  print("Player 2: {}".format(score2))

  # Print the number of moves made by each player.
  print("Player 1 moves: {}".format(moves1))
  print("Player 2 moves: {}".format(moves2))

  # Print the number of wins and losses for each player.
  print("Player 1 wins: {}".format(wins1))
  print("Player 1 losses: {}".format(losses1))
  print("Player 2 wins: {}".format(wins2))
  print("Player 2 losses: {}".format(losses2))

  # Print the number of draws.
  print("Draws: {}".format(draws))

  # Ask the players if they want to play again.
  play_again = input("Do you want to play again? (y/n) ")
  if play_again == 'y':
    os.system('cls')
    jdv()
  else:
    print("Thanks for playing!")


def check_win(grid):
  """
  Check if there is a winner in the given grid.

  Args:
    grid: A 3x3 grid.

  Returns:
    True if there is a winner, False otherwise.
  """

  # Check for horizontal wins.
  for row in grid:
    if all(cell == row[0] for cell in row) and row[0] != ' ':
      return True

  # Check for vertical wins.
  for col in range(3):
    if all(grid[row][col] == grid[0][col] for row in range(3)) and grid[0][col] != ' ':
      return True

  # Check for diagonal wins.
  if all(grid[row][row] == grid[0][0] for row in range(3)) and grid[0][0] != ' ':
    return True

  if all(grid[row][2 - row] == grid[0][2] for row in range(3)) and grid[0][2] != ' ':
    return True

  # No winner yet.
  return False


if __name__ == "__main__":
  jdv()
