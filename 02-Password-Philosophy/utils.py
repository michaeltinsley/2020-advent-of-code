from typing import List, NamedTuple


class Row(NamedTuple):  # pylint: disable=inherit-non-class
    """
    Data object for a password entry row.
    """

    password: str
    letter: str
    min_value: int
    max_value: int


def split_row(line: str) -> Row:
    """
    Splits a given data row into it's elements.

    :param line: The unparsed input data row
    :return: A populated Row data object
    """
    values, letter, password = line.split(" ")
    min, max = values.split("-")
    return Row(password, letter.strip(":"), int(min), int(max))


def load_data(filepath: str) -> List[str]:
    """
    Reads in the raw data file

    :param filepath: The path to the datafile
    :return: A list of strings
    """
    with open(filepath) as f:
        content = [line.rstrip() for line in f]
    return content


def parse_data(data: List[str]) -> List[Row]:
    """
    Parses the loaded data into Row data objects.

    :param data: The unparsed data
    :return: The data as parsed row objects
    """
    return [split_row(row) for row in data]
