import math

from utils import MapEnvironment, get_data

if __name__ == "__main__":
    data = get_data()

    routes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    trees = []

    for route in routes:
        env = MapEnvironment(map_data=data)
        trees.append(env.execute(*route))

    print(f"{math.prod(trees)}")
