from .Scene import *

class SceneGame(SceneBase):
    GAME_QUESTION_TIME_JOB = "GAME_QUESTION_TIME_JOB"
    GAME_BINGO_TIME_JOB = "GAME_BINGO_TIME_JOB"
    GAME_OVER_TIME_JOB = "GAME_OVER_TIME_JOB"

    _score = 0
    _count = 1
    _level = 1

    _value = [0, 0]
    _canSelect = False

    _nowQuestionCountText = None

    _firstQuestionText = None
    _firstQuestionMoreText = None
    _secondQuestionText = None
    _secondQuestionMoreText = None

    _firstAnswerButton = None
    _secondAnswerButton = None
    _whatIsYourSelectionText = None

    _scoreText = None

    def __init__(self, type, win, canvas, sceneManager):
        super().__init__(type, win, canvas, sceneManager)

        self.createImage(400, 300, "whiteBG.png")
        self.createTextData()
        self.createQuestionButton()

        # game start!
        self.registerTimer(self.GAME_BINGO_TIME_JOB, 1, self.showFirstQuestion)

    def createTextData(self):
        self._nowQuestionCountText = self.createText(30, 60, "문제 %d번" % self._count, 40, "black", W)

        self._firstQuestionText = self.createText(100, 200, "", 40) # 숫자
        self._firstQuestionMoreText = self.createText(170, 200, "", 20) # 더하기

        self._secondQuestionText = self.createText(260, 200, "", 40) # 숫자
        self._secondQuestionMoreText = self.createText(305, 200, "", 20) # 는

        self._whatIsYourSelectionText = self.createText(300, 370, "어느 쪽?", 20)

        self._scoreText = self.createText(30, 550, "뇌가 9가 된 정도 : %d" % self._score, 20, "black", W)

    def resetTextData(self):
        self._nowQuestionCountText.configure(text="문제 %d번" % self._count)
        self._firstQuestionText.configure(text="")
        self._firstQuestionMoreText.configure(text="")
        self._secondQuestionText.configure(text="")
        self._secondQuestionMoreText.configure(text="")
        self._firstAnswerButton.configure(text="")
        self._secondAnswerButton.configure(text="")

    def createQuestionButton(self):
        self._firstAnswerButton = self.createImageButton(200, 300, "circleButton.png", "", 30, self.selectQuestion, 0)
        self._secondAnswerButton = self.createImageButton(400, 300, "circleButton.png", "", 30, self.selectQuestion, 1)

    def showFirstQuestion(self):
        self.resetTextData()
        self._firstQuestionText.configure(text="2")
        self.registerTimer(self.GAME_QUESTION_TIME_JOB, 0.25, self.showFirstQuestionMore)

    def showFirstQuestionMore(self):
        self._firstQuestionMoreText.configure(text="더하기")
        self.registerTimer(self.GAME_QUESTION_TIME_JOB, 0.25, self.showSecondQuestion)

    def showSecondQuestion(self):
        self._secondQuestionText.configure(text="2")
        self.registerTimer(self.GAME_QUESTION_TIME_JOB, 0.25, self.showSecondQuestionMore)

    def showSecondQuestionMore(self):
        self._secondQuestionMoreText.configure(text="는")

        self._firstAnswerButton.configure(text="7")
        self._secondAnswerButton.configure(text="9")

        self._canSelect = True
        # 두번째 보기가 완전히 나오면 게임 오버 타이머도 등록
        self.registerTimer(self.GAME_OVER_TIME_JOB, 10, self.gameOver)

    def selectQuestion(self, selection):
        if not self._canSelect:
            return

        answer = selection[0]

        # 정답!
        self.bingo()

        # 오답!
        #self.gameOver()

    def bingo(self):
        SoundManager.get().playFX("bingo.wav")

        self._canSelect = False

        # 현재 레벨 만큼 스코어 상승
        self._score += self._level
        self._count += 1

        # text 갱신
        self._scoreText.configure(text="뇌가 9가 된 정도 : %d" % self._score)

        # 정답을 맞추면 게임 오버 타이머 제거
        self.unRegisterTimer(self.GAME_OVER_TIME_JOB)

        # 바로 다음 문제 타이머 등록
        self.registerTimer(self.GAME_BINGO_TIME_JOB, 1, self.showFirstQuestion)

    def gameOver(self):
        self._canSelect = False
        self.win.quit()
