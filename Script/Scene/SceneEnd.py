# -*- coding: utf-8 -*-

from .Scene import *

class SceneEnd(SceneBase):
    sound = None

    def __init__(self, type, win, sceneManager):
        super().__init__(type, win, sceneManager)

        SoundManager.get().stopBGM()
        self.sound = SoundManager.get().playFX('gameEnd.wav')

        self.createImageLabel(400, 300, "whiteBG.png")

        if Player.get().getScore() >= 100:
            # perfect
            image = "perfectScoreChar.png"
        elif Player.get().getScore() >= 50:
            # good
            image = "goodScoreChar.png"
        elif Player.get().getScore() >= 25:
            # normal
            image = "normalScoreChar.png"
        elif Player.get().getScore() >= 10:
            # notbad
            image = "notbadScoreChar.png"
        else:
            # bad
            image = "badScoreChar.png"

        self.createImageLabel(120, 480, image)

        self.createText(400, 200, "%s 님의 뇌를 9로 변환한 수치는?!" % Player.get().getName(), 20)
        self.createText(400, 300, "%d" % Player.get().getScore(), 40, "blue")

        self.createButton(650, 550, 15, 2, "메뉴로 이동", 20, self.goMenu)

    def goMenu(self):
        self.sound.stop()
        SoundManager.get().playFX("select.wav")
        self.sceneManager.sceneChange(SceneType.MENU)