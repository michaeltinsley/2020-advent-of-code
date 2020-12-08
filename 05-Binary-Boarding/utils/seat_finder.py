from typing import List


class BinaryBoarding:
    TOTAL_ROWS: int = 128
    TOTAL_COLUMNS: int = 8

    def __init__(self, entry: str, num_locations: int = 7, num_positions: int = 3):
        """
        A BinaryBoarding class with relevant helper functions

        :param entry: The binary boarding seat entry
        :param num_locations: The number of row locators
        :param num_positions: The number of column locators
        """
        self.entry: str = entry
        self.row_locator: str = self.entry[:num_locations]
        self.column_locator: str = self.entry[-num_positions:]
        self._validate_entry()

        self.row: List[int] = list(range(self.TOTAL_ROWS))
        self.column: List[int] = list(range(self.TOTAL_COLUMNS))

    def _validate_entry(self):
        """
        Validate the entry is valid
        """
        assert len(self.entry) == 10
        assert set(self.row_locator).issubset({"F", "B"})
        assert set(self.column_locator).issubset({"L", "R"})

    @property
    def row_length(self) -> int:
        """
        The length of the space variable
        """
        return len(self.row)

    @property
    def row_midpoint(self) -> int:
        """
        The midpoint of the space variable
        """
        return int(self.row_length / 2)

    @property
    def column_length(self) -> int:
        """
        The length of the space variable
        """
        return len(self.column)

    @property
    def column_midpoint(self) -> int:
        """
        The midpoint of the space variable
        """
        return int(self.column_length / 2)

    def _make_row_split(self, split: str):
        """
        Calculates and makes the split

        :param split: The split token
        """
        if split == "F":
            self.row = self.row[: self.row_midpoint]
        elif split == "B":
            self.row = self.row[self.row_midpoint :]
        else:
            raise ValueError

    def _run_row(self) -> None:
        """
        Runs the first stage of seat finding
        """
        for value in self.row_locator:
            self._make_row_split(value)

    def _make_column_split(self, split: str):
        """
        Calculates and makes the split

        :param split: The split token
        """
        if split == "L":
            self.column = self.column[: self.column_midpoint]
        elif split == "R":
            self.column = self.column[self.column_midpoint :]
        else:
            raise ValueError

    def _run_column(self) -> None:
        """
        Runs the second stage of seat finding
        """
        for value in self.column_locator:
            self._make_column_split(value)

    @property
    def seat_id(self) -> int:
        """
        Calculates the seat ID for the given code

        :return: The integer seat ID
        """
        self._run_row()
        self._run_column()
        return 8 * self.row[0] + self.column[0]
