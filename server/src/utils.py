from dataclasses import dataclass
from typing import Union
import toml
import sys


@dataclass()
class Config:
    PORT: int
    DBURL: str
    CLIENT_URL: str


config: Union[Config, None] = None


def get_config(path) -> Config:
    global config
    if config is None:
        try:
            with open(path, "r") as f:
                data = toml.load(f)
        except Exception:
            print("Invalid 'config.toml' configuration")
            sys.exit(-1)

        config = Config(
            PORT=data['server']['PORT'],
            DBURL=data['database']['DBURL'],
            CLIENT_URL=data['client']['URL'],
        )
    return config
