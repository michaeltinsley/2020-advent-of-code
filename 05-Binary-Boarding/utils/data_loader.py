from typing import List

FILEPATH = "./data/data.txt"


def load_data(filepath: str = FILEPATH) -> List[str]:
    """
    Reads in the raw data file

    :param filepath: The path to the datafile
    :return: A list of strings
    """
    with open(filepath) as f:
        content = [line.rstrip() for line in f]
    return content
