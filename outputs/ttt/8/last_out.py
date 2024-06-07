import numpy as np
import tkinter as tk

class JdvGame:
  def __init__(self):
    # Create a 3x3 grid
    self.grid = np.zeros((3, 3))

    # Set the current player to 1 (the first player)
    self.current_player = 1

    # Keep track of the number of moves made
    self.num_moves = 0

    # Create the main window
    self.window = tk.Tk()
    self.window.title("Jdv")

    # Create the game board
    self.canvas = tk.Canvas(self.window, width=300, height=300)
    self.canvas.pack()

    # Create the buttons for each cell in the grid
    self.buttons = []
    for row in range(3):
      for col in range(3):
        button = tk.Button(self.canvas, text="", command=lambda row=row, col=col: self.make_move(row, col))
        button.grid(row=row, column=col, padx=1, pady=1)
        self.buttons.append(button)

    # Create a button to reset the game
    self.reset_button = tk.Button(self.window, text="Reset", command=self.reset_game)
    self.reset_button.pack()

    # Create a button to change the difficulty
    self.difficulty_button = tk.Button(self.window, text="Change Difficulty", command=self.change_difficulty)
    self.difficulty_button.pack()

    # Create a button to change the game mode
    self.game_mode_button = tk.Button(self.window, text="Change Game Mode", command=self.change_game_mode)
    self.game_mode_button.pack()

    # Start the game
    self.play()

  def play(self):
    # Keep track of the game loop
    while True:
      # Get the player's move
      move = self.get_move()

      # Check if the move is valid
      if self.grid[move[0], move[1]] != 0:
        print("Invalid move. Please try again.")
        continue

      # Place the player's piece in the grid
      self.grid[move[0], move[1]] = self.current_player

      # Increment the number of moves made
      self.num_moves += 1

      # Check if the player has won
      if self.check_for_win(self.current_player):
        self.show_winner(self.current_player)
        break

      # Check if there are no more free spaces
      if self.num_moves == 9:
        self.show_draw()
        break

      # Switch to the other player
      self.current_player = 2 if self.current_player == 1 else 1

  def get_move(self):
    # Get the player's move from the GUI
    move = None
    while move is None:
      for event in self.window.winfo_children():
        if isinstance(event, tk.Button) and event["state"] == tk.DISABLED:
          continue

        if event.winfo_class() == "Button" and event["command"]:
          move = event.grid_info()["row"], event.grid_info()["column"]
          event["state"] = tk.DISABLED
          event["text"] = "X" if self.current_player == 1 else "O"
          break

    return move

  def check_for_win(self, player):
    """
    Checks if the given player has won the game.

    Args:
      player: The player to check for a win.

    Returns:
      True if the player has won, False otherwise.
    """

    # Check for a win in each row
    for row in range(3):
      if self.grid[row, 0] == self.grid[row, 1] == self.grid[row, 2] == player:
        return True

    # Check for a win in each column
    for col in range(3):
      if self.grid[0, col] == self.grid[1, col] == self.grid[2, col] == player:
        return True

    # Check for a win in each diagonal
    if self.grid[0, 0] == self.grid[1, 1] == self.grid[2, 2] == player:
      return True

    if self.grid[0, 2] == self.grid[1, 1] == self.grid[2, 0] == player:
      return True

    # No win found
    return False

  def show_winner(self, player):
    # Show a message to the player who won
    tk.messagebox.showinfo("Winner", f"Player {player} wins!")

  def show_draw(self):
    # Show a message to the players that the game is a draw
    tk.messagebox.showinfo("Draw", "The game is a draw!")

  def reset_game(self):
    # Reset the game board
    self.grid = np.zeros((3, 3))

    # Reset the current player
    self.current_player = 1

    # Reset the number of moves made
    self.num_moves = 0

    # Reset the buttons
    for button in self.buttons:
      button["state"] = tk.NORMAL
      button["text"] = ""

  def change_difficulty(self):
    # Get the new difficulty from the user
    difficulty = tk.askinteger("Difficulty", "Enter the difficulty level (1-3):")

    # Check if the difficulty is valid
    if difficulty not in range(1, 4):
      tk.messagebox.showerror("Error", "Invalid difficulty level.")
      return

    # Set the new difficulty
    self.difficulty = difficulty

  def change_game_mode(self):
    # Get the new game mode from the user
    game_mode = tk.askstring("Game Mode", "Enter the game mode (PvP or PvC):")

    # Check if the game mode is valid
    if game_mode not in ["PvP", "PvC"]:
      tk.messagebox.showerror("Error", "Invalid game mode.")
      return

    # Set the new game mode
    self.game_mode = game_mode

if __name__ == "__main__":
  game = JdvGame()
  game.window.mainloop()
