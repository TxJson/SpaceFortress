#ui.py

from graphics import Rectangle
from graphics import Text as TextObject
from graphics import color_rgb
from graphics import Point

class Text:
    def __init__(self, pos, text="TEMPLATE", size=18, c=color_rgb(0,0,0), style="normal", font="arial"):
        self.pos = pos
        self.text = text
        self.size = size
        self.color = c
        self.style = style
        self.font = font

        self.object = TextObject(pos, text)
        self.object.setSize(size)
        self.object.setFill(c)
        self.object.setStyle(style)
        self.object.setFace(font)

    def draw(self, win):
        self.object.draw(win)

    def undraw(self):
        self.object.undraw()


class Button:
    def __init__(self, pos, width, height, type=None, bc=color_rgb(255, 255, 255),
    text="", size=18, txtc=color_rgb(0,0,0), style="normal", font="arial"):

        oWidth = width/2 #offset width
        oHeight = height/2 #offset height

        pos1 = Point(pos.getX()-oWidth, pos.getY()-oHeight)
        pos2 = Point(pos.getX()+oWidth, pos.getY()+oHeight)

        self.object = Rectangle(pos1, pos2)
        self.object.setFill(bc)
        self.object.setOutline(color_rgb(255, 255, 255))
        self.pos = pos
        self.pos1 = pos1 #Left-Up Corner
        self.pos2 = pos2 #Right-Down Corner
        self.type = type
        self.width = width
        self.height = height

        self.text = Text(self.object.getCenter(), text, size, txtc, style, font)


    def draw(self, win):
        self.object.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.object.undraw()
        self.text.undraw()

    def getPos(self):
        return self.pos

    def getPos1(self):
        return self.pos1

    def getPos2(self):
        return self.pos2

    def getType(self):
        return self.type
