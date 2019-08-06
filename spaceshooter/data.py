#data.py

from enum import Enum
from graphics import color_rgb

class GameState(Enum):
    NONE=0
    QUIT=1
    MENU=2
    GAME=3
    GAMEONLINE=4


class MenuButton(Enum):
    NONE=0
    QUIT=1
    PLAY=2
    CONNECT=3

class AsteroidState(Enum):
    NONE=0
    SMALL=1
    MIDDLE=2
    BIG=3
