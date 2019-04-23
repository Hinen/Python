import enum

class SceneType(enum.Enum):
    INTRO = 1
    MENU = 2

class Timer():
    time = 0
    callback = None

    def __init__(self, time, callback):
        self.time = time
        self.callback = callback


class SceneBase():
    type = None
    canvas = None
    sceneManager = None

    timer = {}

    def __init__(self, type, canvas, sceneManager):
        self.type = type
        self.canvas = canvas
        self.sceneManager = sceneManager
        self.clearScene()

    def update(self, dt):
        self._updateTimer(dt)

    def _updateTimer(self, dt):
        run = []
        for t in self.timer:
            if self.timer[t] is None:
                continue

            self.timer[t].time -= dt
            if self.timer[t].time <= 0:
                run.append(t)

        for i in run:
            self.timer[i].callback()
            del self.timer[i]

    def registerTimer(self, time, callback):
        # get Time Job
        timeJob = 0
        while True:
            if not (timeJob in self.timer):
                break

            timeJob -= 1

        self.timer[timeJob] = Timer(time, callback)

    def pressKeyHandler(self, key):
        pass

    def createText(self, posX, posY, text, size, *color):
        textColor = "black"
        if color:
            textColor = color[0]

        return self.canvas.create_text(posX, posY, text=text, font=("문체부 제목 돋음체", size), fill=textColor)

    def clearScene(self):
        self.canvas.delete("all")
