#player.py

from graphics import color_rgb
from graphics import Circle
from graphics import Point

from objects import Bullet

import input as k

class Player:
    def __init__(self, pos, r, vel = 1.0, c=color_rgb(255, 255, 255)):
        self.pos = pos #position
        self.radius = r #radius
        self.vel = vel #velocity
        self.colour = c

        self.object = Circle(self.pos, r)
        self.object.setFill(c)
        self.object.setOutline('black')
        self.bullets = [] #bullet list

        self.score = 0

        print(self.object.getRadius())

    def modifyScore(self, value):
        self.score += value
        #print("Score:"+str(self.score))

    def getScore(self):
        return self.score

    def update(self, dt, win):
        x = 0.0
        y = 0.0
        if k.kUp(): #If key up is pressed
            y -= self.vel * dt
        if k.kDown(): #If key down is pressed
            y += self.vel * dt
        if k.kLeft(): #If key left is pressed
            x -= self.vel * dt
        if k.kRight(): #If key right is pressed
            x += self.vel * dt

        #Check if mouse has been clicked
        mouse = k.kMouseLeft(win)
        if mouse != None:
            #print(mouse)
            self.bullets.append(Bullet(self.pos, win, 10, Point(mouse.getX(), mouse.getY()), 1000, self.colour))

        #Update bullets and check if out of bounds
        for bullet in self.bullets:
            bullet.update(dt, win)
            if bullet.getAliveFlag() != True:
                bullet.undraw()
                self.bullets.remove(bullet)

        self.object.move(x, y)
        self.pos = self.object.getCenter()

    def getBullets(self):
        return self.bullets

    def getObject(self):
        return self.object

    def getRadius(self):
        return self.object.getRadius()

    def getPos(self):
        return self.pos

    def draw(self, win):
        self.object.draw(win)

    #undraw object
    def undraw(self):
        self.object.undraw()
