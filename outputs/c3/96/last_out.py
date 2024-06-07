class GameBoard:
    def __init__(self):
        self.board = np.zeros((10, 10), dtype=int)

    def place_piece(self, player, column):
        for i in range(9, -1, -1):
            if self.board[i, column] == 0:
                self.board[i, column] = player
                break

    def check_win(self, player):
        # Check the rows
        for i in range(10):
            if np.all(self.board[i, :] == player):
                return True

        # Check the columns
        for i in range(10):
            if np.all(self.board[:, i] == player):
                return True

        # Check the diagonals
        for i in range(6):
            for j in range(6):
                if np.all(self.board[i:i+3, j:j+3] == player):
                    return True

        for i in range(3, 10):
            for j in range(6):
                if np.all(self.board[i:i+3, j:j+3] == player):
                    return True

        return False


class Player:
    def __init__(self, name):
        self.name = name

    def get_move(self):
        while True:
            try:
                move = int(input(f"Player {self.name}, enter a column (0-9): "))
                if move < 0 or move > 9:
                    raise ValueError("Invalid move.")
                return move
            except ValueError:
                print("Invalid move.")


def main():
    # Create the game board
    board = GameBoard()

    # Create the players
    players = [Player("Player 1"), Player("Player 2")]

    # Play the game
    while True:
        # Get the player's move
        for player in players:
            print(board.board)
            try:
                move = player.get_move()
            except ValueError:
                continue

            # Place the player's piece on the board
            board.place_piece(player.name, move)

            # Check if the player has won
            if board.check_win(player.name):
                print(f"Player {player.name} wins!")
                return

        # Check if the game is a draw
        if np.all(board.board != 0):
            print("Draw!")
            return


if __name__ == "__main__":
    main()
