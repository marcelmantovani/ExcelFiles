import yaml


class IniConfig:

    def __init__(self) -> None:
        try:
            with open('util/config.yaml') as f:
                self.config = yaml.load(f, Loader=yaml.FullLoader)
        except IOError:
            print("Could not read file: config.yaml")