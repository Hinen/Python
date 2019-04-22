from Script.Scene.Scene import *
from Script.Scene.SceneIntro import SceneIntro
from Script.Core.SingleTon import SingleTon

class SceneManager(SingleTon):
    def SceneChange(self, type):
        targetScene = None
        if type is SceneType.INTRO:
            targetScene = SceneIntro()

        return targetScene

