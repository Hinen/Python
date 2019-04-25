from tkinter import *
from datetime import *
import os

def importPyGame():
    try:
        import pygame
        pygame.mixer.init()
    except ImportError:
        print("Installing PyGame")
        os.system('pip install pygame')
        importPyGame()

importPyGame()
from Script.Scene.SceneManager import *

class GameManager():
    _win = None
    _canvas = None

    _dt = 0
    _nowScene = None

    def __init__(self, win):
        self._win = win
        self._win.title("뇌가 이상해지는 변환기")
        self._win.resizable(0, 0)

        # canvas setting
        self._canvas = Canvas(self._win, width=800, height=600)
        self._canvas.pack()

        # event bind
        self._win.bind('<Key>', self.pressKeyHandler)

        # scene init
        self._nowScene = SceneManager.get(self._win, self._canvas).sceneChange(SceneType.INTRO)

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