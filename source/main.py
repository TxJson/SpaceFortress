from graphics import *
import player as plr

window = None
aplr = None
delta = 0.0
lastFrameTime = 0

def init():
    global window
    window = GraphWin("Space Shooter", 1280, 720)
    window.setBackground(color_rgb(0, 0, 0))

    global aplr
    aplr = plr.Player(100, 100, window, "content/spaceship.png")

    pass

def update():
    global aplr
    aplr.update()
    pass

def draw():
    global aplr
    global window
    aplr.draw(window)
    pass

def run():
    ms = 0.0
    global lastFrameTime
    global delta
    global window

    if not window.isClosed():
        while True:
            #ms = time.clock.tick(30)
            #delta = ms - lastFrameTime
            update()
            #draw()
    window.close()
    pass


def main():
    init()
    run()
    pass

main()
