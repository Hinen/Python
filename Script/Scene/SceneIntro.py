from .Scene import *
from .SceneManager import *

class SceneIntro(SceneBase):
    canPressKey = False

    def __init__(self, canvas, sceneManager):
        super().__init__(SceneType.INTRO, canvas, sceneManager)
        self.createText(400, 100, "변환기의 모험", 40)
        self.registerTimer(2, self.createPressAnyKeyText)

    def createPressAnyKeyText(self):
        self.createText(400, 400, "Press Any Key", 15, "red")
        self.canPressKey = True

    def pressKeyHandler(self, key):
        if self.canPressKey:
            self.sceneManager.sceneChange(SceneType.MENU)