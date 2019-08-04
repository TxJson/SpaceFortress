#player.py

import input as k
import gameobject as go

class Player(go.GameObject):
    body = None
    sprite = None

    def __init__(self, x, y, win, spriteLoc):
        go.GameObject.__init__(self, x, y, win, spriteLoc)
        pass

    def update(delta = 1.0):
        if k.kUp(): #If key up is pressed
            go.GameObject.move(0, -0.2)
        if k.kDown(): #If key down is pressed
            go.GameObject.move(0, 0.2)
        if k.kLeft(): #If key left is pressed
            go.GameObject.move(-0.2)
        if k.kRight(): #If key right is pressed
            go.GameObject.move(0.2)
        pass
