import tkinter as tk
import numpy as np

class JdvGame:
  def __init__(self):
    # Set the game size
    self.grid_size = 3

    # Create the game grid
    self.grid = np.zeros((self.grid_size, self.grid_size), dtype=int)

    # Set the player number
    self.player = 1

    # Set the player scores
    self.player_scores = {1: 0, 2: 0}

    # Create the game window
    self.window = tk.Tk()
    self.window.title("Jdv Game")

    # Create the game canvas
    self.canvas = tk.Canvas(self.window, width=300, height=300)
    self.canvas.pack()

    # Create the game board
    for row in range(self.grid_size):
      for col in range(self.grid_size):
        # Create a square for each cell in the grid
        square = tk.Rectangle(self.canvas, width=100, height=100)
        square.place(x=row * 100, y=col * 100)

        # Bind a click event to each square
        square.bind("<Button-1>", self.on_click)

    # Create a menu bar
    self.menubar = tk.Menu(self.window)
    self.window.config(menu=self.menubar)

    # Create a game menu
    self.game_menu = tk.Menu(self.menubar, tearoff=0)
    self.menubar.add_cascade(label="Game", menu=self.game_menu)

    # Add a "New game" option to the game menu
    self.game_menu.add_command(label="New game", command=self.new_game)

    # Add a "Choose grid size" option to the game menu
    self.game_menu.add_command(label="Choose grid size", command=self.choose_grid_size)

    # Add a "Exit" option to the game menu
    self.game_menu.add_separator()
    self.game_menu.add_command(label="Exit", command=self.exit_game)

    # Start the game
    self.play_game()

  def play_game(self):
    # Get the player's move
    move = input("Player {}'s move: ".format(self.player))

    # Convert the move to a row and column
    try:
      row, col = [int(x) for x in move.split(",")]
    except ValueError:
      print("Invalid move. Please try again.")
      self.play_game()

    # Check if the move is valid
    if not (0 <= row < self.grid_size and 0 <= col < self.grid_size):
      print("Invalid move. Please try again.")
      self.play_game()
    if self.grid[row, col] != 0:
      print("Space is already occupied. Please try again.")
      self.play_game()

    # Place the player's piece on the grid
    self.grid[row, col] = self.player

    # Check if the player has won
    if self.check_win(self.grid, self.player):
      print("Player {} wins!".format(self.player))
      self.player_scores[self.player] += 1
      self.play_again()
    else:
      # Check if the game is a draw
      if np.all(self.grid != 0):
        print("Draw!")
        self.play_again()
      else:
        # Switch the player
        self.player = 3 - self.player
        self.play_game()

  def on_click(self, event):
    # Get the row and column of the clicked square
    row = int(event.y / 100)
    col = int(event.x / 100)

    # Check if the square is empty
    if self.grid[row, col] == 0:
      # Place the player's piece on the square
      self.grid[row, col] = self.player

      # Check if the player has won
      if self.check_win(self.grid, self.player):
        print("Player {} wins!".format(self.player))
        self.player_scores[self.player] += 1
        self.play_again()
      else:
        # Check if the game is a draw
        if np.all(self.grid != 0):
          print("Draw!")
          self.play_again()
        else:
          # Switch the player
          self.player = 3 - self.player

  def check_win(self, grid, player):
    """
    Check if the player has won the game.

    Args:
      grid: The game grid.
      player: The player number.

    Returns:
      True if the player has won, False otherwise.
    """

    # Check for a win in each row
    for row in range(grid.shape[0]):
      if np.all(grid[row, :] == player):
        return True

    # Check for a win in each column
    for col in range(grid.shape[1]):
      if np.all(grid[:, col] == player):
        return True

    # Check for a win in each diagonal
    if np.all(grid.diagonal() == player) or np.all(np.flip(grid).diagonal() == player):
      return True

    # No win
    return False

  def play_again(self):
    # Ask the players if they want to play again
    while True:
      play_again = input("Play again? (y/n) ")
      if play_again == "y":
        # Reset the grid and player number
        self.grid = np.zeros((self.grid_size, self.grid_size), dtype=int)
        self.player = 1
        # Play the game again
        self.play_game()
      elif play_again == "n":
        # Print the player scores and exit the game
        print("Player scores:")
        for player, score in self.player_scores.items():
          print("Player {}: {}".format(player, score))
        self.window.destroy()
        break
      else:
        print("Invalid input. Please enter 'y' or 'n'.")

  def new_game(self):
    # Reset the grid and player number
    self.grid = np.zeros((self.grid_size, self.grid_size), dtype=int)
    self.player = 1
    # Play the game again
    self.play_game()

  def choose_grid_size(self):
    # Get the new grid size from the user
    new_grid_size = input("Enter the new grid size: ")

    # Check if the new grid size is valid
    try:
      new_grid_size = int(new_grid_size)
    except ValueError:
      print("Invalid grid size. Please enter a valid integer.")
      return

    # Check if the new grid size is greater than 2
    if new_grid_size < 3:
      print("The grid size must be greater than 2.")
      return

    # Update the grid size
    self.grid_size = new_grid_size

    # Reset the grid and player number
    self.grid = np.zeros((self.grid_size, self.grid_size), dtype=int)
    self.player = 1

    # Play the game again
    self.play_game()

  def exit_game(self):
    # Exit the game
    self.window.destroy()

if __name__ == "__main__":
  jdv = JdvGame()
  jdv.window.mainloop()
