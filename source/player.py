#player.py

from graphics import *
import input as k

class Player():
    body = None
    sprite = None

    def __init__(self, x, y, win, spriteLoc):
        global sprite
        sprite = Image(Point(x, y), spriteLoc)
        sprite.draw(win)
        pass

    def update(delta = 1.0):
        if k.kUp(): #If key up is pressed
            sprite.move(0, -0.2)
        if k.kDown(): #If key down is pressed
            sprite.move(0, 0.2)
        if k.kLeft(): #If key left is pressed
            sprite.move(-0.2, 0)
        if k.kRight(): #If key right is pressed
            sprite.move(0.2, 0)
        pass

    def draw(self, win):
        global sprite
        sprite.draw(win)
        pass

    def clear():
        global sprite
        sprite.undraw()
