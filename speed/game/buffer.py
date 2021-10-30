from game import constants
from game.actor import Actor
from game.point import Point

class Buffer:
    '''Stereotype: Information Holder, Service Provider '''


    def __init__(self, inputService):
        """The class constructor.
        
        Args:
        """
        super().__init__()
        self._character = []
        self._prepare_buffer()
        self._segments = []

    def _prepare_buffer(self):
        """Prepares the snake body by adding segments.
        
        Args:
            
        """
        x = int(0)
        y = int(constants.MAX_Y)
        text = "Buffer: "
        position = Point(x, y)
        velocity = Point(0, 0)
        self._add_segment(text, position, velocity)

       
    def _add_segment(self, text, position, velocity):
        """Adds a new segment to the snake using the given text, position and velocity.

        Args:
           
        """
        segment = Actor()
        segment.set_text(text)
        segment.set_position(position)
        segment.set_velocity(velocity)
        self._segments.append(segment)


    def  _add_character(self): 
        '''adds a character to the buffer based on player input. Copy from Snake program but         
        there are changes.'''
        new = self._segments[-1]
        text = self._input_service.get_current()
        position = new.get_position()
        velocity = new.get_velocity()
        self._add_segment(text, position, velocity)
    
    
    def get_characters(): 
        pass
        
        
    def get_all(): 
        '''copy from the Snake program'''