from Script.Scene.SceneManager import *
from Script.Scene.Scene import *

class SceneIntro(SceneBase):
    canPressKey = False

    def __init__(self, canvas):
        super().__init__(SceneType.INTRO, canvas)
        self.createText(400, 100, "변환기의 모험", 40)
        self.registerTimer(2, self.createPressAnyKeyText)

    def createPressAnyKeyText(self):
        self.createText(400, 400, "Press Any Key", 15, "red")
        self.canPressKey = True

    def pressKeyHandler(self, key):
        if self.canPressKey:
            SceneManager.get().sceneChange(SceneType.MENU)