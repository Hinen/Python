import enum

class SceneType(enum.Enum):
    INTRO = 1
    MENU = 2

class SceneBase():
    type = None
    canvas = None

    def __init__(self, type, canvas):
        self.type = type
        self.canvas = canvas

    def update(self, dt):
        print("update %f" % dt)
        pass

    def createText(self, posX, posY, text, size, *color):
        textColor = "black"
        if color:
            textColor = color[0]

        self.canvas.create_text(posX, posY, text=text, font=("문체부 제목 돋음체", size), fill=textColor)
