from .Scene import SceneType
from .SceneIntro import SceneIntro
from .SceneMenu import SceneMenu
from Script.Core.SingleTon import SingleTon

class SceneManager(SingleTon):
    canvas = None

    def __init__(self, *args):
        if args:
            self.canvas = args[0]

    def sceneChange(self, type):
        targetScene = None
        if type is SceneType.INTRO:
            targetScene = SceneIntro(self.canvas, self)
        elif type is SceneType.MENU:
            targetScene = SceneMenu(self.canvas, self)

        return targetScene

