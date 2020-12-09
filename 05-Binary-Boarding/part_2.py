from utils.data_loader import load_data
from utils.seat_finder import BinaryBoarding

if __name__ == "__main__":
    data = load_data("./data/data.txt")

    results = set()

    for entry in data:
        model = BinaryBoarding(entry)
        results.add(model.seat_id)

    _range = set(list(range(min(results), max(results) + 1)))
    difference = _range.difference(results)

    print(f"The missing seat number is {list(difference)[0]}")
