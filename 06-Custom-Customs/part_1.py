from utils.data_loader import load_data, group, reduce


if __name__ == "__main__":
    data = load_data('./data/data.txt')
    grouped_data = group(data)
    reduced_data = reduce(grouped_data)
    total = sum([len(entry) for entry in reduced_data])

    print(f"The sum of the counts is {total}")
