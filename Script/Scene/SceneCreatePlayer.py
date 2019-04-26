# -*- coding: utf-8 -*-

from .Scene import *

class SceneCreatePlayer(SceneBase):
    entry = None

    def __init__(self, type, win, sceneManager):
        super().__init__(type, win, sceneManager)

        self.createImage(400, 300, "whiteBG.png")
        self.createText(400, 100, "당신의 이름은?", 40)

        self.entry = self.createEntry(400, 300, 10, 5, 20, self.naming)

    def naming(self, event):
        name = self.entry.object.get()
        if not name:
            name = "박수빈충성충성^^7"

        # init player
        Player.get(name)
        self.sceneManager.sceneChange(SceneType.MENU)