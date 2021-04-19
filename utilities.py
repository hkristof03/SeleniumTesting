import yaml


def load_yaml(path: str) -> dict:
    with open(path, 'r') as file:
        data = yaml.load(file, Loader=yaml.Loader)
    return data
