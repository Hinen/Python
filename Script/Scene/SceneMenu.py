# -*- coding: utf-8 -*-

from .Scene import *

class SceneMenu(SceneBase):
    def __init__(self, type, win, sceneManager):
        super().__init__(type, win, sceneManager)

        self.createImageLabel(400, 300, "whiteBG.png")
        self.createText(400, 100, "메뉴", 40)

        self.createButton(400, 300, 15, 2, "게임 시작", 20, self.gameStart)
        self.createButton(400, 400, 15, 2, "게임 설명", 20, self.gameDesc)
        self.createButton(400, 500, 15, 2, "게임 종료", 20, self.gameQuit)

        if not SoundManager.get().isPlayingBGM():
            SoundManager.get().playBGM('taebo.wav', -1)

    def gameStart(self):
        SoundManager.get().playFX("select.wav")
        self.sceneManager.sceneChange(SceneType.GAME)

    def gameDesc(self):
        SoundManager.get().playFX("select.wav")
        self.sceneManager.sceneChange(SceneType.DESC)

    def gameQuit(self):
        self.win.quit()