import numpy as np

def jdv(board_size=3):
  """
  This function implements the jdv game.

  The game is played on a square grid of size board_size x board_size, and two players take turns placing their pieces in a free space.
  The first player to make a line of three adjacent pieces wins the game.
  If there are no more free spaces, the game is declared a draw.

  The function takes the size of the game board as an optional argument and returns the winner of the game.
  """

  # Create the game board.
  game_board = np.array([[' ' for _ in range(board_size)] for _ in range(board_size)])

  # Get the names of the two players.
  player1 = input("Player 1, enter your name: ")
  player2 = input("Player 2, enter your name: ")

  # Set the current player to player 1.
  current_player = player1

  # Play the game until someone wins or there are no more free spaces.
  while True:
    # Get the current player's move.
    while True:
      try:
        move = input("{}'s turn. Enter a row and column number (e.g. 1,2): ".format(current_player))
        row, column = map(int, move.split(','))
        break
      except ValueError:
        print("Invalid move. Try again.")

    # Check if the move is valid.
    if row < 1 or row > board_size or column < 1 or column > board_size or game_board[row-1][column-1] != ' ':
      print("Invalid move. Try again.")
      continue

    # Place the current player's piece on the board.
    game_board[row-1][column-1] = 'X' if current_player == player1 else 'O'

    # Check if the current player has won.
    if np.any(np.all(game_board == 'X', axis=0)) or np.any(np.all(game_board == 'X', axis=1)) or np.all(game_board.diagonal() == 'X') or np.all(np.flip(game_board).diagonal() == 'X'):
      print("{} wins!".format(current_player))
      break

    # Check if there are no more free spaces.
    if np.all(game_board != ' '):
      print("Draw!")
      break

    # Switch the current player.
    current_player = player2 if current_player == player1 else player1


if __name__ == "__main__":
  jdv()
