#player.py

from graphics import color_rgb
from graphics import Circle
from graphics import Point
import input as k
from bullet import Bullet

class Player:
    def __init__(self, pos, win, r, vel = 1.0, c=color_rgb(255, 255, 255)):
        self.pos = pos #position
        self.radius = r #radius
        self.vel = vel #velocity

        self.object = Circle(self.pos, r)
        self.object.setFill(c)
        self.bullets = [] #bullet list

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
            print(mouse.getX(), mouse.getY())
            self.bullets.append(Bullet(self.pos, win, 15, Point(mouse.getX(), mouse.getY()), 1000, 'green'))

        #Update bullets and check if out of bounds
        for obj in self.bullets:
            obj.update(dt, win)
            if obj.getAliveFlag() != True:
                obj.undraw()
                self.bullets.remove(obj)

        self.object.move(x, y)
        self.pos = self.object.getCenter()

    def draw(self, win):
        self.object.draw(win)

    #undraw object
    def clear(self):
        self.object.undraw()
