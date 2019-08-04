#ui.py

from graphics import *

class UiElement:
    def __init__(self, pos, win, spriteLoc):
        self.pos = pos
        self.object = Image(self.pos, spriteLoc)
        self.object.draw(win)
        pass

    def __init__(self, pos, win, size=18, text="TEMPLATE",
    c = color_rgb(0,0,0), font="arial", style="normal"):

        self.pos = pos

        self.object = Text(pos, text)

        self.object.setSize(size) #Sets size of text
        self.object.setFace(font) #Sets font of text
        self.object.setStyle(style) #Sets style of text
        self.object.setFill(c) #Sets colour of text

        self.object.draw(win)
        pass

    #Clear function
    def clear():
        self.object.undraw()
        pass
