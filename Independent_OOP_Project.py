#tic tac toe I guess

from tkinter import *
import tkinter.font as font
from datetime import datetime
counter = 1 #counter used to determine whether to insert X or O into buttons
board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0] #current state of the board, 0 is empty cell, 1 is taken by X, 2 is taken by O
winner = False

#function to check for a win or a draw, run every time the cells are pressed.
def check_win():
    global counter, board_state
    #function to check if the win should be awarded to X or O, if there is a win all buttons are disabled
    def win_condition():
        if board_state[v1] == board_state[v2] and board_state[v2] == board_state[v3] and board_state[v1] != 0 and board_state[v2] != 0 and board_state[v3] != 0:
            if counter % 2 == 0:
                win_display.config(text = "Player O wins\nReset board to play again")
                winner = True
                list = overallFrame.grid_slaves()
                for b in list:
                    b.config(state = "disabled")
            else:
                win_display.config(text = "Player X wins\nReset board to play again")
                winner = True
                list = overallFrame.grid_slaves()
                for b in list:
                    b.config(state = "disabled")
    #code to check for win horizontally, vertically and diagonally
    v1 = v2 = v3 = 0
    for j in range(0, 9, 3):
        v1 = j
        v2 = v1 + 1
        v3 = v2 + 1
        win_condition()

    v1 = v2 = v3 = 0
    for j in range(0, 3):
        v1 = j
        v2 = v1 + 3
        v3 = v2 + 3
        win_condition()

    v1 = 0
    v2 = v1 + 4
    v3 = v2 + 4
    win_condition()
    v1 = 2
    v2 = v1 + 2
    v3 = v2 + 2
    win_condition()
    #check for draw
    if counter == 9 and winner == False:
        win_display.config(text = "Draw...\nReset the board to play again")

#function to change text in the cells depending on the counter to determine who's turn it is
def change_text(x):
    global counter
    insert = ""
    if counter % 2 == 0:
        insert = "O"
        counter += 1
    else:
        insert = "X"
        counter += 1

    x.config(text = insert, state = "disabled")

#function that updates the current board array, calls the function to check for a win
def update_board(x):
    global counter, board_state
    if str(x)[-1] == "n":
        if counter % 2 == 0:
            board_state[0] = 2
        else:
            board_state[0] = 1
    elif board_state[(int(str(x)[-1])-1)] not in range(2, 10):
        if counter % 2 == 0:
            board_state[(int(str(x)[-1])-1)] = 2
        else:
            board_state[(int(str(x)[-1])-1)] = 1

    check_win()
    
#reset button resets all variables to default and buttons to starting position
def reset_buttons():
    global counter, board_state, winner
    list = overallFrame.grid_slaves()
    for b in list:
        b.config(text = "", state = "normal")
    win_display.config(text = "X goes first")
    counter = 1
    board_state = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    winner = False

#creating window and giving properties
root = Tk()
root.title("Tic Tac Toe")
root.geometry("700x500")
root.resizable(0,0)
my_font = font.Font(size = 20)
root.config(bg = "teal")


#class to create all 9 buttons
class CreateButton:
    def __init__(self, row, column, name):
        self.row = row
        self.column = column
        self.value = ""
        self.disabled = False

        name = Button(overallFrame)
        name.config(command = lambda: [update_board(name), change_text(name)],text = self.value, height = 4, width = 8, bd = 1, bg = "#6a95de", fg = "light grey", activeforeground = "pink",activebackground = "#5785d4",  disabledforeground = "white", relief = "solid", font = my_font)
        name.grid(column = self.column, row = self.row)
    
        reset = Button(root)
        reset.config(command = lambda:reset_buttons(), text = "RESET", bg = "light blue", activebackground = "teal", font = font.Font(size = 10))
        reset.grid(column = 0, row = 1)

#label to display win or draw
win_display = Label(root)
win_display.config(text = "X goes first", font = font.Font(size = 15), bg = "teal", fg = "light grey")
win_display.grid(column = 1, row = 0, sticky = N)

#frame to house the cells
overallFrame = Frame(root)
overallFrame.config(bg = "black", bd = 2)
overallFrame.grid(column = 0, row = 0)

one = CreateButton(0, 0, "one")
two = CreateButton(0, 1, "two")
three = CreateButton(0, 2, "three")
four = CreateButton(1, 0, "four")
five = CreateButton(1, 1, "five")
six = CreateButton(1, 2, "six")
seven = CreateButton(2, 0, "seven")
eight = CreateButton(2, 1, "eight")
nine = CreateButton(2, 2, "nine")


#creating timer
def timer(w):
    ct = datetime.now().strftime("%H:%M:%S")
    timer_label.config(text = ct)
    root.after(1000, lambda: timer(w))

timer_frame = Frame(root)
timer_frame.config(bg = "black", bd = 1, relief = "solid")
timer_frame.grid(column = 0, row = 1, sticky = E)
timer_label = Label(timer_frame)
timer_label.config(bg = "teal")
timer_label.pack()
timer(timer_frame)


#root.wm_attributes("-fullscreen", True)
root.mainloop()