from tkinter import *

class GameManager():
    win = None

    def __init__(self, win):
        self.win = win
        self.win.title("변환 프로그램")
        self.win.geometry("800x600")
        self.win.resizable(0, 0)
        self.gameLoop()

    def gameLoop(self):
        self.win.after(100, self.gameLoop)   # 0.1초마다 loop

_win = Tk()
_gameManager = GameManager(_win)
_win.mainloop()