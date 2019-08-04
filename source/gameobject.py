from graphics import *

class GameObject:
    obj = None

    def __init__(self, x, y, win, spriteLoc):
        global obj
        obj = Image(Point(x, y), spriteLoc)
        obj.draw(win)
        pass

    def update():
        pass

    def move(x, y=0):
        obj.move(x, y)
        pass

    def draw(self, win):
        global obj
        obj.draw(win)
        pass

    def clear():
        global obj
        obj.undraw()
        pass
