import tkinter as tk
import numpy as np
import random

class Connect4:
  def __init__(self):
    # Create the game board
    self.board = np.full((10, 10), ' ')

    # Initialize the game state
    self.player = 1
    self.winner = None

    # Create the GUI
    self.root = tk.Tk()
    self.root.title("Connect 4")

    # Create the game board canvas
    self.canvas = tk.Canvas(self.root, width=400, height=400)
    self.canvas.pack()

    # Create the game board squares
    self.squares = []
    for row in range(10):
      for col in range(10):
        square = tk.Button(self.canvas, width=4, height=2, command=lambda row=row, col=col: self.drop_piece(row, col))
        square.grid(row=row, column=col)
        self.squares.append(square)

    # Create the game status label
    self.status_label = tk.Label(self.root, text="Player 1's turn")
    self.status_label.pack()

    # Start the game loop
    self.main()

  def drop_piece(self, row, col):
    # Check if the column is full
    if self.board[0][col] != ' ':
      return

    # Drop the piece into the board
    for i in range(len(self.board)-1, -1, -1):
      if self.board[i][col] == ' ':
        self.board[i][col] = 'X' if self.player == 1 else 'O'
        break

    # Check for a winner
    self.winner = self.check_win()

    # Switch to the other player
    self.player = 2 if self.player == 1 else 1

    # Update the GUI
    self.update_gui()

  def check_win(self):
    # Check for horizontal wins
    for row in self.board:
      if len(set(row)) == 1 and row[0] != ' ':
        return row[0]

    # Check for vertical wins
    for col in range(len(self.board[0])):
      column = [row[col] for row in self.board]
      if len(set(column)) == 1 and column[0] != ' ':
        return column[0]

    # Check for diagonal wins
    diagonals = [[self.board[i][i] for i in range(len(self.board))],
                 [self.board[i][len(self.board)-i-1] for i in range(len(self.board))]]
    for diagonal in diagonals:
      if len(set(diagonal)) == 1 and diagonal[0] != ' ':
        return diagonal[0]

    return None

  def update_gui(self):
    # Update the game board squares
    for row in range(10):
      for col in range(10):
        if self.board[row][col] == 'X':
          self.squares[row*10 + col].configure(bg="red")
        elif self.board[row][col] == 'O':
          self.squares[row*10 + col].configure(bg="yellow")

    # Update the game status label
    if self.winner is None:
      self.status_label.configure(text=f"Player {self.player}'s turn")
    else:
      self.status_label.configure(text=f"Player {self.winner} wins!")

  def main(self):
    # Run the game loop
    self.root.mainloop()

if __name__ == "__main__":
  Connect4()
