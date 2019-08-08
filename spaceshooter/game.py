#game.py

from graphics import Point
from graphics import color_rgb

from objects import Asteroid
from ui import Text
from player import Player
from data import GameState
from random import randrange

from functions import cirIntersects

import input

class Game:
    def __init__(self, win, online):
        self.player = Player(Point(win.getWidth()/2, win.getHeight()/2), 25, 450, color_rgb(255, 120, 90))
        self.online = online #For peer-to-peer gameplay
        self.asteroidCounter = 0

        self.scoreui = Text(Point(100, 100), str(self.player.getScore()), 25, color_rgb(255, 145, 164), "bold")

        if not online:
            self.asteroids = []

    def update(self, dt, win):
        data = GameState.NONE

        self.player.update(dt, win)

        if input.kReturn():
            print("Returned to menu")
            data = GameState.MENU
            self.undraw()


        #Asteroids
        self.asteroidCounter += 1

        if self.asteroidCounter>=80:
            self.createAsteroids(win)
            self.asteroidCounter=0

        for obj in self.asteroids:
            obj.update(dt, win)

            for bullet in self.player.getBullets():
                if cirIntersects(obj.getObject(), bullet.getObject()):
                    obj.setAliveFlag(False)
                    obj.undraw()
                    bullet.undraw()

                    self.player.getBullets().remove(bullet)

                    self.player.modifyScore(7)
                    self.scoreui.setText(self.player.getScore())
                    break

            if obj.getOutOfBounds():
                obj.undraw()
                self.asteroids.remove(obj)
            elif not obj.getAliveFlag():
                self.calcAsteroid(win, obj)
                self.asteroids.remove(obj)

        return data

    def createAsteroids(self, win):
        pos = Point(win.getWidth()+100, randrange(-250, win.getWidth()+250))
        dest = Point(-250, randrange(200, win.getWidth()-200))
        self.asteroids.append(Asteroid(pos, dest, win, 250, randrange(1, 4)))

    def calcAsteroid(self, win, object):
        if object.getType() > 1:
            amnt = randrange(1, 4)
            pos = object.pos
            for i in range(amnt):
                dest = Point(-250, randrange(100, win.getWidth()-100))
                self.asteroids.append(Asteroid(pos, dest, win, 250, object.getType()-1))

    def draw(self, win):
        self.player.draw(win)
        self.scoreui.draw(win)

    def undraw(self):
        self.player.undraw()
        self.scoreui.undraw()
        for obj in self.asteroids:
            obj.undraw()

        self.asteroids = []
