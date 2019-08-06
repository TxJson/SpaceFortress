#objects.py

from graphics import Point
from graphics import Circle
from graphics import color_rgb

from data import AsteroidState
from random import randrange

from functions import normalize as norm

import math

## TODO: Add asteroid

class Asteroid:
    def __init__(self, pos, dest, win, vel, type):
        self.pos = pos
        self.dest = Point(dest.getX()-pos.getX(), dest.getY()-pos.getY())
        self.vel = vel
        self.type = type
        self.aliveFlag = True
        self.outOfBounds = False

        r = 25*type
        self.object = Circle(self.pos, r)
        self.object.setFill(color_rgb(randrange(100, 255), 240, 90))

        self.draw(win)

    def draw(self, win):
        self.object.draw(win)

    def undraw(self):
        self.object.undraw()

    def update(self, dt, win):
        #normalize values
        dest = norm(self.dest.getX(), self.dest.getY())

        #calculate x and y movement
        x = dest.getX()*self.vel*dt
        y = dest.getY()*self.vel*dt

        self.object.move(x, y)
        self.pos = self.object.getCenter()

        if self.pos.getX() < -100:
            self.outOfBounds = True

    def getAliveFlag(self):
        return self.aliveFlag

    def setAliveFlag(self, statement=True):
        self.aliveFlag = statement

    def getOutOfBounds(self):
        return self.outOfBounds

    def getType(self):
        return self.type

    def getObject(self):
        return self.object


class Bullet:
    def __init__(self, pos, win, r, dest, vel = 1.0, c=color_rgb(255, 255, 255)):
        self.pos = pos #position
        self.dest = Point(dest.getX() - pos.getX(), dest.getY() - pos.getY()) #destination
        self.radius = r #radius
        self.vel = vel #velocity

        self.object = Circle(self.pos, r) #Circle
        self.object.setFill(c) #set colour
        self.object.setOutline('black')
        self.draw(win) #draw

        self.aliveFlag = True

    def getAliveFlag(self):
        return self.aliveFlag

    def update(self, dt, win):
        #normalize values
        dest = norm(self.dest.getX(), self.dest.getY())

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

    def getObject(self):
        return self.object

    def draw(self, win):
        self.object.draw(win)

    #remove object from screen
    def undraw(self):
        self.object.undraw()
