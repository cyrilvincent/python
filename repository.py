import abc
from typing import List
import csv
import media
import pickle


class ARepository(metaclass=abc.ABCMeta):

    def __init__(self):
        self.medias: List[media.Media] = []

    @abc.abstractmethod
    def load(self, path: str): ...

    def get_by_price(self, price: float) -> List[media.Media]:
        return [m for m in self.medias if m.price <= price]

    def get_by_title(self, title: str) -> List[media.Media]:
        return [m for m in self.medias if title.upper() in m.title.upper()]

    def add(self, media_: media.Media):
        self.medias.append(media_)

    @abc.abstractmethod
    def save(self, path: str): ...


class PickleRepository(ARepository):

    def load(self, path: str):
        with open(path, "rb") as f:
            self.medias = pickle.load(f)

    def save(self, path: str):
        with open(path, "wb") as f:
            pickle.dump(self.medias, f)


class CSVRepository(ARepository):

    def load(self, path: str):
        with open(path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                title = row["title"]
                price = float(row["price"])
                b = media.Book(title, price)
                self.medias.append(b)

    def save(self, path: str):
        with open(path, "w") as f:
            f.write("title,price\n")
            for m in self.medias:
                f.write(f"{m.title},{m.price}\n")












# XML JSON