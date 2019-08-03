import keyboard as kb

#if key up is pressed, return true
def kUp():
    return True if kb.is_pressed('w') else False

#if key down is pressed, return true
def kDown():
    return True if kb.is_pressed('s') else False

#if key left is pressed, return true
def kLeft():
    return True if kb.is_pressed('a') else False

#if key right is pressed, return true
def kRight():
    return True if kb.is_pressed('d') else False
