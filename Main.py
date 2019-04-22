from tkinter import *
from datetime import *
from Script.Scene.SceneManager import *

class GameManager():
    _win = None
    _canvas = None

    _dt = 0
    _nowScene = None

    def __init__(self, win):
        self._win = win
        self._win.title("변환기의 모험")
        self._win.resizable(0, 0)

        # canvas setting
        self._canvas = Canvas(self._win, width=800, height=600)
        self._canvas.pack()

        # scene init
        self._nowScene = SceneManager.get(self._canvas).sceneChange(SceneType.INTRO)

        # event bind
        self._win.bind('<Key>', self.pressKeyHandler)

        self.gameLoop()

    def pressKeyHandler(self, key):
        self._nowScene.pressKeyHandler(key)

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