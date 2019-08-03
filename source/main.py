#main.py

from graphics import *
import player as plr

window = None #Window
aplr = None #Player

#Main init function
def init():
    #Initializes and loads the window
    global window
    window = GraphWin("Space Shooter", 1280, 720)
    window.setBackground(color_rgb(0, 0, 0))

    #Initializes player
    global aplr
    aplr = plr.Player(100, 100, window, "content/spaceship.png")

    pass

#Main update function
def update():
    global aplr
    aplr.update()
    pass

#Main draw function
def draw():
    global aplr
    global window
    aplr.draw(window)
    pass

#Clear the screen
def clear():
    global aplr
    aplr.clear()
    pass

#Main run function
def run():
    ms = 0.0
    global lastFrameTime
    global delta
    global window

    if not window.isClosed():
        while True:
            update()
    clear()
    window.close()
    pass

#main
def main():
    init() #Initialize
    run() #Run game
    pass

main()
