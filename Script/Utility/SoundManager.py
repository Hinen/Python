import pygame
from Script.Core.SingleTon import *

class SoundManager(SingleTon):
    fxDic = {}

    def __init__(self):
        pygame.mixer.init()

    def playBGM(self, name, loop):
        pygame.mixer.music.load('Resources/Sound/BGM/' + name)
        pygame.mixer.music.play(loop)

    def stopBGM(self):
        pygame.mixer.music.stop()

    def isPlayingBGM(self):
        return pygame.mixer.music.get_busy()

    def playFX(self, name):
        # 효과음 캐싱
        if name in self.fxDic:
            self.fxDic[name].play()
        else:
            sound = pygame.mixer.Sound('Resources/Sound/FX/' + name)
            sound.play()
            self.fxDic[name] = sound

        return self.fxDic[name]