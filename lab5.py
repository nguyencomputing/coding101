from tkinter import *
import random
import numpy as np

TARGET = 2048
colours = {0:"#cec3b5", 2:"#eee4da", 4:"#ede0c8", 8:"#f2b179", 16:"#f59563", 32:"#f67c5f", 64:"#f65e3b", 128:"#edcf72", 256:"#edcc61", 512:"#edc850", 1024:"#edc53f", 2048:"#edc22e"}


class window(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.squares = []
        self.master.title = "Window"
        self.board = []
        for i in range(4):
            self.board.append([0] * 4)
        self.addTwo()
        self.addTwo()
        self._init_window()

    def _init_window(self):
        for i in range(4):
            for j in range(4):
                square = Label(text="{}".format(self.board[i][j]), height=10, width=20, borderwidth=4, relief="solid", font=("Helvetica", 17, "bold"))
                square.grid(row=i, column=j)
                self.squares.append(square)
        self.colours()

    def display(self):
        pos = 0
        for i in range(4):
            for j in range(4):
                self.squares[pos]['text'] = self.board[i][j]
                pos += 1
        self.colours()

    def colours(self):
        pos = 0
        for i in range(4):
            for j in range(4):
                self.squares[pos]['bg'] = colours[self.board[i][j]]
                pos += 1

    def addTwo(self):
        if not self.checkFull():
            newPos = random.choice([[i, j] for i in range(len(self.board))
                                    for j in range(len(self.board[i])) if self.board[i][j] == 0])
            self.board[newPos[0]][newPos[1]] = 2

    def checkFull(self):
        if len([[i, j] for i in range(len(self.board)) for j in range(len(self.board[i]))
                if self.board[i][j] == 0]) == 0:
            return True
        else:
            return False

    def checkWin(self):
        if TARGET in np.array(self.board):
            return True
        else:
            return False

    def checkLose(self):
        if len([[i, j] for i in range(len(self.board)) for j in range(len(self.board[i])) if
                self.board[i][j] == 0]) == 0:
            for pos in [[i, j] for i in range(len(self.board))
                        for j in range(len(self.board[i])) if self.board[i][j] != TARGET]:
                if pos[1] - 1 >= 0:
                    if self.board[pos[0]][pos[1] - 1] == self.board[pos[0]][pos[1]]:
                        return True
                if pos[1] + 1 <= 3:
                    if self.board[pos[0]][pos[1] + 1] == self.board[pos[0]][pos[1]]:
                        return True
                if pos[0] - 1 >= 0:
                    if self.board[pos[0] - 1][pos[1]] == self.board[pos[0]][pos[1]]:
                        return True
                if pos[0] + 1 <= 3:
                    if self.board[pos[0] + 1][pos[1]] == self.board[pos[0]][pos[1]]:
                        return True
        return False

    def change(self, event):
        if repr(event.char) == "'a'":
            self.left()
            if not self.checkFull(): self.addTwo()
            self.display()
        elif repr(event.char) == "'w'":
            self.up()
            if not self.checkFull(): self.addTwo()
            self.display()
        elif repr(event.char) == "'s'":
            self.down()
            if not self.checkFull(): self.addTwo()
            self.display()
        elif repr(event.char) == "'d'":
            self.right()
            if not self.checkFull(): self.addTwo()
            self.display()
        if self.checkLose():
            pos = 0
            for i in range(4):
                for j in range(4):
                    self.squares[pos].destroy()
                    pos += 1
            self.bruh = Label(text="You lost! :(", font=("Helvetica", 70, "bold"))
            self.bruh.place(x=230, y=375)
        elif self.checkWin():
            pos = 0
            for i in range(4):
                for j in range(4):
                    self.squares[pos].destroy()
                    pos += 1
            self.bruh = Label(text="You won! :)", font=("Helvetica", 70, "bold"))
            self.bruh.place(x=230, y=375)

    def left(self):
        allNumPos = [[i, j] for i in range(len(self.board)) for j in range(len(self.board[i])) if self.board[i][j] != 0]
        for pos in allNumPos:
            num = self.board[pos[0]][pos[1]]
            while pos[1] - 1 >= 0:
                if self.board[pos[0]][pos[1] - 1] == 0:
                    self.board[pos[0]][pos[1] - 1] = num
                    self.board[pos[0]][pos[1]] = 0
                    pos[1] -= 1
                else:
                    break
            if pos[1] - 1 >= 0:
                if self.board[pos[0]][pos[1] - 1] == num:
                    self.board[pos[0]][pos[1] - 1] = num * 2
                    self.board[pos[0]][pos[1]] = 0
                    pos[1] -= 1
            elif list("{}{}".format(pos[0], pos[1] - 1)) in allNumPos:
                allNumPos.append(pos)

    def up(self):
        allNumPos = [[i, j] for i in range(len(self.board)) for j in range(len(self.board[i])) if self.board[i][j] != 0]
        for pos in allNumPos:
            num = self.board[pos[0]][pos[1]]
            while pos[0] - 1 >= 0:
                if self.board[pos[0] - 1][pos[1]] == 0:
                    self.board[pos[0] - 1][pos[1]] = num
                    self.board[pos[0]][pos[1]] = 0
                    pos[0] -= 1
                else:
                    break
            if pos[0] - 1 >= 0:
                if self.board[pos[0] - 1][pos[1]] == num:
                    self.board[pos[0] - 1][pos[1]] = num * 2
                    self.board[pos[0]][pos[1]] = 0
                    pos[0] -= 1
            elif list("{}{}".format(pos[0] - 1, pos[1])) in allNumPos:
                allNumPos.append(pos)

    def down(self):
        self.board[0][0] = TARGET
        allNumPos = [[i, j] for i in range(len(self.board)) for j in range(len(self.board[i])) if self.board[i][j] != 0]
        for pos in allNumPos:
            num = self.board[pos[0]][pos[1]]
            while pos[0] + 1 <= 3:
                if self.board[pos[0] + 1][pos[1]] == 0:
                    self.board[pos[0] + 1][pos[1]] = num
                    self.board[pos[0]][pos[1]] = 0
                    pos[0] += 1
                else:
                    break
            if pos[0] + 1 <= 3:
                if self.board[pos[0] + 1][pos[1]] == num:
                    self.board[pos[0] + 1][pos[1]] = num * 2
                    self.board[pos[0]][pos[1]] = 0
                    pos[0] += 1
                elif list("{}{}".format(pos[0] + 1,pos[1])) in allNumPos:
                    allNumPos.append(pos)

    def right(self):
        allNumPos = [[i, j] for i in range(len(self.board)) for j in range(len(self.board[i]))
                     if self.board[i][j] != 0]
        for pos in reversed(allNumPos):
            num = self.board[pos[0]][pos[1]]
            while pos[1] + 1 <= 3:
                if self.board[pos[0]][pos[1] + 1] == 0:
                    self.board[pos[0]][pos[1] + 1] = num
                    self.board[pos[0]][pos[1]] = 0
                    pos[1] += 1
                else:
                    break
            if pos[1] + 1 <= 3:
                if self.board[pos[0]][pos[1] + 1] == num:
                    self.board[pos[0]][pos[1] + 1] = num * 2
                    self.board[pos[0]][pos[1]] = 0
                    pos[1] += 1
                elif list("{}{}".format(pos[0],pos[1]+1)) in allNumPos:
                    allNumPos.append(pos)


root = Tk()
app = window(root)
root.bind("<Key>", app.change)
root.mainloop()
