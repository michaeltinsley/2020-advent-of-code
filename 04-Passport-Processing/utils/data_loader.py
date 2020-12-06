from typing import List, Dict

import itertools


FILEPATH = "./data/data.txt"


def load_data(filepath: str) -> List[str]:
    """
    Reads in the raw data file

    :param filepath: The path to the datafile
    :return: A list of strings
    """
    with open(filepath) as f:
        content = [line.rstrip() for line in f]
    return content


def parse(data: List[str], delimiter: str = "") -> List[str]:
    """
    Parses the raw data into grouped lists

    :param data: The raw loaded dataset
    :param delimiter: Delimiting char
    :return: Grouped entries
    """
    groupby = itertools.groupby(data, lambda z: z == delimiter)
    grouped_data = [list(y) for x, y in groupby if not x]
    return [" ".join(group) for group in grouped_data]


def split_entry(entry: str) -> Dict[str, str]:
    """
    Splits a given entry into a dictionary of parameters

    :param entry: An entry as a formatted string
    :return: A dictionary of key value pairs
    """
    entries = entry.split(" ")
    return {key: value for key, value in [entry.split(":") for entry in entries]}


def parse_dataset(dataset: List[str]) -> List[Dict[str, str]]:
    """
    Parses the given dataset into dictionaries

    :param dataset: The unparsed loaded data
    :return: The parsed dataset
    """
    parsed_data = parse(dataset, delimiter="")
    return [split_entry(entry) for entry in parsed_data]
