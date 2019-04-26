from Script.Scene.Scene import SceneType
from Script.Scene.SceneIntro import SceneIntro
from Script.Scene.SceneMenu import SceneMenu
from Script.Scene.SceneDesc import SceneDesc
from Script.Scene.SceneGame import SceneGame
from Script.Scene.SceneEnd import SceneEnd
from Script.Scene.SceneCreatePlayer import SceneCreatePlayer
from Script.Core.SingleTon import SingleTon

class SceneManager(SingleTon):
    win = None
    callback = None

    def __init__(self, *args):
        if args:
            self.win = args[0]
            self.callback = args[1]

    def sceneChange(self, type):
        targetScene = None
        if type is SceneType.INTRO:
            targetScene = SceneIntro(type, self.win, self)
        elif type is SceneType.MENU:
            targetScene = SceneMenu(type, self.win, self)
        elif type is SceneType.DESC:
            targetScene = SceneDesc(type, self.win, self)
        elif type is SceneType.GAME:
            targetScene = SceneGame(type, self.win, self)
        elif type is SceneType.END:
            targetScene = SceneEnd(type, self.win, self)
        elif type is SceneType.CREATE_PLAYER:
            targetScene = SceneCreatePlayer(type, self.win, self)

        self.callback(targetScene)

