#menu.py

import input as k
from graphics import *
#import uielement as ui
import input as k
from enum import Enum

from data import MenuButton
from data import GameState

## TODO: Move to UI Element
class Button:
    def __init__(self, pos1, pos2, type=MenuButton.NONE, bc=color_rgb(255, 255, 255),
    text="", size=18, font="arial", style="normal", txtc=color_rgb(0,0,0)):
        self.object = Rectangle(pos1, pos2)
        self.object.setFill(bc)
        self.object.setOutline(color_rgb(255, 255, 255))
        self.pos1 = pos1
        self.pos2 = pos2
        self.type = type

        self.text = Text(self.object.getCenter(), text)
        self.text.setSize(size)
        self.text.setFace(font)
        self.text.setStyle(style)
        self.text.setFill(txtc)

    def draw(self, win):
        self.object.draw(win)
        self.text.draw(win)

    def clear(self):
        self.object.undraw()
        self.text.undraw()


class MainMenu:
    def __init__(self, win):
        self.buttons = []
        self.buttons.append(Button(Point(180, 300), Point(310, 350), MenuButton.PLAY, color_rgb(105, 105, 105), "Play"))
        self.buttons.append(Button(Point(180, 380), Point(310, 430), MenuButton.CONNECT, color_rgb(105, 105, 105), "Connect"))
        self.buttons.append(Button(Point(180, 460), Point(310, 510), MenuButton.QUIT, color_rgb(105, 105, 105), "Quit"))


    def update(self, win):
        data = GameState.NONE
        mouse = k.kMouseLeft(win)
        if mouse != None:
            for btn in self.buttons:
                if mouse.getX() > btn.pos1.getX() and mouse.getX() < btn.pos2.getX():
                    if mouse.getY() > btn.pos1.getY() and mouse.getY() < btn.pos2.getY():
                        if btn.type==MenuButton.PLAY:
                            print("Play")
                            data=GameState.GAME
                        elif btn.type==MenuButton.CONNECT:
                            print("Connect")
                            data=GameState.GAMEONLINE
                        elif btn.type==MenuButton.QUIT:
                            print("Quit")
                            data=GameState.QUIT
                        break
        return data

    def draw(self, win):
        for btn in self.buttons:
            btn.draw(win)

    def clear(self):
        #self.text.clear()
        for btn in self.buttons:
            btn.clear()
