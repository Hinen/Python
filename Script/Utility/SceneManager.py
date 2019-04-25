from Script.Scene.Scene import SceneType
from Script.Scene.SceneIntro import SceneIntro
from Script.Scene.SceneMenu import SceneMenu
from Script.Core.SingleTon import SingleTon

class SceneManager(SingleTon):
    win = None
    canvas = None

    def __init__(self, *args):
        if args:
            self.win = args[0]
            self.canvas = args[1]

    def sceneChange(self, type):
        targetScene = None
        if type is SceneType.INTRO:
            targetScene = SceneIntro(self.win, self.canvas, self)
        elif type is SceneType.MENU:
            targetScene = SceneMenu(self.win, self.canvas, self)

        return targetScene

