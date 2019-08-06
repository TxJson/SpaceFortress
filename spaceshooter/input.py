#input.py

import keyboard as kb

#if key up is pressed, return true, else false
def kUp():
    return True if kb.is_pressed('w') else False

#if key down is pressed, return true, else false
def kDown():
    return True if kb.is_pressed('s') else False

#if key left is pressed, return true, else false
def kLeft():
    return True if kb.is_pressed('a') else False

#if key right is pressed, return true, else false
def kRight():
    return True if kb.is_pressed('d') else False

#if key is pressed, return true, else false
def kClose():
    return True if kb.is_pressed('esc') else False

def kReturn():
    return True if kb.is_pressed('z') else False

def kMouseLeft(win):
    v = win.checkMouse()
    if v != None:
        return v
    else: return None
