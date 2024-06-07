import numpy as np
import tkinter as tk

class JdvGame:
    def __init__(self, num_players, player_symbols, grid_size=3):
        self.grid = np.zeros((grid_size, grid_size), dtype=int)
        self.players = player_symbols
        self.num_players = num_players
        self.current_player = 0
        self.grid_size = grid_size

    def play_game(self):
        # Create the game window
        window = tk.Tk()
        window.title("Jdv Game")

        # Create the game grid
        self.canvas = tk.Canvas(window, width=300, height=300)
        self.canvas.pack()

        # Draw the grid lines
        for i in range(self.grid_size):
            self.canvas.create_line(0, i * 100, 300, i * 100, width=2)
            self.canvas.create_line(i * 100, 0, i * 100, 300, width=2)

        # Add click event handler to the grid
        self.canvas.bind("<Button-1>", self.on_click)

        # Start the game loop
        window.mainloop()

    def on_click(self, event):
        # Get the row and column of the clicked cell
        row = event.y // 100
        col = event.x // 100

        # Check if the cell is empty
        if self.grid[row, col] == 0:
            # Place the player's piece on the grid
            self.grid[row, col] = self.players[self.current_player]

            # Draw the player's piece on the canvas
            self.draw_piece(row, col, self.players[self.current_player])

            # Check if the player has won
            winner = self.check_winner(self.players[self.current_player])
            if winner is not None:
                # Display the winner
                self.display_winner(winner)
                return

            # Check if the game is a draw
            if np.all(self.grid != 0):
                # Display a draw message
                self.display_draw()
                return

            # Switch the current player
            self.current_player = (self.current_player + 1) % self.num_players

    def draw_piece(self, row, col, symbol):
        # Draw a circle at the center of the cell
        self.canvas.create_oval(col * 100 + 25, row * 100 + 25, col * 100 + 75, row * 100 + 75, fill=symbol)

    def check_winner(self, player):
        # Check rows
        for row in range(self.grid_size):
            if np.all(self.grid[row, :] == player):
                return player

        # Check columns
        for col in range(self.grid_size):
            if np.all(self.grid[:, col] == player):
                return player

        # Check diagonals
        if np.all(np.diag(self.grid) == player) or np.all(np.diag(np.flip(self.grid)) == player):
            return player

        return None

    def display_winner(self, winner):
        # Create a new window to display the winner
        winner_window = tk.Tk()
        winner_window.title("Winner")

        # Create a label to display the winner's name
        winner_label = tk.Label(winner_window, text=f"{winner} wins!")
        winner_label.pack()

        # Add a button to close the window
        close_button = tk.Button(winner_window, text="Close", command=winner_window.destroy)
        close_button.pack()

    def display_draw(self):
        # Create a new window to display the draw message
        draw_window = tk.Tk()
        draw_window.title("Draw")

        # Create a label to display the draw message
        draw_label = tk.Label(draw_window, text="Draw!")
        draw_label.pack()

        # Add a button to close the window
        close_button = tk.Button(draw_window, text="Close", command=draw_window.destroy)
        close_button.pack()


# Get the number of players
num_players = int(input("Enter the number of players (2-4): "))

# Check if the number of players is valid
if num_players not in range(2, 5):
    print("Invalid number of players. Please enter a number between 2 and 4.")
    exit()

# Get the player symbols
player_symbols = []
for i in range(num_players):
    symbol = input(f"Player {i + 1}, choose your symbol: ")
    player_symbols.append(symbol)

# Create a new game instance
game = JdvGame(num_players, player_symbols)

# Start the game
game.play_game()
