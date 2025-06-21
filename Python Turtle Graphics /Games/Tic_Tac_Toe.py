from turtle import *
import random
import tkinter as tk
from tkinter import messagebox
import winsound

screen = Screen()
screen.title("Tic Tac Toe")
screen.setup(width=600, height=600)
screen.tracer(0)

bob = Turtle()
bob.shape("turtle")
bob.speed(10)
bob.width(5)
bob.penup()
bob.hideturtle()

bob.face = lambda x, y: bob.seth(bob.towards(x, y))
bob.old_goto = bob.goto
bob.goto = lambda x, y: (bob.face(x, y), bob.old_goto(x, y))
bob.home = lambda: (bob.goto(-190, 0), bob.seth(90))

def play_sound():
    winsound.PlaySound("click.wav", winsound.SND_FILENAME | winsound.SND_ASYNC)

def draw_title():
    title_writer = Turtle()
    title_writer.hideturtle()
    title_writer.penup()
    title_writer.goto(0, 240)
    title_writer.color("black")
    title_writer.write("Tic Tac Toe", align="center", font=("Arial", 36, "bold"))

def draw_grid():
    bob.clear()
    bob.width(5)
    bob.pencolor("black")
    for x in [-50, 50]:
        bob.goto(x, 150)
        bob.pendown()
        bob.goto(x, -150)
        bob.penup()

    for y in [-50, 50]:
        bob.goto(-150, y)
        bob.pendown()
        bob.goto(150, y)
        bob.penup()

button_drawer = Turtle()
button_drawer.hideturtle()

computer_modes_visible = False

def display_score():
    bob.penup()
    bob.goto(0, -220)
    bob.color("blue")
    bob.write(f"Score - X: {x_score}  O: {o_score}", align="center", font=("Arial", 18, "bold"))
    bob.color("black")


def reset_scores():
    global x_score, o_score
    x_score = 0
    o_score = 0
    display_score()

def draw_buttons():
    button_drawer.clear()
    button_drawer.penup()
    button_drawer.goto(-120, 180)
    button_drawer.pendown()
    button_drawer.fillcolor("lightgreen")
    button_drawer.begin_fill()
    for _ in range(2):
        button_drawer.forward(240)
        button_drawer.left(90)
        button_drawer.forward(40)
        button_drawer.left(90)
    button_drawer.end_fill()
    button_drawer.penup()
    button_drawer.goto(0, 185)
    button_drawer.write("Play with Player", align="center", font=("Arial", 16, "bold"))

    button_drawer.penup()
    button_drawer.goto(-120, 130)
    button_drawer.pendown()
    button_drawer.fillcolor("lightblue")
    button_drawer.begin_fill()
    for _ in range(2):
        button_drawer.forward(240)
        button_drawer.left(90)
        button_drawer.forward(40)
        button_drawer.left(90)
    button_drawer.end_fill()
    button_drawer.penup()
    button_drawer.goto(0, 135)
    button_drawer.write("Play vs Computer", align="center", font=("Arial", 16, "bold"))

    # Reset Score button
    button_drawer.penup()
    button_drawer.goto(-120, 80)
    button_drawer.pendown()
    button_drawer.fillcolor("lightgray")
    button_drawer.begin_fill()
    for _ in range(2):
        button_drawer.forward(240)
        button_drawer.left(90)
        button_drawer.forward(40)
        button_drawer.left(90)
    button_drawer.end_fill()
    button_drawer.penup()
    button_drawer.goto(0, 85)
    button_drawer.write("Reset Scores", align="center", font=("Arial", 16, "bold"))

    if computer_modes_visible:
        button_drawer.goto(-120, 130)
        button_drawer.pendown()
        button_drawer.fillcolor("lightyellow")
        button_drawer.begin_fill()
        for _ in range(2):
            button_drawer.forward(240)
            button_drawer.left(90)
            button_drawer.forward(30)
            button_drawer.left(90)
        button_drawer.end_fill()
        button_drawer.penup()
        button_drawer.goto(0, 135)
        button_drawer.write("Easy Mode", align="center", font=("Arial", 14, "bold"))

        button_drawer.goto(-120, 90)
        button_drawer.pendown()
        button_drawer.fillcolor("orange")
        button_drawer.begin_fill()
        for _ in range(2):
            button_drawer.forward(240)
            button_drawer.left(90)
            button_drawer.forward(30)
            button_drawer.left(90)
        button_drawer.end_fill()
        button_drawer.penup()
        button_drawer.goto(0, 95)
        button_drawer.write("Intermediate Mode", align="center", font=("Arial", 14, "bold"))

        button_drawer.goto(-120, 50)
        button_drawer.pendown()
        button_drawer.fillcolor("lightcoral")
        button_drawer.begin_fill()
        for _ in range(2):
            button_drawer.forward(240)
            button_drawer.left(90)
            button_drawer.forward(30)
            button_drawer.left(90)
        button_drawer.end_fill()
        button_drawer.penup()
        button_drawer.goto(0, 55)
        button_drawer.write("Hard Mode", align="center", font=("Arial", 14, "bold"))

x_score = 0
o_score = 0
board = {}

draw_title()
draw_buttons()
display_score()


turn = "X"
busy = False
vs_computer = None

win_lines = [
    [(-1, 1), (0, 1), (1, 1)],
    [(-1, 0), (0, 0), (1, 0)],
    [(-1, -1), (0, -1), (1, -1)],
    [(-1, 1), (-1, 0), (-1, -1)],
    [(0, 1), (0, 0), (0, -1)],
    [(1, 1), (1, 0), (1, -1)],
    [(-1, 1), (0, 0), (1, -1)],
    [(1, 1), (0, 0), (-1, -1)],
]

def check_win(turn):
    for line in win_lines:
        if all(pos in board and board[pos] == turn for pos in line):
            return line
    return False

def draw_XO(pos, symbol):
    play_sound()
    x, y = pos
    x *= 100
    y *= 100
    if symbol == "X":
        bob.goto(x - 40, y + 40)
        bob.pendown()
        bob.goto(x + 40, y - 40)
        bob.penup()
        bob.goto(x + 40, y + 40)
        bob.pendown()
        bob.goto(x - 40, y - 40)
        bob.penup()
    else:
        bob.goto(x, y - 40)
        bob.setheading(0)
        bob.pendown()
        bob.circle(40)
        bob.penup()

def play_computer_move():
    global turn, busy
    if turn != "O" or check_win("X") or check_win("O"):
        return
    empty_cells = [(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1] if (x, y) not in board]
    if not empty_cells:
        return
    pos = random.choice(empty_cells)
    board[pos] = "O"
    draw_XO(pos, "O")
    win_line = check_win("O")
    if win_line:
        announce_winner("O", win_line)
    else:
        turn = "X"
        busy = False

def announce_winner(player, win_line):
    global busy, x_score, o_score
    bob.width(10)
    x1, y1 = win_line[0]
    x2, y2 = win_line[2]
    x1 *= 100
    y1 *= 100
    x2 *= 100
    y2 *= 100

    bob.goto(x1, y1)
    bob.face(x2, y2)
    bob.backward(50)
    bob.pencolor("red")
    bob.pendown()
    bob.goto(x2, y2)
    bob.forward(50)
    bob.penup()
    bob.pencolor("black")

    if player == "X":
        x_score += 1
    else:
        o_score += 1

    bob.goto(0, 160)
    bob.write(player + " wins!", font=("Arial", 40, "bold"), align="center")
    display_score()
    bob.home()
    busy = True
    screen.ontimer(ask_play_again, 1000)

def ask_play_again():
    root = tk.Tk()
    root.withdraw()
    answer = messagebox.askyesno("Game Over", "Do you want to play again?")
    root.destroy()

    if answer:
        reset_game()
    else:
        bob.clear()
        draw_grid()
        draw_title()
        display_score()
        bob.penup()
        bob.goto(0, -180)
        bob.write(f"Final Score - X: {x_score}  O: {o_score}", align="center", font=("Arial", 20, "bold"))
        bob.goto(0, -210)
        if x_score > o_score:
            bob.write("Player X Wins the Game!", align="center", font=("Arial", 18, "bold"))
        elif o_score > x_score:
            bob.write("Player O Wins the Game!", align="center", font=("Arial", 18, "bold"))
        else:
            bob.write("The Game is a Draw!", align="center", font=("Arial", 18, "bold"))
        bob.goto(0, -240)
        bob.write("Tap anywhere to exit", align="center", font=("Arial", 16, "italic"))
        screen.onclick(lambda x, y: screen.bye())
    

def reset_game():
    global board, turn, busy, vs_computer, computer_modes_visible
    board.clear()
    draw_grid()
    bob.clear()
    draw_title()
    display_score()
    computer_modes_visible = False
    draw_buttons()
    turn = "X"
    busy = False
    vs_computer = None

def on_click(x, y):
    global x_score, o_score
    global board, turn, busy, vs_computer, computer_modes_visible
    if busy:
        return
    if vs_computer is None:
        if -120 <= x <= 120 and 130 <= y <= 170:
            computer_modes_visible = not computer_modes_visible
            draw_buttons()
            return
        if computer_modes_visible:
            if -120 <= x <= 120 and 130 <= y <= 160:
                vs_computer = "easy"
            elif -120 <= x <= 120 and 90 <= y <= 120:
                vs_computer = "medium"
            elif -120 <= x <= 120 and 50 <= y <= 80:
                vs_computer = "hard"
            else:
                return
        elif -120 <= x <= 120 and 180 <= y <= 220:
            vs_computer = False
        elif -120 <= x <= 120 and 80 <= y <= 120:
            reset_scores()
            return
        else:
            return
        draw_grid()
        board.clear()
        turn = "X"
        busy = False
        button_drawer.clear()
        return

    x = round(x / 100.0)
    y = round(y / 100.0)
    if abs(x) > 1 or abs(y) > 1:
        return
    pos = (x, y)
    if pos in board:
        return

    board[pos] = turn
    draw_XO(pos, turn)

    win_line = check_win(turn)
    if win_line:
        announce_winner(turn, win_line)
        return
    if len(board) == 9:
        bob.goto(0, 160)
        bob.write("It's a Tie!", font=("Arial", 40, "bold"), align="center")
        display_score()
        busy = True
        screen.ontimer(ask_play_again, 1000)
        return

    if turn == "X":
        turn = "O"
        if vs_computer:
            busy = True
            screen.ontimer(play_computer_move, 500)
    else:
        turn = "X"

screen.onclick(on_click)
screen.mainloop()

screen.mainloop()
