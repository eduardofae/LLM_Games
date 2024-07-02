import numpy as np

def jdv():
  """
  Plays a game of JDV (Jogo da Velha).

  Returns:
    The winner of the game, or None if the game is a draw.
  """

  board = np.zeros((3, 3), dtype=int)
  player1 = input("Player 1 name: ")
  player2 = input("Player 2 name: ")
  turn = 1

  while True:
    try:
      move = input(f"{player1 if turn == 1 else player2}'s move: ")
      row, col = map(int, move.split())
      if not (1 <= row <= 3 and 1 <= col <= 3):
        raise ValueError
      if board[row - 1, col - 1] != 0:
        raise ValueError
    except ValueError:
      print("Invalid move.")
      continue

    row -= 1
    col -= 1
    board[row, col] = turn

    if check_win(board, turn):
      print(f"{player1 if turn == 1 else player2} wins!")
      return player1 if turn == 1 else player2

    if np.all(board != 0):
      print("Draw!")
      return None

    turn = 3 - turn

def check_win(board, turn):
  for row in range(3):
    if np.all(board[row, :] == turn):
      return True

  for col in range(3):
    if np.all(board[:, col] == turn):
      return True

  if np.all(board.diagonal() == turn):
    return True

  if np.all(np.flip(board).diagonal() == turn):
    return True

  return False


if __name__ == "__main__":
  while True:
    winner = jdv()
    if winner is not None:
      print(f"{winner} wins!")
    else:
      print("Draw!")

    play_again = input("Play again? (y/n) ")
    if play_again.lower() != "y":
      break
