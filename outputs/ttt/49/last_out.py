import numpy as np

class Jdv:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.currentPlayer = 1

    def play(self, x, y):
        if self.is_valid_move(x, y):
            self.board[x, y] = self.currentPlayer
            self.currentPlayer *= -1

    def is_valid_move(self, x, y):
        return (x >= 0 and x < 3 and
                y >= 0 and y < 3 and
                self.board[x, y] == 0)

    def check_winner(self):
        for i in range(3):
            if np.all(self.board[i, :] == self.board[i, 0]) and self.board[i, 0] != 0:
                return self.board[i, 0]
            if np.all(self.board[:, i] == self.board[0, i]) and self.board[0, i] != 0:
                return self.board[0, i]

        if np.all(self.board.diagonal() == self.board[0, 0]) and self.board[0, 0] != 0:
            return self.board[0, 0]

        if np.all(np.flip(self.board).diagonal() == self.board[0, 2]) and self.board[0, 2] != 0:
            return self.board[0, 2]

        if np.all(self.board != 0):
            return 0

        return None

    def __str__(self):
        return "\n".join([" ".join([str(x) for x in row]) for row in self.board])

if __name__ == "__main__":
    game = Jdv()

    # Game loop
    while True:
        # Clear the console
        print("\n" * 100)

        # Display the board
        print(game)

        # Display the current player's turn
        print("Player", game.currentPlayer, "'s turn")

        # Get the player's input
        try:
            x, y = map(int, input("Enter the coordinates (x, y) or 'q' to quit: ").split())
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space or 'q' to quit.")
            continue

        # Handle quitting the game
        if x == 'q' or y == 'q':
            break

        # Check if the move is valid
        if game.is_valid_move(x, y):
            # Make the move
            game.play(x, y)
        else:
            print("Invalid move. Please try again.")
            continue

        # Check if there is a winner
        winner = game.check_winner()
        if winner is not None:
            if winner == 0:
                print("Draw!")
            else:
                print("Player", winner, "wins!")
            break
