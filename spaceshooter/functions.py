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

#if two circles intersect
def cirIntersects(circle1, circle2):
    x1 = circle1.getCenter().getX()
    y1 = circle1.getCenter().getY()
    x2 = circle2.getCenter().getX()
    y2 = circle2.getCenter().getY()

    dx = x2 - x1
    dy = y2 - y1
    rad = circle1.getRadius() + circle2.getRadius()

    return True if (((dx*dx)+(dy*dy)) < (rad*rad)) else False
