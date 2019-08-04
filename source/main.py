#main.py

from graphics import *
import player as plr
import uielement as ui
import input as k

window = None #Window
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
    aplr = plr.Player(100, 100, window, "content/spaceship.png")

    #initializes indev text
    global uielement
    uielement = ui.UiElement(60, 20, window, 18, "Dev build", color_rgb(255, 0, 0))

    pass

#Main update function
def update():
    global aplr
    aplr.update()

    uielement

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
            update()

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
