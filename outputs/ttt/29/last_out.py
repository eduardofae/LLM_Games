import numpy as np
import tkinter as tk

class JdvGame:
  def __init__(self):
    # Create the game board
    self.board = np.zeros((3, 3))

    # Create a list of the players
    self.players = ['X', 'O']

    # Set the current player to the first player
    self.current_player = self.players[0]

    # Create the Tkinter window
    self.window = tk.Tk()
    self.window.title("Jdv")

    # Create the game board
    self.canvas = tk.Canvas(self.window, width=300, height=300)
    self.canvas.pack()

    # Create the buttons
    self.buttons = []
    for row in range(3):
      for col in range(3):
        button = tk.Button(self.canvas, text="", command=lambda row=row, col=col: self.button_click(row, col))
        button.grid(row=row, column=col, sticky="nsew")
        self.buttons.append(button)

    # Create the menu bar
    self.menubar = tk.Menu(self.window)
    self.window.config(menu=self.menubar)

    # Create the game menu
    self.game_menu = tk.Menu(self.menubar)
    self.menubar.add_cascade(label="Game", menu=self.game_menu)

    # Add the new game option to the game menu
    self.new_game_option = tk.Menu(self.game_menu)
    self.new_game_option.add_command(label="New Game", command=self.new_game)
    self.game_menu.add_cascade(label="New", menu=self.new_game_option)

    # Add the quit option to the game menu
    self.quit_option = tk.Menu(self.game_menu)
    self.quit_option.add_command(label="Quit", command=self.quit_game)
    self.game_menu.add_cascade(label="Quit", menu=self.quit_option)

    # Start the game
    self.play_game()

  def button_click(self, row, col):
    # Check if the move is valid
    if self.board[row, col] != 0:
      print("Invalid move. Please choose a free space.")
      return

    # Place the player's piece on the board
    self.board[row, col] = self.current_player

    # Check if the player has won
    if self.check_win(self.board, self.current_player):
      print(f"Player {self.current_player} wins!")
      self.window.destroy()
      return

    # Check if the game is a draw
    if np.all(self.board != 0):
      print("It's a draw!")
      self.window.destroy()
      return

    # Switch to the other player
    self.current_player = self.players[(self.players.index(self.current_player) + 1) % 2]

    # Update the game board
    self.update_board()

  def check_win(self, board, player):
    """
    This function checks if the player has won the game.

    Args:
      board: The game board
      player: The player to check

    Returns:
      True if the player has won, False otherwise
    """

    # Check if the player has won horizontally
    for row in range(3):
      if np.all(board[row, :] == player):
        return True

    # Check if the player has won vertically
    for col in range(3):
      if np.all(board[:, col] == player):
        return True

    # Check if the player has won diagonally
    if np.all(board.diagonal() == player):
      return True
    if np.all(np.flip(board).diagonal() == player):
      return True

    # The player has not won
    return False

  def update_board(self):
    for row in range(3):
      for col in range(3):
        if self.board[row, col] == 'X':
          self.buttons[row * 3 + col]["text"] = "X"
        elif self.board[row, col] == 'O':
          self.buttons[row * 3 + col]["text"] = "O"

  def new_game(self):
    # Reset the game board
    self.board = np.zeros((3, 3))

    # Reset the current player
    self.current_player = self.players[0]

    # Update the game board
    self.update_board()

  def quit_game(self):
    # Quit the game
    self.window.destroy()

  def play_game(self):
    self.window.mainloop()

if __name__ == "__main__":
  JdvGame()
