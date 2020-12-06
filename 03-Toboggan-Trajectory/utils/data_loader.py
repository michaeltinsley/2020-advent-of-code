from typing import List

FILEPATH = "./data.txt"


def load_data(filepath: str) -> List[str]:
    """
    Reads in the raw data file

    :param filepath: The path to the datafile
    :return: A list of strings
    """
    with open(filepath) as f:
        content = [line.rstrip() for line in f]
    return content


def parse_line(row: str) -> List[str]:
    """
    Parse a given row in a list of elements

    :param row: A string representation of a row
    :return: A list of elements
    """
    return [char for char in row]


def get_data(filepath: str = FILEPATH) -> List[List[str]]:
    """
    Loads the data in as a list of lists

    :param filepath: The filepath of dataset
    :return: The parsed data
    """
    data = load_data(filepath)
    return [parse_line(row) for row in data]
