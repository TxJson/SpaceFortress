#bullet.py

import math
from graphics import *
import functions as func

class Bullet:
    def __init__(self, pos, win, r, dest, vel = 1.0, c=color_rgb(255, 255, 255)):
        self.pos = pos #position
        self.dest = Point(dest.getX() - pos.getX(), dest.getY() - pos.getY()) #destination
        self.radius = r #radius
        self.vel = vel #velocity

        self.object = Circle(self.pos, r) #Circle
        self.object.setFill(c) #set colour
        self.object.draw(win) #draw

        self.aliveFlag = True
        pass

    def getAliveFlag(self):
        return self.aliveFlag

    #remove object from screen
    def undraw(self):
        self.object.undraw()

    def update(self, dt, win):
        #normalize values
        dest = func.normalize(self.dest.getX(), self.dest.getY())

        #calculate x and y movement
        x = dest.getX()*self.vel*dt
        y = dest.getY()*self.vel*dt

        #move object
        self.object.move(x, y)

        #set position
        self.pos = self.object.getCenter()

        #Split into two if statements for readability
        if self.pos.getX() > win.getWidth() or self.pos.getY() > win.getHeight():
            self.aliveFlag = False
        elif self.pos.getX() < 0 or self.pos.getY() < 0:
            self.aliveFlag = False
        pass
