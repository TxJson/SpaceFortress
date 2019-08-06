#game.py

from graphics import Point
from graphics import color_rgb

from player import Player

from data import GameState

import input

class Game:
    def __init__(self, win):
        self.player = Player(Point(100, 100), win, 25, 450, color_rgb(0, 255, 0))
        self.online = False #For peer-to-peer gameplay

    def update(self, dt, win):
        data = GameState.NONE

        self.player.update(dt, win)

        if input.kReturn():
            print("Return to menu")
            data = GameState.MENU

        return data

    def draw(self, win):
        self.player.draw(win)

    def undraw(self):
        self.player.undraw()
