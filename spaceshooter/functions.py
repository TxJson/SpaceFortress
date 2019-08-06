#functions.py

import math
from graphics import Point

def normalize(x, y):
    #normalize
    length = math.sqrt((x*x)+(y*y))
    if length != 0.0:
        x *= (1.0/length)
        y *= (1.0/length)

    return Point(x, y)
