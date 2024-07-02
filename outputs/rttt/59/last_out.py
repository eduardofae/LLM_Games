import numpy as np
import tkinter as tk

class Jdv:
    def __init__(self):
        self.grid = np.zeros((3, 3), dtype=int)
        self.turn = 1
        self.player1 = input("Player 1, what is your name? ")
        self.player2 = input("Player 2, what is your name? ")
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=300, height=300)
        self.canvas.pack()
        self.draw_grid()
        self.canvas.bind("<Button-1>", self.handle_click)
        self.root.mainloop()

    def draw_grid(self):
        for i in range(3):
            for j in range(3):
                x1 = i * 100
                y1 = j * 100
                x2 = x1 + 100
                y2 = y1 + 100
                self.canvas.create_rectangle(x1, y1, x2, y2)
                if self.grid[i, j] == 1:
                    self.canvas.create_line(x1, y1, x2, y2, width=5)
                    self.canvas.create_line(x2, y1, x1, y2, width=5)
                elif self.grid[i, j] == 2:
                    self.canvas.create_oval(x1, y1, x2, y2, width=5)

    def handle_click(self, event):
        x = event.x // 100
        y = event.y // 100
        if self.grid[x, y] == 0:
            self.grid[x, y] = self.turn
            self.draw_grid()
            if self.check_win(self.grid, self.turn):
                if self.turn == 1:
                    print(f"{self.player1} wins!")
                else:
                    print(f"{self.player2} wins!")
                self.root.destroy()
            elif np.all(self.grid != 0):
                print("The game is a draw.")
                self.root.destroy()
            else:
                self.turn = 3 - self.turn

    def check_win(self, grid, turn):
        """
        Checks if the player with the given turn has won the game.

        Args:
            grid: The game grid.
            turn: The player's turn.

        Returns:
            True if the player has won, False otherwise.
        """

        # Check for a win in each row.
        for row in range(3):
            if np.all(grid[row, :] == turn):
                return True

        # Check for a win in each column.
        for column in range(3):
            if np.all(grid[:, column] == turn):
                return True

        # Check for a win in each diagonal.
        if np.all(grid.diagonal() == turn) or np.all(np.flip(grid).diagonal() == turn):
            return True

        # No win found.
        return False


if __name__ == "__main__":
    Jdv()
