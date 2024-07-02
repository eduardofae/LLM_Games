import numpy as np

class Jdv:
    """
    A class to represent the Jdv game.

    Attributes:
        board: A 3x3 numpy array representing the game board.
        player: The current player's turn. 1 for player 1, -1 for player 2.
        num_moves: The number of moves made so far.
        player1_wins: The number of wins for player 1.
        player2_wins: The number of wins for player 2.
        player1_moves: The number of moves made by player 1.
        player2_moves: The number of moves made by player 2.
    """

    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.player = 1
        self.num_moves = 0
        self.player1_wins = 0
        self.player2_wins = 0
        self.player1_moves = 0
        self.player2_moves = 0

    def play(self, row, col):
        """
        Place a piece on the board at the given row and column.

        Args:
            row: The row to place the piece in.
            col: The column to place the piece in.
        """
        if self.board[row, col] == 0:
            self.board[row, col] = self.player
            self.player *= -1
            self.num_moves += 1
            if self.player == 1:
                self.player1_moves += 1
            else:
                self.player2_moves += 1

    def check_winner(self):
        """
        Check if there is a winner.

        Returns:
            The player who won, or 0 if there is no winner yet.
        """
        for i in range(3):
            # Check rows
            if np.all(self.board[i, :] == self.player):
                return self.player
            # Check columns
            if np.all(self.board[:, i] == self.player):
                return self.player
        # Check diagonals
        if np.all(np.diagonal(self.board) == self.player):
            return self.player
        if np.all(np.flip(np.diagonal(self.board), axis=0) == self.player):
            return self.player
        # Check draw
        if np.all(self.board != 0):
            return 0
        return None

    def __str__(self):
        """
        Return a string representation of the game board.
        """
        return "\n".join([" ".join([str(x) for x in row]) for row in self.board])

if __name__ == "__main__":
    game = Jdv()

    # Choose which player goes first
    while True:
        player = input("Choose which player goes first (1 or 2): ")
        if player == "1" or player == "2":
            game.player = int(player)
            break
        else:
            print("Invalid input. Please enter 1 or 2.")

    # Choose whether to play against the computer or another human player
    while True:
        opponent = input("Choose your opponent (computer or human): ")
        if opponent == "computer" or opponent == "human":
            break
        else:
            print("Invalid input. Please enter computer or human.")

    # Choose the difficulty of the computer player
    if opponent == "computer":
        while True:
            difficulty = input("Choose the difficulty of the computer player (easy, medium, or hard): ")
            if difficulty == "easy" or difficulty == "medium" or difficulty == "hard":
                break
            else:
                print("Invalid input. Please enter easy, medium, or hard.")

    while True:
        print(game)
        print(f"Player {game.player}'s turn.")
        if game.player == 1 or opponent == "human":
            try:
                row, col = map(int, input("Enter row and column: ").split())
            except ValueError:
                print("Invalid input. Please enter two integers.")
                continue

            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid row or column. Please enter a number between 0 and 2.")
                continue
        else:
            # Computer player's turn
            row, col = game.computer_move(difficulty)

        game.play(row, col)
        winner = game.check_winner()
        if winner is not None:
            if winner == 0:
                print("Draw!")
            else:
                print(f"Player {winner} wins!")
                if winner == 1:
                    game.player1_wins += 1
                else:
                    game.player2_wins += 1
            break

        # Check if the game is a draw
        if game.num_moves == 9:
            print("Draw!")
            break

    print(f"Player 1 wins: {game.player1_wins}")
    print(f"Player 2 wins: {game.player2_wins}")

    # Ask if the user wants to play again
    while True:
        play_again = input("Do you want to play again (yes or no): ")
        if play_again == "yes" or play_again == "no":
            break
        else:
            print("Invalid input. Please enter yes or no.")

    if play_again == "yes":
        game = Jdv()
        continue
