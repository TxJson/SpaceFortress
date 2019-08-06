#game.py

from graphics import Point
from graphics import color_rgb

from player import Player
from objects import Asteroid
from data import GameState
from random import randrange

from functions import cirIntersects

import input

class Game:
    def __init__(self, win, online):
        self.player = Player(Point(100, 100), 25, 450, color_rgb(255, 120, 90))
        self.online = online #For peer-to-peer gameplay
        self.asteroidCounter = 0

        if not online:
            self.asteroids = []

    def update(self, dt, win):
        data = GameState.NONE

        self.player.update(dt, win)

        if input.kReturn():
            print("Return to menu")
            data = GameState.MENU


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

    def undraw(self):
        self.player.undraw()
