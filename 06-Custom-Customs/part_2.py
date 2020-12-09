from typing import List, Set

from utils.data_loader import group, load_data


def split_users(grouped_data: List[str]) -> List[List[str]]:
    """
    Group user groups into votes per person
    """
    return [value.split(" ") for value in grouped_data]


def find_common_values(split_data: List[List[str]]) -> List[List[str]]:
    """
    Calculates the intersection of common votes for each user group
    """
    group_common_votes = []
    for user_group in split_data:
        group_sets = [set(user) for user in user_group]
        intersection = set.intersection(*group_sets)
        group_common_votes.append(intersection)

    return group_common_votes


def common_value_summation(common_votes: List[Set[int]]) -> int:
    """
    Calculates the final summation of total number of common votes
    """
    return sum([len(values) for values in common_votes])


if __name__ == "__main__":
    data = load_data("./data/data.txt")
    grouped = group(data)
    split = split_users(grouped)
    grouped_common_votes = find_common_values(split)
    value_summation = common_value_summation(grouped_common_votes)
    print(f"The sum of the counts is {value_summation}")
