#menu.py

from graphics import Point
from graphics import color_rgb

from data import MenuButton
from data import GameState

from ui import Button

import input

class MainMenu:
    def __init__(self, win):
        self.buttonPos = Point(180, 300)
        self.buttonDis = 20
        self.buttons = []

        self.buttonAdd(160, 50, MenuButton.PLAY, "Play")
        self.buttonAdd(160, 50, MenuButton.CONNECT, "Connect")
        self.buttonAdd(160, 50, MenuButton.QUIT, "Quit")

    def update(self, win):
        data = GameState.NONE
        mouse = input.kMouseLeft(win)
        if mouse != None:
            for btn in self.buttons:
                if mouse.getX() > btn.getPos1().getX() and mouse.getX() < btn.getPos2().getX():
                    if mouse.getY() > btn.getPos1().getY() and mouse.getY() < btn.getPos2().getY():
                        if btn.getType()==MenuButton.PLAY:
                            print("Play")
                            data=GameState.GAME
                        elif btn.getType()==MenuButton.CONNECT:
                            print("Connect")
                            data=GameState.GAMEONLINE
                        elif btn.getType()==MenuButton.QUIT:
                            print("Quit")
                            data=GameState.QUIT
                        break
        return data

    def buttonAdd(self, width, height, type=MenuButton.NONE, text="", c=color_rgb(105, 105, 105)):
        btnPos = Point(self.buttonPos.getX(), self.buttonPos.getY()+((height+self.buttonDis)*len(self.buttons)))
        self.buttons.append(Button(btnPos, width, height, type, c, text))

    def draw(self, win):
        for btn in self.buttons:
            btn.draw(win)

    def undraw(self):
        #self.text.clear()
        for btn in self.buttons:
            btn.undraw()
