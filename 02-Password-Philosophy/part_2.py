from typing import List

from utils import Row, load_data, parse_data

FILEPATH = "./data.txt"


def validate_entry(entry: Row) -> bool:
    """
    Validates a given entry

    :param entry: A populated Row object
    :return: True if entry is valid, False otherwise
    """
    validation_1 = (entry.password[entry.min - 1] == entry.letter) and (
        entry.password[entry.max - 1] != entry.letter
    )
    validation_2 = (entry.password[entry.min - 1] != entry.letter) and (
        entry.password[entry.max - 1] == entry.letter
    )

    if validation_1 or validation_2:
        return True
    else:
        return False


def run_validation(parsed_data: List[Row]) -> List[bool]:
    """
    Runs validation on the full dataset

    :param parsed_data:
    :return:
    """
    return [validate_entry(row) for row in parsed_data]


if __name__ == "__main__":
    data = load_data(FILEPATH)
    parsed_data = parse_data(data)
    validated_data = run_validation(parsed_data)
    total_rows = len(validated_data)
    total_valid_rows = sum(validated_data)
    total_invalid_rows = total_rows - total_valid_rows

    print(f"Total valid rows is {total_valid_rows}")
    print(f"Total invalid rows is {total_invalid_rows}")
