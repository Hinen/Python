from .Scene import *

class SceneDesc(SceneBase):
    def __init__(self, type, win, canvas, sceneManager):
        super().__init__(type, win, canvas, sceneManager)

        self.createText(400, 100, "설명", 40)