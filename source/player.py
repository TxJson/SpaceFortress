#player.py

from graphics import color_rgb
from graphics import Circle
from graphics import Point
import input as k
from bullet import Bullet

class Player:
    #body = None
    #obj = None
    #velocity = None
    #listBullets = None

    def __init__(self, pos, win, r, vel = 1.0, c=color_rgb(255, 255, 255)):
        #go.__init__(self, x, y, win, r, c)

        self.pos = pos
        self.radius = r
        self.vel = vel

        self.object = Circle(self.pos, r)
        self.object.setFill(c)
        self.object.draw(win)
        self.bullets = []
        #global obj
        #obj = Circle(self.pos, r)
        #obj.setFill(c)
        #obj = Image(Point(x, y), spriteLoc)
        #obj.draw(win)
        #self.y = y
        #self.vel = vel

        #global velocity
        #velocity = vel

        #global listBullets
        #listBullets = []

        pass

    def update(self, win):
        global velocity
        global listBullets
        moveX = 0.0
        moveY = 0.0
        if k.kUp(): #If key up is pressed
            moveY -= self.vel
        if k.kDown(): #If key down is pressed
            moveY += self.vel
        if k.kLeft(): #If key left is pressed
            moveX -= self.vel
        if k.kRight(): #If key right is pressed
            moveX += self.vel

        mouse = k.kMouseLeft(win)

        if mouse != None:
            self.bullets.append(Bullet(self.pos, win, 15, Point(mouse.getX(), mouse.getY())))

        #list = []
        for obj in self.bullets:
            obj.update(win)
            if obj.getAliveFlag() != True:
                obj.undraw()
                self.bullets.remove(obj)
                print("Object destroyed")
        #for obj in list:
        #    self.bullets.remove(obj)
        #    print("Bullet removed")

        self.object.move(moveX, moveY)
        self.pos = self.object.getCenter()
        pass

        #Clear function
        def clear():
            self.object.undraw()
            pass
