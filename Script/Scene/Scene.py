import enum

class SceneType(enum.Enum):
    INTRO = 1
    MENU = 2

class SceneBase():
    type = None

    def __init__(self, type):
        self.type = type

    def update(self, dt):
        print("update %f" % dt)
        pass
