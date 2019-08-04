#main.py

from graphics import *
import player as plr
import uielement as ui
import input as k
import time

window = None #Window
lastFrameTime = 0.0
delta = 0.0
aplr = None #Player
uielement = None #UIElement

#Main init function
def init():
    #Initializes and loads the window
    global window
    window = GraphWin("Space Shooter", 1280, 720)
    window.setBackground(color_rgb(0, 0, 0))

    #Initializes player
    global aplr
    aplr = plr.Player(Point(100, 100), window, 25, 450, color_rgb(0, 255, 0))

    #initializes indev text
    global uielement
    uielement = ui.UiElement(Point(60, 20), window, 18, "Dev build", color_rgb(255, 0, 0))

    pass

#Main update function
def update(dt):
    global window
    global aplr
    aplr.update(dt, window)
    window.flush()
    pass

#Main draw function
def draw():
    global aplr
    global uielement
    global window
    aplr.draw(window)
    uielement.draw(window)
    pass

#Clear the screen
def clear():
    global aplr
    aplr.clear()
    pass

def close():
    global window
    window.close()

#Main run function
def run():
    ms = 0.0
    global lastFrameTime
    global delta
    global window

    if not window.isClosed():
        _ = True
        while _:
            #DeltaTime
            currentTime = time.time()
            delta = currentTime - lastFrameTime
            lastFrameTime = currentTime

            #Main update function
            update(delta)

            #if close key is pressed, close
            if k.kClose():
                close()
                _ = False
    pass

#main
def main():
    init() #Initialize
    run() #Run game
    pass

main()
