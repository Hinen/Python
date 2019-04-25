from .Scene import *
from .SceneManager import *

class SceneIntro(SceneBase):
    canPressKey = False

    def __init__(self, win, canvas, sceneManager):
        super().__init__(SceneType.INTRO, win, canvas, sceneManager)
        self.createText(400, 100, "뇌가 이상해지는 변환기", 40)
        self.registerTimer(2, self.createPressAnyKeyText)

        pygame.mixer.music.load('Resources/Sound/BGM/taebo.wav')
        pygame.mixer.music.play(-1)

    def createPressAnyKeyText(self):
        self.createText(400, 400, "Press Any Key", 25, "red")
        self.canPressKey = True

    def pressKeyHandler(self, key):
        if self.canPressKey:
            self.sceneManager.sceneChange(SceneType.MENU)