#data.py

from enum import Enum

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
