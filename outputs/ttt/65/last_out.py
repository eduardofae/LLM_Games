class Jdv:
    def __init__(self):
        self.board = np.zeros((3, 3))
        self.players = ['X', 'O']
        self.current_player = self.players[0]
        self.valid_moves = [(i, j) for i in range(3) for j in range(3) if self.board[i, j] == 0]

    def play(self):
        """
        Plays the jdv game.
        """

        while self.valid_moves:
            # Get the current player's move
            move = input(f"Player {self.current_player}, enter your move (row, column): ")
            move = move.split(',')
            move = (int(move[0]), int(move[1]))

            # Check if the move is valid
            if move not in self.valid_moves:
                print("Invalid move. Please try again.")
                continue

            # Place the current player's piece on the board
            self.board[move[0], move[1]] = self.current_player

            # Check if the current player has won
            if self.check_win(self.current_player):
                print(f"Player {self.current_player} wins!")
                break

            # Switch to the other player
            self.current_player = self.players[(self.players.index(self.current_player) + 1) % 2]

            # Update the list of valid moves
            self.valid_moves = [(i, j) for i in range(3) for j in range(3) if self.board[i, j] == 0]

        # If there are no more valid moves, the game is a draw
        if not self.valid_moves:
            print("Draw!")

    def check_win(self, player):
        """
        Checks if the given player has won the game.

        Args:
            player: The player to check.

        Returns:
            True if the player has won, False otherwise.
        """

        # Check for a win in the rows
        for row in self.board:
            if all(row == player):
                return True

        # Check for a win in the columns
        for col in self.board.T:
            if all(col == player):
                return True

        # Check for a win in the diagonals
        if all(self.board.diagonal() == player) or all(np.flip(self.board).diagonal() == player):
            return True

        # Otherwise, the player has not won
        return False

if __name__ == "__main__":
    jdv = Jdv()
    jdv.play()
