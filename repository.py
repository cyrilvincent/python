import abc
from typing import List

import media


class ARepository(metaclass=abc.ABCMeta):

    def __init__(self):
        self.medias: List[media.Media] = []

    @abc.abstractmethod
    def load(self, path: str): ...

    @abc.abstractmethod
    def get_by_price(self, price: float) -> List[media.Media]: ...

    @abc.abstractmethod
    def get_by_title(self, title: str) -> List[media.Media]: ...

    @abc.abstractmethod
    def add(self, media_: media.Media): ...

    @abc.abstractmethod
    def save(self, path: str): ...


class PickleRepository(ARepository):
    pass

class CSVRepository(ARepository):
    pass

# XML JSON