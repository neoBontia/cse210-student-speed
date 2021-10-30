from game import constants
from game.actor import Actor
from game.point import Point


class Buffer:
    """The player or where the player types the string.

    Stereotype:
        Structurer, Information Holder

    Attributes:
        _segments (List): The buffer's list of characters (a list of Actor instances)
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Buffer): An instance of buffer.
        """
        super().__init__()
        self._segments = []
        self._prepare_buffer()

    def get_all(self):
        return self._segments

    def get_string(self):
        s = ""
        for x in self._segments[1:]:
            s += x.get_text()

        return s

    def add_characters(self, char):
        if char == "*":
            self._prepare_buffer()
        elif not char == None:  # adding new characters to the buffer
            offset = self._get_offset()
            text = char  # adding a character to the list
            position = offset
            velocity = Point(0, 0)
            self._add_segment(text, position, velocity)

    def _get_offset(self):
        offset = 0
        for x in self._segments:
            offset += len(x.get_text())

        return Point(offset, constants.MAX_Y)

    def _add_segment(self, text, position, velocity):
        segment = Actor()
        segment.set_text(text)
        segment.set_position(position)
        segment.set_velocity(velocity)
        self._segments.append(segment)

    def _prepare_buffer(self):
        self._segments.clear()  # for refreshing the buffer
        x = 0
        y = constants.MAX_Y
        text = "BUFFER > "
        position = Point(x, y)
        velocity = Point(0, 0)
        self._add_segment(text, position, velocity)
