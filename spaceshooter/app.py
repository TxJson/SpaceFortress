#app.py

from graphics import GraphWin
from graphics import color_rgb
from graphics import Point

from menu import MainMenu
from game import Game

from data import GameState

import time
import input

class Application:
    def __init__(self, title = "", sWidth=1280, sHeight=720, bgC=color_rgb(0, 0, 0)):
        self.window = GraphWin(title, sWidth, sHeight)
        self.window.setBackground(bgC)

        self.gameState = GameState.MENU

        self.menu = MainMenu(self.window)
        self.game = Game(self.window)

        self.dt = 0.0 #DeltaTime
        self.lastFrameTime = 0.0

        self.setState(self.gameState)

    def quit(self):
        self.window.flush()
        self.window.close()

    def undraw(self):
        if self.gameState==GameState.MENU:
            self.menu.undraw()
        elif self.gameState==GameState.GAME:
            self.game.undraw()
        else:
            self.menu.undraw()
            self.game.undraw()

    def run(self):
        while not self.window.isClosed():
            #Calculate deltatime
            currentTime = time.time()
            self.dt = currentTime - self.lastFrameTime
            self.lastFrameTime = currentTime

            self.update(self.dt)

            if not self.window.isClosed():
                self.window.flush()

            #If the close key is pressed, close window, for debugging
            if input.kClose():
                quit()

    def update(self, dt):
        state = GameState.NONE
        if self.gameState==GameState.MENU:
            state = self.menu.update(self.window)
        elif self.gameState==GameState.GAME:
            state = self.game.update(dt, self.window)

        if not state==GameState.NONE:
            if state==GameState.QUIT:
                quit()
            else:
                self.setState(state)

    def setState(self, state=GameState.NONE):
        if state==GameState.NONE:
            self.setState(GameState.MENU)
        else:
            if state==GameState.GAMEONLINE: #Failsafe since its not yet implemented
                print("Game Online Unavailable")
                print("Reverting to GameState.GAME")
                self.setState(GameState.GAME)
            else:
                self.undraw()
                if state==GameState.GAME:
                    self.game.draw(self.window)
                elif state==GameState.MENU:
                    self.menu.draw(self.window)
                self.gameState=state
