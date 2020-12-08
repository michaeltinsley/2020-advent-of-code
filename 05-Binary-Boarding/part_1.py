from utils.data_loader import load_data
from utils.seat_finder import BinaryBoarding

if __name__ == "__main__":
    data = load_data("./data/data.txt")

    results = []

    for entry in data:
        model = BinaryBoarding(entry)
        results.append(model.seat_id)

    print(f"The highest seat value is {max(results)}")
