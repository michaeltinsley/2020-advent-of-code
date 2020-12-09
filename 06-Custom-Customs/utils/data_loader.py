import itertools
from typing import List

FILEPATH = "./data/data.txt"


def load_data(filepath: str) -> List[str]:
    """
    Reads in the raw data file

    :param filepath: The path to the datafile
    :return: A list of strings
    """
    with open(filepath) as file:
        content = [line.rstrip() for line in file]
    return content


def group(data: List[str], delimiter: str = "") -> List[str]:
    """
    Parses the raw data into grouped lists

    :param data: The raw loaded dataset
    :param delimiter: Delimiting char
    :return: Grouped entries
    """
    groupby = itertools.groupby(data, lambda z: z == delimiter)
    grouped_data = [list(y) for x, y in groupby if not x]
    return [" ".join(group) for group in grouped_data]
