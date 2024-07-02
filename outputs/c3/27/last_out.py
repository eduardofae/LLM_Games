import numpy as np

class Board:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [['.' for _ in range(self.cols)] for _ in range(self.rows)]

    def print_board(self):
        for row in self.grid:
            print(' '.join(row))

    def is_valid_move(self, col):
        return col >= 0 and col < self.cols and self.grid[0][col] == '.'

    def place_piece(self, player, col):
        for i in range(self.rows-1, -1, -1):
            if self.grid[i][col] == '.':
                self.grid[i][col] = player
                break

    def check_winner(self):
        # Check for horizontal wins
        for row in self.grid:
            if len(set(row)) == 1 and row[0] != '.':
                return row[0]

        # Check for vertical wins
        for col in range(self.cols):
            column = [row[col] for row in self.grid]
            if len(set(column)) == 1 and column[0] != '.':
                return column[0]

        # Check for diagonal wins
        diagonals = [[self.grid[i][i] for i in range(self.rows)],
                     [self.grid[i][self.cols-i-1] for i in range(self.rows)]]
        for diagonal in diagonals:
            if len(set(diagonal)) == 1 and diagonal[0] != '.':
                return diagonal[0]

        # Check for draw
        if '.' not in np.array(self.grid).flatten():
            return 'Draw'

        # No winner yet
        return None


class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def get_move(self, board):
        while True:
            col = int(input("{}'s turn: Enter a column (1-10): ".format(self.name))) - 1
            if board.is_valid_move(col):
                return col
            else:
                print("Invalid move. Try again.")


class AI:
    def __init__(self, color):
        self.color = color

    def get_move(self, board):
        # Implement minimax algorithm or other AI technique to determine the best move

# Play against AI
if __name__ == "__main__":
    game = Game(10, 10)
    game.players = [Player(input("Enter your name: "), 'X'), AI('O')]  # Replace the second player with an AI opponent
    game.play()

# AI vs AI mode
if __name__ == "__main__":
    game = Game(10, 10)
    game.players = [AI('X'), AI('O')]  # Replace both players with AI opponents
    game.play()

# Add difficulty levels
if __name__ == "__main__":
    difficulty = int(input("Enter difficulty level (1-3): "))
    game = Game(10, 10)
    if difficulty == 1:
        game.players = [Player(input("Enter your name: "), 'X'), AI('O')]
    elif difficulty == 2:
        game.players = [Player(input("Enter your name: "), 'X'), AI('O', depth=4)]
    elif difficulty == 3:
        game.players = [Player(input("Enter your name: "), 'X'), AI('O', depth=6)]
    game.play()

# Enhance user experience
if __name__ == "__main__":
    game = Game(10, 10)
    game.players = [Player(input("Enter player 1's name: "), 'X'), Player(input("Enter player 2's name: "), 'O')]
    game.play(visual=True)  # Add a visual representation of the board
