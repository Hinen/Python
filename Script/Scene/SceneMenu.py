from Script.Scene.Scene import *

class SceneMenu(SceneBase):
    def __init__(self, canvas):
        super().__init__(SceneType.INTRO, canvas)
        self.createText(400, 100, "변환기의 메뉴", 40)

    def update(self, dt):
        pass
