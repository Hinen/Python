from Script.Scene.Scene import SceneType
from Script.Scene.SceneIntro import SceneIntro
from Script.Scene.SceneMenu import SceneMenu
from Script.Scene.SceneDesc import SceneDesc
from Script.Scene.SceneGame import SceneGame
from Script.Core.SingleTon import SingleTon

class SceneManager(SingleTon):
    win = None
    canvas = None
    callback = None

    def __init__(self, *args):
        if args:
            self.win = args[0]
            self.canvas = args[1]
            self.callback = args[2]

    def sceneChange(self, type):
        targetScene = None
        if type is SceneType.INTRO:
            targetScene = SceneIntro(type, self.win, self.canvas, self)
        elif type is SceneType.MENU:
            targetScene = SceneMenu(type, self.win, self.canvas, self)
        elif type is SceneType.DESC:
            targetScene = SceneDesc(type, self.win, self.canvas, self)
        elif type is SceneType.GAME:
            targetScene = SceneGame(type, self.win, self.canvas, self)

        self.callback(targetScene)

