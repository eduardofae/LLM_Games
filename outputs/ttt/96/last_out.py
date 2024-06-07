import numpy as np
import tkinter as tk

class Jdv:
    def __init__(self, board_size=3):
        self.grid = np.zeros((board_size, board_size))
        self.player1 = 'X'
        self.player2 = 'O'
        self.current_player = self.player1
        self.game_over = False
        self.winner = None

        self.window = tk.Tk()
        self.window.title("JdV")
        self.window.geometry(f"{board_size * 100}x{board_size * 100}")

        self.canvas = tk.Canvas(self.window, width=board_size * 100, height=board_size * 100)
        self.canvas.pack()

        self.canvas.bind("<Button-1>", self.on_click)

        self.draw_board()

    def on_click(self, event):
        if self.game_over:
            return

        x = event.x // 100
        y = event.y // 100

        if self.grid[x, y] == 0:
            self.grid[x, y] = self.current_player

            self.draw_board()

            self.check_win()

            if self.game_over:
                self.declare_winner()
            else:
                self.switch_player()

    def draw_board(self):
        self.canvas.delete("all")

        for i in range(self.grid.shape[0]):
            for j in range(self.grid.shape[1]):
                if self.grid[i, j] == 0:
                    self.canvas.create_rectangle(i * 100, j * 100, (i + 1) * 100, (j + 1) * 100, fill="white")
                elif self.grid[i, j] == self.player1:
                    self.canvas.create_oval(i * 100, j * 100, (i + 1) * 100, (j + 1) * 100, fill="red")
                else:
                    self.canvas.create_oval(i * 100, j * 100, (i + 1) * 100, (j + 1) * 100, fill="blue")

    def check_win(self):
        # Check for a horizontal win
        for row in self.grid:
            if np.all(row == self.current_player):
                self.game_over = True
                self.winner = self.current_player
                return

        # Check for a vertical win
        for col in self.grid.T:
            if np.all(col == self.current_player):
                self.game_over = True
                self.winner = self.current_player
                return

        # Check for a diagonal win
        if np.all(self.grid.diagonal() == self.current_player):
            self.game_over = True
            self.winner = self.current_player
            return

        if np.all(np.flip(self.grid).diagonal() == self.current_player):
            self.game_over = True
            self.winner = self.current_player
            return

    def declare_winner(self):
        self.canvas.delete("all")
        self.canvas.create_text(150, 150, text=f"{self.winner} wins!", font=("Arial", 30))

    def switch_player(self):
        if self.current_player == self.player1:
            self.current_player = self.player2
        else:
            self.current_player = self.player1

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    jdv = Jdv()
    jdv.run()
