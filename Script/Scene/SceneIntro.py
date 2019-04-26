# -*- coding: utf-8 -*-

from .Scene import *
from Script.Utility.SceneManager import *

class SceneIntro(SceneBase):
    canPressKey = False

    def __init__(self, type, win, sceneManager):
        super().__init__(type, win, sceneManager)

        self.createImage(400, 300, "whiteBG.png")
        self.createText(400, 100, "뇌를 9로 바꾸는 변환기", 40)

        self.registerTimer(self.getNotUseTimeJob(), 2, self.createPressAnyKeyText)

        # play bgm
        SoundManager.get().playBGM('taebo.wav', -1)

    def createPressAnyKeyText(self):
        self.createText(400, 400, "Press Any Key", 25, "red")
        self.canPressKey = True

    def pressKeyHandler(self, key):
        if self.canPressKey:
            self.sceneManager.sceneChange(SceneType.CREATE_PLAYER)