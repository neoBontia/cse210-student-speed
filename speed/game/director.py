from time import sleep
from game import constants
from game.word import Word
from game.score import Score
from game.buffer import Buffer

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        food (Food): The snake's target.
        input_service (InputService): The input mechanism.
        keep_playing (boolean): Whether or not the game can continue.
        output_service (OutputService): The output mechanism.
        score (Score): The current score.
        buffer (Buffer): The player or where the player types.
    """

    def __init__(self, input_service, output_service):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self._word_list = []
        for _ in range(constants.STARTING_WORDS):
            word = Word()
            self._word_list.append(word)
        self._input_service = input_service
        self._keep_playing = True
        self._output_service = output_service
        self._score = Score()
        self._buffer = Buffer()
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._keep_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()
            sleep(constants.FRAME_LENGTH)

    def _get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means getting the desired direction and moving the snake.

        Args:
            self (Director): An instance of Director.
        """
        self._buffer.add_characters(self._input_service.get_letter())  # adding a char at every type
        for word in self._word_list:
            word.move_next()

    def _do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means checking for a collision and updating the score.

        Args:
            self (Director): An instance of Director.
        """
        self._handle_checking()
        
    def _do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means checking if there are stones left and declaring 
        the winner.

        Args:
            self (Director): An instance of Director.
        """
        self._output_service.clear_screen()
        for word in self._word_list:
            self._output_service.draw_actor(word)
        self._output_service.draw_actors(self._buffer.get_all())
        self._output_service.draw_actor(self._score)
        self._output_service.check(self._buffer.get_string()) # prints the current string
        self._output_service.flush_buffer()

    def _handle_checking(self):
        answer = self._buffer.get_string()

        for word in self._word_list:
            key = word.get_text()

            if answer == key:
                self._score.add_points(word.get_points())
                word.reset()
