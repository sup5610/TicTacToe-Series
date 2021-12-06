from tkinter import *
import math
#import tkinter.font as tkFont
#Normally it's import tkFont as tkFont? Don't really need tkFont here.

turnCounter = 1;#X starts. Odd numbers x, even numbers O.
insertText = "";#Text to be inserted into the button when pressed, X or O.
correspondingIndexX = 0;
correspondingIndexY = 0;
updatedBoardArray = [["","",""],
                     ["","",""],
                     ["","",""]];
winCondition = False;
arrayIndex = 0;
resetBool = False;


def movePress(correspondingButton,index):
    global turnCounter, correspondingIndexX, correspondingIndexY, arrayIndex;
    if (turnCounter % 2 == 0):
        insertText = "O";
    else:
        insertText = "X";
    turnCounter += 1;

    correspondingButton.config(text = insertText);
    correspondingButton["state"] = DISABLED;

    correspondingIndexY = math.floor(index/2.9);
    correspondingIndexX = index%3;
    updatedBoardArray[correspondingIndexY][correspondingIndexX] = insertText;
    print(updatedBoardArray);


     
def cells(cellName,x,y,index):
    cellName = Button(frame);
    cellName.config(command = lambda:movePress(cellName, index), height = 10, width = 20,bg = "#6a95de", activebackground = "#5785d4",  disabledforeground = "white", relief = "solid", bd = 1, fg = "pink", text = insertText);
    cellName.grid(column = y, row = x, columnspan = 1, rowspan = 1);
    



root = Tk();
root.title("TicTacToe");
root.geometry("1000x1000");


frame = Frame(root);
frame.config(height = 666, width = 666, bg = "black", relief = "solid", bd = 2);
frame.pack(padx = 167, pady = 167);

cells("1",0,0,0);
cells("2",0,1,1);
cells("2",0,2,2);
cells("3",1,0,3);
cells("4",1,1,4);
cells("5",1,2,5);
cells("6",2,0,6);
cells("7",2,1,7);
cells("8",2,2,8);


while resetBool == False:
    if (updatedBoardArray[0] or updatedBoardArray[1] or updatedBoardArray[2] == ["X","X","X"] or ["O","O","O"]):
        resetBool = True;
        print(updatedBoardArray);
    else:
        print("No")
        break;


root.mainloop();


