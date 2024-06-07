import numpy as np
import unittest

class Player:
    def __init__(self, symbol):
        self.symbol = symbol

    def take_turn(self, board):
        try:
            move = input(f"Enter your move (row, column) {self.symbol}: ")
            row, col = map(int, move.split(","))
            if row < 0 or row > 2 or col < 0 or col > 2:
                print("Invalid move. Please enter a valid move.")
                return self.take_turn(board)
            elif board[row, col] != 0:
                print("That space is already taken. Please enter a valid move.")
                return self.take_turn(board)
            else:
                return row, col
        except ValueError:
            print("Invalid input. Please enter a comma-separated pair of integers.")
            return self.take_turn(board)

class GameManager:
    def __init__(self):
        self.board = np.zeros((3, 3))
        self.player1 = Player("X")
        self.player2 = Player("O")
        self.current_player = self.player1

    def play_game(self):
        while True:
            self.print_board()
            row, col = self.current_player.take_turn(self.board)
            self.board[row, col] = self.current_player.symbol
            if self.check_win():
                print(f"Player {self.current_player.symbol} wins!")
                break
            elif (self.board == 0).any() == False:
                print("It's a draw!")
                break
            self.switch_player()

    def check_win(self):
        # Check if there is a winner in rows
        for row in self.board:
            if (row == [1, 1, 1]).all() or (row == [2, 2, 2]).all():
                return True

        # Check if there is a winner in columns
        for col in range(3):
            if (self.board[:, col] == [1, 1, 1]).all() or (self.board[:, col] == [2, 2, 2]).all():
                return True

        # Check if there is a winner in diagonals
        if (self.board.diagonal() == [1, 1, 1]).all() or (self.board.diagonal() == [2, 2, 2]).all()):
            return True
        if (np.flip(self.board).diagonal() == [1, 1, 1]).all() or (np.flip(self.board).diagonal() == [2, 2, 2]).all()):
            return True

        # No winner yet
        return False

    def switch_player(self):
        self.current_player = self.player2 if self.current_player == self.player1 else self.player1

    def print_board(self):
        for row in self.board:
            for cell in row:
                if cell == 0:
                    print(" ", end=" ")
                elif cell == 1:
                    print("X", end=" ")
                else:
                    print("O", end=" ")
            print()

class UnitTester(unittest.TestCase):
    def test_take_turn_valid_move(self):
        player = Player("X")
        board = np.zeros((3, 3))
        row, col = player.take_turn(board)
        self.assertTrue(0 <= row <= 2 and 0 <= col <= 2)

    def test_take_turn_invalid_move(self):
        player = Player("X")
        board = np.zeros((3, 3))
        with self.assertRaises(ValueError):
            player.take_turn(board, -1, 3)

    def test_take_turn_space_taken(self):
        player = Player("X")
        board = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        with self.assertRaises(ValueError):
            player.take_turn(board, 0, 0)

    def test_check_win_row(self):
        game_manager = GameManager()
        game_manager.board = np.array([[1, 1, 1], [0, 0, 0], [0, 0, 0]])
        self.assertTrue(game_manager.check_win())

    def test_check_win_column(self):
        game_manager = GameManager()
        game_manager.board = np.array([[0, 0, 0], [1, 1, 1], [0, 0, 0]])
        self.assertTrue(game_manager.check_win())

    def test_check_win_diagonal(self):
        game_manager = GameManager()
        game_manager.board = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
        self.assertTrue(game_manager.check_win())

    def test_check_win_no_winner(self):
        game_manager = GameManager()
        game_manager.board = np.zeros((3, 3))
        self.assertFalse(game_manager.check_win())

if __name__ == "__main__":
    game = GameManager()
    game.play_game()

    unittest.main()
