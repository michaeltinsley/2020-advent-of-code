from utils import Passport, load_data, parse_dataset

if __name__ == "__main__":
    dataset = load_data("./data/data.txt")
    parsed_dataset = parse_dataset(dataset)

    num_valid = 0
    num_invalid = 0

    for entry in parsed_dataset:
        try:
            passport = Passport(validation=True, **entry)
            num_valid += 1
        except TypeError:
            num_invalid += 1

    print(f"{num_valid} valid passports, {num_invalid} invalid passports")
