from typing import Dict, List

from utils.data_loader import group, load_data


def reduce(grouped_data: List[str]) -> List[Dict[str, int]]:
    """
    Reduces the grouped data to a single list with no whitespace
    """
    return ["".join(set(entry.replace(" ", ""))) for entry in grouped_data]


if __name__ == "__main__":
    data = load_data("./data/data.txt")
    grouped_data = group(data)
    reduced_data = reduce(grouped_data)
    total = sum([len(entry) for entry in reduced_data])

    print(f"The sum of the counts is {total}")
