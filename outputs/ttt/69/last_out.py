import numpy as np
import turtle
import winsound

# Create the game board
board = np.zeros((3, 3))

# Define the player symbols
player1 = 'X'
player2 = 'O'

# Create the turtle graphics
turtle.setup(600, 600)
turtle.title("Tic-Tac-Toe")
turtle.speed(0)
turtle.hideturtle()
turtle.penup()

# Draw the game board
def draw_board():
    for i in range(3):
        for j in range(3):
            turtle.goto(100 * i, 100 * j)
            turtle.pendown()
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.left(90)
            turtle.forward(100)
            turtle.penup()

# Check if the move is valid
def is_valid_move(move):
    if move[0] < 0 or move[0] > 2 or move[1] < 0 or move[1] > 2:
        return False
    if board[move[0], move[1]] != 0:
        return False
    return True

# Place the player's piece on the board
def place_piece(player, move):
    board[move[0], move[1]] = player

# Check if the player has won
def has_won(player):
    if any([
        np.all(board[i, :] == player) for i in range(3)
    ] or [
        np.all(board[:, i] == player) for i in range(3)
    ] or [
        np.all(np.diagonal(board) == player) or
        np.all(np.flip(np.diagonal(board), axis=0) == player)
    ]):
        return True
    return False

# Check if there are no more free spaces
def is_draw():
    if np.all(board != 0):
        return True
    return False

# Reset the game board
def reset_board():
    board[:] = 0

# Play the game sound
def play_sound():
    winsound.Beep(2500, 100)

# Start the game loop
while True:
    # Get the player's move
    player = player1 if player1 == 'X' else player2
    move = input("Player {}'s turn: ".format(player))
    move = [int(x) for x in move.split(',')]

    # Check if the move is valid
    if not is_valid_move(move):
        print("Invalid move. Please try again.")
        continue

    # Place the player's piece on the board
    place_piece(player, move)

    # Draw the player's piece
    turtle.goto(100 * move[0] + 50, 100 * move[1] + 50)
    turtle.write(player, font=("Arial", 50, "bold"))

    # Check if the player has won
    if has_won(player):
        print("Player {} wins!".format(player))
        play_sound()
        break

    # Check if there are no more free spaces
    if is_draw():
        print("It's a draw!")
        play_sound()
        break

    # Switch the player
    player1, player2 = player2, player1

    # Ask the user if they want to play again
    again = input("Play again? (y/n) ")
    if again == 'y':
        reset_board()
        draw_board()
    else:
        break

# Keep the turtle window open until the user clicks
turtle.exitonclick()
