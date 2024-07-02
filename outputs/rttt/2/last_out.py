import numpy as np

class JdvGame:
    PLAYER1 = "X"
    PLAYER2 = "O"

    def __init__(self):
        self.grid = np.empty((3, 3), dtype=str)
        self.current_player = self.PLAYER1
        self.winner = None

    def play(self):
        while True:
            # Display the game board.
            print(self.grid)

            # Get the current player's move.
            print(f"\n{self.current_player}'s turn:")
            move = input("Enter a row and column (e.g. 1,2): ")

            # Validate the move.
            try:
                row, col = map(int, move.split(","))
                if not (0 <= row < 3 and 0 <= col < 3):
                    raise ValueError("Invalid row or column number.")
                if self.grid[row, col] != '':
                    raise ValueError("That space is already taken.")
            except ValueError as e:
                print(e)
                continue

            # Place the player's piece in the space.
            self.grid[row, col] = self.current_player

            # Check if the player has won.
            self.winner = self.check_win()

            # Check if the game is a draw.
            if self.grid.all() and self.winner is None:
                self.winner = "Draw"
                print("Draw!")
                break

            # Switch to the other player's turn.
            self.current_player = self.PLAYER2 if self.current_player == self.PLAYER1 else self.PLAYER1

        # Print the winner.
        if self.winner is not None:
            print(f"{self.winner} wins!")

    def check_win(self):
        # Check for a win in each row.
        for row in self.grid:
            if all(row == self.current_player):
                return self.current_player

        # Check for a win in each column.
        for col in self.grid.T:
            if all(col == self.current_player):
                return self.current_player

        # Check for a win in each diagonal.
        if all(self.grid.diagonal() == self.current_player) or all(np.flip(self.grid).diagonal() == self.current_player):
            return self.current_player

        # No win found.
        return None

    def reset(self):
        self.grid = np.empty((3, 3), dtype=str)
        self.current_player = self.PLAYER1
        self.winner = None

if __name__ == "__main__":
    game = JdvGame()

    while True:
        # Play the game.
        game.play()

        # Ask the players if they want to play again.
        play_again = input("Play again? (y/n): ")

        # Reset the game if the players want to play again.
        if play_again == "y":
            game.reset()
        # Quit the game if the players don't want to play again.
        else:
            break
