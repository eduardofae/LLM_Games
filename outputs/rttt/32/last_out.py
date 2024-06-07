# Import the necessary modules.
import numpy as np
import tkinter as tk

# Create the game board.
board = np.zeros((3, 3))

# Define the players' turns.
player1 = 1
player2 = 2

# Define the winning lines.
winning_lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

# Start the game loop.
while True:
    # Print the game board.
    print(board)

    # Get the player's move.
    move = int(input("Player {}'s turn: ".format(player1 if player1 == 1 else player2)))

    # Check if the move is valid.
    if move < 0 or move > 8 or board[move] != 0:
        print("Invalid move.")
        continue

    # Place the player's piece on the board.
    board[move] = player1 if player1 == 1 else player2

    # Check if the player has won.
    for line in winning_lines:
        if board[line[0]] == board[line[1]] == board[line[2]] != 0:
            print("Player {} wins!".format(player1 if player1 == 1 else player2))
            break

    # Check if the game is a draw.
    if np.all(board != 0):
        print("Draw!")
        break

    # Switch the player's turns.
    player1, player2 = player2, player1

# Reset the game board.
board = np.zeros((3, 3))

# Keep track of the number of moves made.
num_moves = 0

# Play against a computer opponent.
while True:
    # Print the game board.
    print(board)

    # Get the player's move.
    move = int(input("Player 1's turn: "))

    # Check if the move is valid.
    if move < 0 or move > 8 or board[move] != 0:
        print("Invalid move.")
        continue

    # Place the player's piece on the board.
    board[move] = player1

    # Increment the number of moves made.
    num_moves += 1

    # Check if the player has won.
    for line in winning_lines:
        if board[line[0]] == board[line[1]] == board[line[2]] != 0:
            print("Player 1 wins!")
            break

    # Check if the game is a draw.
    if np.all(board != 0):
        print("Draw!")
        break

    # Get the computer's move.
    move = np.random.randint(9)

    # Check if the move is valid.
    while board[move] != 0:
        move = np.random.randint(9)

    # Place the computer's piece on the board.
    board[move] = player2

    # Increment the number of moves made.
    num_moves += 1

    # Check if the computer has won.
    for line in winning_lines:
        if board[line[0]] == board[line[1]] == board[line[2]] != 0:
            print("Player 2 wins!")
            break

    # Check if the game is a draw.
    if np.all(board != 0):
        print("Draw!")
        break

# Save the game.
with open("jdv.txt", "w") as f:
    f.write(np.array2string(board))

# Load the game.
with open("jdv.txt", "r") as f:
    board = np.array(eval(f.read()))

# Create a graphical user interface (GUI).
class JdvGui(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Jdv")
        self.geometry("300x300")

        self.board = np.zeros((3, 3))

        self.canvas = tk.Canvas(self, width=300, height=300)
        self.canvas.pack()

        self.draw_board()

        self.canvas.bind("<Button-1>", self.on_click)

    def draw_board(self):
        for i in range(3):
            for j in range(3):
                if self.board[i, j] == 1:
                    self.canvas.create_oval(100 * i, 100 * j, 100 * i + 100, 100 * j + 100, fill="red")
                elif self.board[i, j] == 2:
                    self.canvas.create_oval(100 * i, 100 * j, 100 * i + 100, 100 * j + 100, fill="blue")

    def on_click(self, event):
        i = event.x // 100
        j = event.y // 100

        if self.board[i, j] == 0:
            self.board[i, j] = 1

            self.draw_board()

            # Check if the player has won.
            for line in winning_lines:
                if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != 0:
                    print("Player 1 wins!")
                    break

            # Check if the game is a draw.
            if np.all(self.board != 0):
                print("Draw!")
                break

            # Get the computer's move.
            move = np.random.randint(9)

            # Check if the move is valid.
            while self.board[move] != 0:
                move = np.random.randint(9)

            # Place the computer's piece on the board.
            self.board[move] = 2

            self.draw_board()

            # Check if the computer has won.
            for line in winning_lines:
                if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != 0:
                    print("Player 2 wins!")
                    break

            # Check if the game is a draw.
            if np.all(self.board != 0):
                print("Draw!")
                break

if __name__ == "__main__":
    jdv = JdvGui()
    jdv.mainloop()
