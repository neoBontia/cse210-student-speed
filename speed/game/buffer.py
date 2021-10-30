from game import constants
from game.actor import Actor
from game.point import Point


class Buffer:
    """A limbless reptile. The responsibility of Snake is keep track of its segments. It contains methods for moving and growing among others.

    Stereotype:
        Structurer, Information Holder

    Attributes:
        _body (List): The snake's body (a list of Actor instances)
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Snake): An instance of snake.
        """
        super().__init__()
        self._segments = []
        self._prepare_buffer()

    def get_all(self):
        """Gets all the snake's segments.
        
        Args:
            self (Snake): An instance of snake.

        Returns:
            list: The snake's segments.
        """
        return self._segments

    def add_characters(self, char):
        """Grows the snake's tail by one segment.
        
        Args:
            self (Snake): An instance of snake.
        """
        if not char == None:  # adding new characters to the buffer
            #offset = 0
            offset = self._get_offset()
            #tail = self._segments[-1]
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
        """Adds a new segment to the snake using the given text, position and velocity.

        Args:
            self (Snake): An instance of snake.
            text (string): The segment's text.
            position (Point): The segment's position.
            velocity (Point): The segment's velocity.
        """
        segment = Actor()
        segment.set_text(text)
        segment.set_position(position)
        segment.set_velocity(velocity)
        self._segments.append(segment)

    def _prepare_buffer(self):
        """Prepares the snake body by adding segments.
        
        Args:
            self (Snake): an instance of Snake.
        """
        self._segments.clear()  # for refreshing the buffer
        x = 0
        y = constants.MAX_Y
        text = "BUFFER > "
        position = Point(x, y)
        velocity = Point(0, 0)
        self._add_segment(text, position, velocity)
