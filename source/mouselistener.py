from pynput.mouse import Listener

with Listener() as listener:
    listener.join()

def on_move(x, y):
    return Point(x, y)

def on_click_left(x, y, button, pressed):
    if pressed:
        if button is "Button.left":
            return True
    return False

def on_click_right(x, y, button, pressed):
    if pressed:
        if button is "Button.right":
            return True
    return False

def on_scroll(x, y, dx, dy):
    pass
