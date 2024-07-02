import numpy as np

class Jdv:
  def __init__(self, grid_size=3, num_players=2):
    self.grid = np.zeros((grid_size, grid_size), dtype=int)
    self.player_turn = 1  # 1 or 2
    self.winner = None
    self.computer_player = False
    self.num_players = num_players

  def play(self, row, col):
    if self.winner is not None:
      return  # Game is over

    if self.grid[row, col] != 0:
      return  # Space is already occupied

    self.grid[row, col] = self.player_turn
    self.check_winner()
    self.player_turn = self.player_turn % self.num_players + 1

  def check_winner(self):
    # Check rows
    for row in range(self.grid.shape[0]):
      if np.all(self.grid[row, :] == self.player_turn):
        self.winner = self.player_turn
        return

    # Check columns
    for col in range(self.grid.shape[1]):
      if np.all(self.grid[:, col] == self.player_turn):
        self.winner = self.player_turn
        return

    # Check diagonals
    if np.all(self.grid.diagonal() == self.player_turn):
      self.winner = self.player_turn
      return
    if np.all(np.flip(self.grid).diagonal() == self.player_turn):
      self.winner = self.player_turn
      return

    # Check for draw
    if np.all(self.grid != 0):
      self.winner = 0  # Draw

  def get_grid(self):
    return self.grid

  def get_winner(self):
    return self.winner

  def computer_move(self):
    # Get all possible moves
    possible_moves = []
    for row in range(self.grid.shape[0]):
      for col in range(self.grid.shape[1]):
        if self.grid[row, col] == 0:
          possible_moves.append((row, col))

    # Choose a random move
    move = random.choice(possible_moves)

    # Make the move
    self.play(move[0], move[1])

if __name__ == "__main__":
  # Get the grid size
  grid_size = int(input("Enter the grid size: "))

  # Get the number of players
  num_players = int(input("Enter the number of players: "))

  # Create a new game
  jdv = Jdv(grid_size, num_players)

  # Get the level of difficulty
  difficulty = input("Choose a level: easy, medium, or hard: ")

  # Set the computer player to True if the difficulty is hard
  if difficulty == "hard":
    jdv.computer_player = True

  # Play the game
  while jdv.winner is None:
    # Get the player's move
    print(jdv.get_grid())
    row, col = map(int, input("Enter row and column: ").split())
    jdv.play(row, col)

    # Check if the player has won
    if jdv.winner is not None:
      break

    # If the computer player is True, make a move
    if jdv.computer_player:
      jdv.computer_move()

    # Check if the computer player has won
    if jdv.winner is not None:
      break

  # Print the winner
  if jdv.winner == 0:
    print("Draw")
  else:
    print("Player", jdv.winner, "wins")
