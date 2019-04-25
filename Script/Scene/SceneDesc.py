from .Scene import *

class SceneDesc(SceneBase):
    def __init__(self, type, win, canvas, sceneManager):
        super().__init__(type, win, canvas, sceneManager)

        self.createText(400, 100, "설명", 40)
        self.createButton(650, 550, 20, 2, "뒤로가기", 20, self.goMenu)


    def goMenu(self):
        SoundManager.get().playFX("select.wav")
        self.sceneManager.sceneChange(SceneType.MENU)