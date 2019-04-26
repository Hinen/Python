# -*- coding: utf-8 -*-

from .Scene import *

class SceneDesc(SceneBase):
    def __init__(self, type, win, canvas, sceneManager):
        super().__init__(type, win, canvas, sceneManager)

        self.createImage(400, 300, "whiteBG.png")
        self.createText(400, 100, "설명", 40)

        self.createText(400, 200, "덧셈 문제와 보기 2개가 나오면", 20)
        self.createText(400, 240, "정답이 아닌 틀린 답을 클릭하세요!", 20, "red")
        self.createText(400, 280, "단, 덧셈의 정답이 9일 경우에는", 20)
        self.createText(400, 320, "올바른 답을 선택해주세요!", 20, "red")
        self.createText(400, 400, "이제부터 당신의 뇌를 9로 변환하겠습니다!", 20)

        self.createButton(650, 550, 15, 2, "뒤로가기", 20, self.goMenu)

    def goMenu(self):
        SoundManager.get().playFX("select.wav")
        self.sceneManager.sceneChange(SceneType.MENU)