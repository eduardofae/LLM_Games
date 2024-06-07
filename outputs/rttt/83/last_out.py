import numpy as np
import random
import os
import socket
import json

def print_board(board):
  for i in range(3):
    for j in range(3):
      if board[i][j] == 0:
        print(" ", end=" ")
      elif board[i][j] == 1:
        print("X", end=" ")
      elif board[i][j] == 2:
        print("O", end=" ")
    print()

def check_winner(board):
  # Check rows
  for i in range(3):
    if board[i][0] == board[i][1] == board[i][2] != 0:
      return board[i][0]

  # Check columns
  for j in range(3):
    if board[0][j] == board[1][j] == board[2][j] != 0:
      return board[0][j]

  # Check diagonals
  if board[0][0] == board[1][1] == board[2][2] != 0:
    return board[0][0]
  if board[0][2] == board[1][1] == board[2][0] != 0:
    return board[0][2]

  # Check draw
  if np.all(board != 0):
    return 3

  # No winner yet
  return 0

def computer_move(board):
  # Get all possible moves
  moves = []
  for i in range(3):
    for j in range(3):
      if board[i][j] == 0:
        moves.append((i, j))

  # Choose the best move using minimax algorithm
  best_move = minimax(board, 2, -np.inf, np.inf)

  return best_move

def minimax(board, player, alpha, beta):
  # Check if the game is over
  winner = check_winner(board)
  if winner != 0:
    if winner == 1:
      return -1
    elif winner == 2:
      return 1
    else:
      return 0

  # Get all possible moves
  moves = []
  for i in range(3):
    for j in range(3):
      if board[i][j] == 0:
        moves.append((i, j))

  # Evaluate all possible moves
  scores = []
  for move in moves:
    # Make the move
    board[move[0]][move[1]] = player

    # Get the score for the move
    score = -minimax(board, 3-player, -beta, -alpha)

    # Undo the move
    board[move[0]][move[1]] = 0

    # Update the scores list
    scores.append(score)

  # Choose the best move
  if player == 2:
    best_move = np.argmax(scores)
  else:
    best_move = np.argmin(scores)

  # Return the score of the best move
  return scores[best_move]

def handle_online_game(sock, player):
  # Receive the opponent's move
  data = sock.recv(1024).decode()
  move = json.loads(data)

  # Check if the move is valid
  if move[0] < 0 or move[0] > 2 or move[1] < 0 or move[1] > 2 or board[move[0]][move[1]] != 0:
    sock.send(json.dumps({"error": "Invalid move"}).encode())
    return

  # Place the opponent's piece on the board
  board[move[0]][move[1]] = 3 - player

  # Check if there is a winner
  winner = check_winner(board)

  # Send the game state back to the opponent
  data = json.dumps({"board": board.tolist(), "winner": winner})
  sock.send(data.encode())

  # If there is a winner, close the socket
  if winner != 0:
    sock.close()

def main():
  # Create a 3x3 board
  board = np.zeros((3, 3), dtype=int)

  # Player 1 starts
  player = 1

  # Create a socket for online multiplayer
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.bind(("", 5555))
  sock.listen(5)

  while True:
    # Print the board
    print_board(board)

    # Display the current player's turn
    if player == 1:
      print("Player 1's turn (X)")
    else:
      print("Computer's turn (O)")

    # Get the player's move
    if player == 1:
      try:
        row, col = map(int, input("Enter row and column (e.g. 0 2): ").split())
      except ValueError:
        print("Invalid input. Please enter two integers separated by a space.")
        continue
    else:
      row, col = computer_move(board)

    # Check if the move is valid
    if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != 0:
      print("Invalid move. Please try again.")
      continue

    # Place the player's piece on the board
    board[row][col] = player

    # Check if there is a winner
    winner = check_winner(board)

    # If there is a winner, print the winner and break out of the loop
    if winner != 0:
      if winner == 3:
        print("Draw!")
      else:
        if winner == 1:
          print("Player 1 wins!")
        else:
          print("Computer wins!")
      break

    # Check for incoming online game requests
    conn, addr = sock.accept()
    data = conn.recv(1024).decode()
    request = json.loads(data)

    # If the request is to start a new game, send the game state and start handling the online game
    if request["action"] == "new_game":
      data = json.dumps({"board": board.tolist(), "player": 2})
      conn.send(data.encode())
      handle_online_game(conn, 2)

    # Switch players
    player = 3 - player

if __name__ == "__main__":
  main()
