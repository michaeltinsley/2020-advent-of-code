import copy
from typing import List


class MapEnvironment:
    TREE_CHAR = "#"
    BLANK_CHAR = "."
    TOBOGGAN = "X"

    def __init__(self, map_data: List[List[str]]):
        """
        An actionable map environment class

        :param map_data: The parsed dataset
        """
        self.map_data = map_data
        self._horizontal_position = 0
        self._vertical_position = 0
        self._map_multiple = 1
        self.trees_encountered = 0

    @property
    def map_height(self) -> int:
        """
        The total height of the map
        """
        return len(self.map_data)

    @property
    def map_width(self) -> int:
        """
        The total width of the map
        """
        return len(self.map_data[0])

    @property
    def current_space(self) -> str:
        """
        The current space of the toboggan
        """
        return self.map_data[self._vertical_position][self._horizontal_position]

    @property
    def current_map(self) -> List[List[str]]:
        """
        The map with the toboggans current location
        """
        current_map = copy.deepcopy(self.map_data)
        current_map[self._vertical_position][self._horizontal_position] = self.TOBOGGAN
        return current_map

    @property
    def _run_complete(self) -> bool:
        """
        Asserts the run is complete
        """
        return self._vertical_position == self.map_height - 1

    def validate_move(self) -> bool:
        """
        Validates the move increasing the trees encountered

        :return: True if move is valid, False otherwise
        """
        if self.current_space == self.TREE_CHAR:
            self.trees_encountered += 1
            return False
        else:
            return True

    def _move(self, horizontal: int, vertical: int):
        """
        Update the position given a move

        :param horizontal: The horizontal movement
        :param vertical: The vertical movement
        """
        self._horizontal_position += horizontal
        self._vertical_position += vertical

        if self._horizontal_position > self.map_width - 1:
            self._horizontal_position -= self.map_width

    def execute(self, horizontal: int, vertical: int) -> int:
        """
        Runs the program for a given horizontal and vertical movement

        :param horizontal: The horizontal movement
        :param vertical: The vertical movement
        :return: The number of trees hit
        """
        while not self._run_complete:
            self._move(horizontal, vertical)
            self.validate_move()
        return self.trees_encountered
