import numpy as np
import random
import winsound
import socket
import threading

def print_board(board):
  for row in board:
    for cell in row:
      print(cell, end=" ")
    print()

def check_win(board):
  # Check for horizontal wins
  for row in board:
    if len(set(row)) == 1 and row[0] != " ":
      return True

  # Check for vertical wins
  for col in range(len(board[0])):
    column = [row[col] for row in board]
    if len(set(column)) == 1 and column[0] != " ":
      return True

  # Check for diagonal wins
  diagonals = [
    [board[i][i] for i in range(len(board))],
    [board[i][len(board)-i-1] for i in range(len(board))],
  ]
  for diagonal in diagonals:
    if len(set(diagonal)) == 1 and diagonal[0] != " ":
      return True

  return False

def check_draw(board):
  return " " not in np.array(board).ravel()

def play_game(board_size=10, difficulty="easy"):
  board = np.full((board_size, board_size), " ")
  player = 1
  while True:
    print_board(board)
    print("Player", player, "turn")

    if player == 1:
      while True:
        try:
          col = int(input("Choose a column (0-9): "))
          if 0 <= col <= board_size-1:
            break
          else:
            print("Invalid column")
        except ValueError:
          print("Invalid input")
    else:
      if difficulty == "easy":
        col = random.randint(0, board_size-1)
      elif difficulty == "medium":
        # TODO: Implement medium difficulty AI
        pass
      elif difficulty == "hard":
        # TODO: Implement hard difficulty AI
        pass

    for row in range(len(board)-1, -1, -1):
      if board[row][col] == " ":
        board[row][col] = "X" if player == 1 else "O"
        break

    if check_win(board):
      print_board(board)
      print("Player", player, "wins!")
      break

    if check_draw(board):
      print_board(board)
      print("Draw!")
      break

    player = 2 if player == 1 else 1

def play_online_game(board_size=10):
  # Create a socket
  sock = socket.socket()

  # Bind the socket to a port
  sock.bind(('localhost', 9000))

  # Listen for connections
  sock.listen()

  # Accept a connection
  conn, addr = sock.accept()

  # Create a board
  board = np.full((board_size, board_size), " ")

  # Create a chat window
  chat_window = tkinter.Tk()
  chat_window.title("Chat")
  chat_window.geometry("300x200")
  chat_window.resizable(False, False)

  # Create a text box for the chat messages
  chat_text_box = tkinter.Text(chat_window)
  chat_text_box.pack()

  # Create a button to send chat messages
  chat_send_button = tkinter.Button(chat_window, text="Send")
  chat_send_button.pack()

  # Define a function to send chat messages
  def send_chat_message(event):
    message = chat_text_box.get("1.0", "end")
    conn.send(message.encode())

  # Bind the send button to the enter key
  chat_send_button.bind("<Button-1>", send_chat_message)

  # Create a thread to receive chat messages
  def receive_chat_messages():
    while True:
      message = conn.recv(1024).decode()
      chat_text_box.insert("end", message + "\n")

  threading.Thread(target=receive_chat_messages).start()

  # Game loop
  while True:
    # Print the board
    print_board(board)

    # Get the player's move
    move = input("Your move: ")

    # Send the move to the other player
    conn.send(move.encode())

    # Receive the other player's move
    move = conn.recv(1024).decode()

    # Update the board
    for row in range(len(board)-1, -1, -1):
      if board[row][int(move)] == " ":
        board[row][int(move)] = "X"
        break

    # Check for a win or draw
    if check_win(board):
      print_board(board)
      print("You win!")
      break
    elif check_draw(board):
      print_board(board)
      print("Draw!")
      break

if __name__ == "__main__":
  difficulty = input("Choose a difficulty level (easy, medium, hard): ")
  play_game(difficulty=difficulty)
