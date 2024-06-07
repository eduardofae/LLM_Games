import numpy as np

class Jdv:
    def __init__(self):
        self.board = np.zeros((3, 3))
        self.player = 1  # 1 for player 1, 2 for player 2
        self.winner = None
        self.num_moves = 0

    def play(self, row, col):
        try:
            if self.board[row, col] == 0 and self.winner is None:
                self.board[row, col] = self.player
                self.num_moves += 1
                self.check_winner()
                self.player = 3 - self.player  # Switch player
        except IndexError:
            raise InvalidMoveError("Invalid move. Please enter a valid row and column.")

    def check_winner(self):
        # Check rows
        for i in range(3):
            if np.all(self.board[i, :] == self.player):
                self.winner = self.player
                return

        # Check columns
        for j in range(3):
            if np.all(self.board[:, j] == self.player):
                self.winner = self.player
                return

        # Check diagonals
        if np.all(self.board.diagonal() == self.player):
            self.winner = self.player
            return

        if np.all(np.flipud(self.board).diagonal() == self.player):
            self.winner = self.player
            return

        # Check draw
        if self.num_moves == 9:
            self.winner = 0

    def print_board(self):
        for row in self.board:
            print(" | ".join(["." if x == 0 else "X" if x == 1 else "O" for x in row]))
            print("-" * 7)

    def is_finished(self):
        return self.winner is not None

    def get_winner(self):
        return self.winner

    def get_num_moves(self):
        return self.num_moves

    def minimax(self, depth, maximizing_player):
        """
        Minimax algorithm for finding the best move for the AI opponent.

        Args:
            depth (int): The current depth of the search tree.
            maximizing_player (bool): True if the AI is the maximizing player, False if it is the minimizing player.

        Returns:
            A tuple containing the best move (row, col) and its corresponding score.
        """

        # Check if the game is finished
        if self.is_finished():
            if self.winner == 1:
                return None, -1  # AI loses
            elif self.winner == 2:
                return None, 1  # AI wins
            else:
                return None, 0  # Draw

        # Find all possible moves for the current player
        possible_moves = []
        for i in range(3):
            for j in range(3):
                if self.board[i, j] == 0:
                    possible_moves.append((i, j))

        # Evaluate each possible move and choose the best one
        best_move = None
        best_score = -np.inf if maximizing_player else np.inf
        for move in possible_moves:
            row, col = move
            self.play(row, col)  # Make the move
            score = self.minimax(depth + 1, not maximizing_player)[1]  # Get the score for the opponent's move
            self.board[row, col] = 0  # Undo the move
            if maximizing_player:
                if score > best_score:
                    best_move = move
                    best_score = score
            else:
                if score < best_score:
                    best_move = move
                    best_score = score

        return best_move, best_score


class InvalidMoveError(Exception):
    pass


def main():
    # Initialize the game
    game = Jdv()

    # Get player symbols
    player1_symbol = input("Player 1, choose your symbol (X or O): ")
    player2_symbol = input("Player 2, choose your symbol (X or O): ")

    # Ensure valid symbols
    while player1_symbol not in ["X", "O"] or player2_symbol not in ["X", "O"] or player1_symbol == player2_symbol:
        print("Invalid symbols. Please choose different symbols.")
        player1_symbol = input("Player 1, choose your symbol (X or O): ")
        player2_symbol = input("Player 2, choose your symbol (X or O): ")

    # Game loop
    while not game.is_finished():
        game.print_board()
        print("Number of moves made:", game.get_num_moves())

        # Get player 1 move
        if game.player == 1:
            symbol = player1_symbol
            row, col = map(int, input("Player 1 ({}): Enter row and column (e.g. 0 1): ".format(symbol)).split())
            try:
                game.play(row, col)
            except InvalidMoveError as e:
                print(e)
        # Get player 2 move (AI opponent)
        else:
            symbol = player2_symbol
            move, _ = game.minimax(0, True)
            row, col = move
            game.play(row, col)

    # Game over
    game.print_board()
    winner = game.get_winner()
    if winner == 0:
        print("Draw!")
    else:
        print("Player {} ({}) wins!".format(winner, player1_symbol if winner == 1 else player2_symbol))


if __name__ == "__main__":
    main()
