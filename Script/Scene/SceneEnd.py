# -*- coding: utf-8 -*-

from .Scene import *

class SceneEnd(SceneBase):
    sound = None

    def __init__(self, type, win, sceneManager):
        super().__init__(type, win, sceneManager)

        SoundManager.get().stopBGM()
        self.sound = SoundManager.get().playFX('gameEnd.wav')

        self.createButton(650, 550, 15, 2, "메뉴로 이동", 20, self.goMenu)

    def goMenu(self):
        self.sound.stop()
        SoundManager.get().playFX("select.wav")
        self.sceneManager.sceneChange(SceneType.MENU)