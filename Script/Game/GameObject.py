# -*- coding: utf-8 -*-

from tkinter import *

class GameObject():
    object = None
    isVisible = False

    _posX = 0
    _posY = 0
    _anchor = None

    def __init__(self, object, posX, posY, anchor):
        self.object = object
        self.isVisible = True

        self._posX = posX
        self._posY = posY
        self._anchor = anchor

        self.object.place(x=self._posX, y=self._posY, anchor=self._anchor)

    def setPosition(self, posX, posY):
        self._posX = posX
        self._posY = posY

        if self.isVisible:
            self.object.place(x=self._posX, y=self._posY, anchor=self._anchor)

    def setAnchor(self, anchor):
        self._anchor = anchor

        if self.isVisible:
            self.object.place(x=self._posX, y=self._posY, anchor=self._anchor)

    def setVisible(self, set):
        self.isVisible = set
        if set:
            self.object.place(x=self._posX, y=self._posY, anchor=self._anchor)
        else:
            self.object.place_forget()

    def setTextConfigure(self, text):
        self.object.configure(text=text)

