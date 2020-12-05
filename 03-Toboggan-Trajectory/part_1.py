from utils import get_data, MapEnvironment

if __name__ == "__main__":
    data = get_data()
    env = MapEnvironment(map_data=data)
    trees = env.execute(3, 1)
    print(f"{trees} trees hit")
