from tkinter import *
from datetime import *
from Script.Scene.SceneManager import SceneManager, SceneType

class GameManager():
    _win = None
    _dt = 0
    _nowScene = SceneManager.get().SceneChange(SceneType.INTRO)

    def __init__(self, win):
        self._win = win
        self._win.title("변환 프로그램")
        self._win.geometry("800x600")
        self._win.resizable(0, 0)

        self.gameLoop()

    def gameLoop(self):
        # calc dt
        now = datetime.now().timestamp()
        if self._dt == 0:
            self._dt = now

        updateDt = now - self._dt
        self._dt = now

        # scene update
        self._nowScene.update(updateDt)

        # loop
        self._win.after(100, self.gameLoop)

_win = Tk()
_gameManager = GameManager(_win)
_win.mainloop()