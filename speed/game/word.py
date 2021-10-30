import random
from game import constants
from game.actor import Actor
from game.point import Point

class Word (Actor):
    """Food is a nutritious substance that snakes like.
    The responsibility of Food is to keep track of its 
    appearance and position. Food can move around randomly
    if asked to do so.

    Attributes:
        _points (number) : A randomly genereated number of
            points from 1-5 that the player will get
            everytime they eat a food.
    """

    def __init__(self):
        super().__init__()
        self._text = random.choice(constants.LIBRARY)
        x = random.randint(2, constants.MAX_X)
        y = random.randint(2, constants.MAX_Y)
        self._position = Point(x, y)
        self._points = 1
        if random.randint(1,2) == 1:
            self._velocity = Point(1, 0)
        else:
            self._velocity = Point(0, 1)

    def reset(self):
        self._text = random.choice(constants.LIBRARY)
        x = random.randint(2, constants.MAX_X)
        y = random.randint(2, constants.MAX_Y)
        self._position = Point(x, y)
        if random.randint(1, 2) == 1:
            self._velocity = Point(1, 0)
        else:
            self._velocity = Point(0, 1)

    def get_points(self):
        return self._points
