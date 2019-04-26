# -*- coding: utf-8 -*-

from Script.Core.SingleTon import *

class Player(SingleTon):
    _name = "박수빈"
    _score = 0

    def __init__(self, name):
        self._name = name

    def getName(self):
        return self._name

    def getScore(self):
        return self._score

    def setScore(self, score):
        self._score = score