from typing import List, Tuple

FILEPATH = "./expense_report.txt"
TARGET = 2020


def expense_report_loader(filepath: str) -> List[int]:
    """
    Loads the data file and converts to a list of integers.

    :param filepath: The filepath of the data file
    :return: The loaded data as a list of integers
    """
    with open(filepath) as f:
        content = [int(line.rstrip()) for line in f]
    return content


def summation_calculator(target: int, possible_values: List[int]) -> Tuple[int, int]:
    """
    Returns the the values in a given list that sum to the given target.

    :param target: The integer summation value
    :param possible_values: A list of possible values
    :return: The two found values
    """
    possible_values.sort(reverse=True)

    for value in possible_values:
        target_bond = target - value

        if target_bond in possible_values:
            return value, target_bond

        possible_values.remove(value)


def product_calculator(*args: int) -> int:
    """
    Calculates the product of the given inputs.

    :param args: A set of input values
    :return: The product of the given values
    """
    value = 1
    for i in args:
        value *= i
    return value


if __name__ == "__main__":
    data = expense_report_loader(FILEPATH)
    value_pair = summation_calculator(TARGET, data)
    print(f"The entries are {value_pair[0]} and {value_pair[1]}")

    product = product_calculator(*value_pair)
    print(f"The product of these values is {product}")
