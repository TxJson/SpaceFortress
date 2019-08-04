#bullet.py

import math
from graphics import *
import functions as func

class Bullet:
    #velocity = None
    #destX = 0
    #destY = 0

    def __init__(self, pos, win, r, dest, vel = 1.0, c=color_rgb(255, 255, 255)):
        #go.__init__(self, x, y, win, r, c)

        self.pos = pos
        self.dest = dest
        self.radius = r
        self.vel = vel

        self.object = Circle(self.pos, r)
        self.object.setFill(c)
        self.object.draw(win)

        self.aliveFlag = True

        #global velocity
        #velocity = vel

        #global destX
        #global destY

        #destX = destinationX
        #destY = destinationY

        pass

    def getAliveFlag(self):
        return self.aliveFlag

    def undraw(self):
        self.object.undraw()

    def update(self, win):
        #global velocity
        #global destX
        #global destY

        dest = func.normalize(self.dest.getX(), self.dest.getY())

        x = dest.getX()*self.vel
        y = dest.getY()*self.vel

        self.pos = Point(self.pos.getX()+x, self.pos.getY()+y)

        self.object.move(x, y)

        if self.pos.getX() > win.getWidth() or self.pos.getY() > win.getHeight():
            self.aliveFlag = False


        pass
