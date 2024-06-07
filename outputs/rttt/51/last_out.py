import tkinter as tk

class GameLogic:
    def __init__(self, board_size=3):
        # Create the game board
        self.board = [[" " for _ in range(board_size)] for _ in range(board_size)]

        # Create a list of the players
        self.players = ["X", "O"]

        # Set the current player to the first player
        self.current_player = 0

    def make_move(self, row, col):
        # Check if the move is valid
        if self.board[row][col] == " ":
            # Place the current player's piece on the board
            self.board[row][col] = self.players[self.current_player]

            # Check if the current player has won
            if self.check_win(self.board, self.players[self.current_player]):
                return True
            else:
                # Check if there are no more free spaces
                if self.check_draw(self.board):
                    return True
                else:
                    # Switch to the other player
                    self.current_player = (self.current_player + 1) % 2
        else:
            # Invalid move
            return False

    def check_win_in_direction(self, board, player, direction):
        """
        Check if the given player has won the game in a specific direction.

        Args:
            board (list): The game board.
            player (str): The player to check.
            direction (str): The direction to check (row, column, or diagonal).

        Returns:
            bool: True if the player has won, False otherwise.
        """
        if direction == "row":
            for row in board:
                if all(cell == player for cell in row):
                    return True
        elif direction == "column":
            for col in range(len(board)):
                if all(board[row][col] == player for row in range(len(board))):
                    return True
        elif direction == "diagonal":
            if all(board[i][i] == player for i in range(len(board))):
                return True
            if all(board[i][len(board)-i-1] == player for i in range(len(board))):
                return True

        # No win in this direction
        return False

    def check_win(self, board, player):
        """
        Check if the given player has won the game.

        Args:
            board (list): The game board.
            player (str): The player to check.

        Returns:
            bool: True if the player has won, False otherwise.
        """

        # Check rows, columns, and diagonals
        return self.check_win_in_direction(board, player, "row") or \
               self.check_win_in_direction(board, player, "column") or \
               self.check_win_in_direction(board, player, "diagonal")

    def check_draw(self, board):
        """
        Check if the game is a draw.

        Args:
            board (list): The game board.

        Returns:
            bool: True if the game is a draw, False otherwise.
        """
        return all(cell != " " for cell in board[0] + board[1] + board[2])

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[" " for _ in range(size)] for _ in range(size)]

class GameUI:
    def __init__(self, game_logic):
        self.game_logic = game_logic

        # Create the game window
        self.window = tk.Tk()
        self.window.title("Jdv Game")

        # Create the game board UI
        self.board_frame = tk.Frame(self.window)
        self.board_frame.pack()

        self.buttons = []
        for row in range(self.game_logic.board.size):
            for col in range(self.game_logic.board.size):
                button = tk.Button(self.board_frame, text=" ", width=4, height=2)
                button.config(command=lambda row=row, col=col: self.make_move(row, col))
                button.grid(row=row, column=col)
                self.buttons.append(button)

        # Start the game
        self.window.mainloop()

    def make_move(self, row, col):
        # Make the move
        if self.game_logic.make_move(row, col):
            # Update the button text
            self.buttons[row * self.game_logic.board.size + col].config(text=self.game_logic.players[self.game_logic.current_player])

            # Check if the game is over
            if self.game_logic.check_win(self.game_logic.board, self.game_logic.players[self.game_logic.current_player]):
                print(f"{self.game_logic.players[self.game_logic.current_player]} wins!")
                self.window.destroy()
            elif self.game_logic.check_draw(self.game_logic.board):
                print("Draw!")
                self.window.destroy()

if __name__ == "__main__":
    players = [Player("Player 1", "X"), Player("Player 2", "O")]
    game_logic = GameLogic()
    game_ui = GameUI(game_logic)
