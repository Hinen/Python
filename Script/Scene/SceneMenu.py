from .Scene import *

class SceneMenu(SceneBase):
    def __init__(self, canvas, sceneManager):
        super().__init__(SceneType.INTRO, canvas, sceneManager)
        self.createText(400, 100, "변환기의 메뉴", 40)

    def update(self, dt):
        pass
