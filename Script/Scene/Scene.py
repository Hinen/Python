import enum

class SceneType(enum.Enum):
    NONE = 0
    INTRO = 1
    MENU = 2

class SceneBase():
    type = SceneType.NONE

    def __init__(self, type):
        self.type = type

    def update(self, dt):
        print("update %f" % dt)
        pass
