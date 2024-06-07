import numpy as np

def jdv():
  """
  A simple 2-player game where players take turns placing their pieces in a free space of a 3x3 grid.
  The first player to make a line of 3 adjacent pieces loses.
  If there are no more free spaces, the game is declared a draw.
  """

  # Create a 3x3 grid
  grid = np.zeros((3, 3), dtype=int)

  # Create a list of the possible winning combinations
  winning_combinations = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)],
  ]

  # Get the names of the two players
  player1_name = input("Player 1, what is your name? ")
  player2_name = input("Player 2, what is your name? ")

  # Determine who goes first
  player1_turn = True

  # Main game loop
  while True:
    # Get the current player's move
    if player1_turn:
      row, col = map(int, input(f"{player1_name}, enter your move (row, column): ").split())
    else:
      row, col = map(int, input(f"{player2_name}, enter your move (row, column): ").split())

    # Check if the move is valid
    if row < 0 or row > 2 or col < 0 or col > 2 or grid[row, col] != 0:
      print("Invalid move.")
      continue

    # Place the player's piece on the grid
    grid[row, col] = 1 if player1_turn else 2

    # Check if the player has won
    for combination in winning_combinations:
      if all(grid[r, c] == grid[combination[0][0], combination[0][1]] for r, c in combination):
        if player1_turn:
          print(f"{player1_name} wins!")
        else:
          print(f"{player2_name} wins!")
        return

    # Check if the game is a draw
    if np.all(grid != 0):
      print("Draw!")
      return

    # Switch turns
    player1_turn = not player1_turn

if __name__ == "__main__":
  jdv()
