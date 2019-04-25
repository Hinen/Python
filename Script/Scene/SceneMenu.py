from .Scene import *

class SceneMenu(SceneBase):
    def __init__(self, win, canvas, sceneManager):
        super().__init__(SceneType.INTRO, win, canvas, sceneManager)
        self.createText(400, 100, "메뉴", 40)
        self.createButton(400, 300, 20, 2, "게임 시작", 20, self.gameStart)
        self.createButton(400, 400, 20, 2, "게임 설명", 20, self.gameDesc)
        self.createButton(400, 500, 20, 2, "게임 종료", 20, self.gameQuit)

    def gameStart(self):
        SoundManager.get().playFX("select.wav")

    def gameDesc(self):
        SoundManager.get().playFX("select.wav")

    def gameQuit(self):
        SoundManager.get().playFX("select.wav")