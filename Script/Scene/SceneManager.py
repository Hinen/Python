from Script.Scene.Scene import SceneType
from Script.Scene.SceneIntro import SceneIntro
from Script.Scene.SceneMenu import SceneMenu
from Script.Core.SingleTon import SingleTon

class SceneManager(SingleTon):
    canvas = None

    def __init__(self, *args):
        if args:
            self.canvas = args[0]

    def sceneChange(self, type):
        targetScene = None
        if type is SceneType.INTRO:
            targetScene = SceneIntro(self.canvas)
        elif type is SceneType.INTRO:
            targetScene = SceneMenu(self.canvas)

        return targetScene

