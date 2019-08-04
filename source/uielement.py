#ui.py

from graphics import *
import gameobject as go

class UiElement(go.GameObject):
    def __init__(self, x, y, win, spriteLoc):
        o.Object.__init__(self, x, y, win, spriteLoc)
        pass

    def __init__(self, x, y, win, size=18, text="TEMPLATE",
    c = color_rgb(0,0,0), font="arial", style="normal"):
        go.GameObject.obj = Text(Point(x, y), text)

        go.GameObject.obj.setSize(size) #Sets size of text
        go.GameObject.obj.setFace(font) #Sets font of text
        go.GameObject.obj.setStyle(style) #Sets style of text

        go.GameObject.obj.setFill(c) #Sets colour of text

        go.GameObject.obj.draw(win)
        pass

    #Draw function
    def draw(self, win):
        global obj
        obj.draw(win)
        pass

    #Clear function
    def clear():
        global obj
        obj.undraw()
        pass
