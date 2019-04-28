# -*- coding: utf-8 -*-

import sys
from Script.Core.SingleTon import *

def isPygameImported():
    return 'pygame' in sys.modules

if isPygameImported():
    import pygame
else:
    import winsound

class SoundManager(SingleTon):
    fxDic = {}

    def __init__(self):
        if isPygameImported():
            pygame.mixer.init()

    def playBGM(self, name, loop):
        if isPygameImported():
            pygame.mixer.music.load('Resources/Sound/BGM/' + name)
            pygame.mixer.music.play(loop)
        else:
            winsound.PlaySound('Resources/Sound/BGM/' + name, winsound.SND_LOOP + winsound.SND_ASYNC)

    def stopBGM(self):
        if isPygameImported():
            pygame.mixer.music.stop()

    def isPlayingBGM(self):
        if isPygameImported():
            return pygame.mixer.music.get_busy()
        else:
            return False

    def playFX(self, name):
        if isPygameImported():
            # 효과음 캐싱
            if name in self.fxDic:
                self.fxDic[name].play()
            else:
                sound = pygame.mixer.Sound('Resources/Sound/FX/' + name)
                sound.play()
                self.fxDic[name] = sound

            return self.fxDic[name]
        else:
            return None