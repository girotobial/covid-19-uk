# base.py

from configparser import ConfigParser
from pathlib import Path
from abc import ABC, abstractmethod
from ..utils import AsDictionaryMixin


class ABCConfig(ABC, AsDictionaryMixin):
    def __str__(self):
        return self.to_dict().__str__()

    def __repr__(self):
        return self.to_dict().__repr__()

    @abstractmethod
    def read_file(self):
        pass

    @staticmethod
    def _open_config_file(path, section):
        # check if path is a pathlib object
        if not isinstance(path, Path):
            path = Path(path)

        # Make sure file exists
        if not path.is_file():
            raise ValueError(f'{path} not found')

        file_ = ConfigParser()
        file_.read(path)

        if section not in file_:
            raise ValueError(f'"{section}" section not found in ini file')

        config = file_[section]
        return config
