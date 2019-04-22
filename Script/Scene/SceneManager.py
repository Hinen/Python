from Script.Scene.Scene import *
from Script.Scene.SceneIntro import SceneIntro
from Script.Core.SingleTon import SingleTon

class SceneManager(SingleTon):
    canvas = None

    def SceneChange(self, type, *canvas):
        if canvas:
            self.canvas = canvas[0]

        targetScene = None
        if type is SceneType.INTRO:
            targetScene = SceneIntro(self.canvas)

        return targetScene

