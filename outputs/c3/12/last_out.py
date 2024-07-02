import numpy as np
import socket

class Pong:
    def __init__(self):
        self.board = np.zeros((10, 10))
        self.players = ['X', 'O']
        self.current_player = 0
        self.computer_player = 'O'
        self.server_socket = None
        self.client_socket = None

    def play(self):
        # Create a server socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('localhost', 5000))
        self.server_socket.listen()

        # Accept a client connection
        self.client_socket, _ = self.server_socket.accept()

        while True:
            self.display_board()

            # Get the column from the current player
            if self.current_player == self.computer_player:
                column = self.get_computer_move()
            else:
                column = self.get_human_move()

            # Send the column to the other player
            self.send_column(column)

            # Check if the column is valid
            if not self.is_valid_column(column):
                print('Invalid column')
                continue

            # Check if the column is full
            if self.is_column_full(column):
                print('Column is full')
                continue

            # Place the piece on the board
            self.place_piece(column)

            # Check if the current player has won
            if self.check_winner():
                print('Player {} wins!'.format(self.players[self.current_player]))
                break

            # Check if the game is a draw
            if self.is_draw():
                print('Draw!')
                break

            # Switch to the other player
            self.current_player = (self.current_player + 1) % 2

    def display_board(self):
        print(self.board)

    def get_human_move(self):
        while True:
            try:
                column = int(input('Player {}: Choose a column (0-9): '.format(self.players[self.current_player])))
                if self.is_valid_column(column):
                    return column
                else:
                    print('Invalid column')
            except ValueError:
                print('Invalid input')

    def get_computer_move(self):
        # Get all possible moves
        moves = []
        for column in range(10):
            if not self.is_column_full(column):
                moves.append(column)

        # Evaluate each move using the minimax algorithm with alpha-beta pruning
        best_score = -np.inf
        best_move = None
        alpha = -np.inf
        beta = np.inf
        for move in moves:
            self.place_piece(move)
            score = self.minimax(3, False, alpha, beta)
            self.board[self.board == self.players[self.current_player]] = 0
            if score > best_score:
                best_score = score
                best_move = move
            alpha = max(alpha, score)
            if alpha >= beta:
                break

        return best_move

    def minimax(self, depth, maximizing_player, alpha, beta):
        # Check if the game is over
        if self.check_winner() or self.is_draw():
            if self.check_winner() and self.board[self.board == self.players[self.current_player]].max() == self.players[self.current_player]:
                return 1
            elif self.check_winner() and self.board[self.board == self.players[self.current_player]].max() == self.players[(self.current_player + 1) % 2]:
                return -1
            else:
                return 0

        # Get all possible moves
        moves = []
        for column in range(10):
            if not self.is_column_full(column):
                moves.append(column)

        # Evaluate each move
        scores = []
        for move in moves:
            self.place_piece(move)
            if maximizing_player:
                score = self.minimax(depth - 1, False, alpha, beta)
            else:
                score = self.minimax(depth - 1, True, alpha, beta)
            self.board[self.board == self.players[self.current_player]] = 0
            scores.append(score)

        # Choose the move with the highest score (for maximizing player) or lowest score (for minimizing player)
        if maximizing_player:
            best_score = -np.inf
            for score in scores:
                best_score = max(best_score, score)
                alpha = max(alpha, score)
                if alpha >= beta:
                    break
            return best_score
        else:
            best_score = np.inf
            for score in scores:
                best_score = min(best_score, score)
                beta = min(beta, score)
                if alpha >= beta:
                    break
            return best_score

    def is_valid_column(self, column):
        return 0 <= column < 10

    def is_column_full(self, column):
        return self.board[:, column].max() != 0

    def place_piece(self, column):
        row = np.where(self.board[:, column] == 0)[0][-1]
        self.board[row, column] = self.players[self.current_player]

    def check_winner(self):
        # Check for a horizontal win
        for row in range(10):
            if np.all(self.board[row, :] == self.players[self.current_player]):
                return True

        # Check for a vertical win
        for col in range(10):
            if np.all(self.board[:, col] == self.players[self.current_player]):
                return True

        # Check for a diagonal win
        for i in range(10):
            if np.all(self.board.diagonal(i) == self.players[self.current_player]) or np.all(np.flip(self.board).diagonal(i) == self.players[self.current_player]):
                return True

        # No winner yet
        return False

    def is_draw(self):
        return np.all(self.board != 0)

    def send_column(self, column):
        self.client_socket.send(str(column).encode())

if __name__ == '__main__':
    game = Pong()
    game.play()
