#menu.py

import input as k
from graphics import *
import uielement as ui
import input as k

class Button:
    def __init__(self, pos1, pos2, bc=color_rgb(255, 255, 255),
    text="", size=18, font="arial", style="normal", txtc=color_rgb(0,0,0)):
        self.object = Rectangle(pos1, pos2)
        self.object.setFill(bc)
        self.object.setOutline(color_rgb(255, 255, 255))
        self.pos1 = pos1
        self.pos2 = pos2
        self.clicked = False

        self.text = Text(self.object.getCenter(), text)
        self.text.setSize(size)
        self.text.setFace(font)
        self.text.setStyle(style)
        self.text.setFill(txtc)

        pass

    def getClicked(self):
        return self.clicked

    def setButton(self, state):
        self.clicked = state

    def draw(self, win):
        self.object.draw(win)
        self.text.draw(win)
        pass


class MainMenu:
    def __init__(self, win):
        self.text = ui.UiElement(Point(win.getWidth()/2, 150), win, 30, "Space Battle", color_rgb(220,20,60))

        self.buttons = []
        self.buttons.append(Button(Point(180, 300), Point(310, 350), color_rgb(105, 105, 105), "Connect"))
        self.buttons.append(Button(Point(180, 380), Point(310, 430), color_rgb(105, 105, 105), "Quit"))

        for btn in self.buttons:
            btn.draw(win)
        pass

    def updateMouse(self, win):
        mouse = k.kMouseLeft(win)
        if mouse != None:
            for btn in self.buttons:
                if mouse.getX() > btn.pos1.getX() and mouse.getX() < btn.pos2.getX():
                    if mouse.getY() > btn.pos1.getY() and mouse.getY() < btn.pos2.getY():
                        btn.setButton(True)
                        break

            for i in range(len(self.buttons)):
                if self.buttons[i].getClicked():
                    if i == 0:
                        print("Connect pressed")
                    elif i == 1:
                        print("Quit pressed")
                        win.flush()
                        win.close()
                    self.buttons[i].setButton(False)
