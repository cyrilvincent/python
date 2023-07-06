import csv
from dataclasses import dataclass


@dataclass
class Book:

    title: str
    price: float
    id: float

    def net_price(self):
        return self.price * 1.055

@dataclass
class HouseCsv:

    path : str

    def load(self):
        loyers = []
        surfaces = []
        with open(self.path) as file:
            reader = csv.DictReader(file)
            for row in reader:
                loyer = float(row['loyer'])
                surface = float(row["surface"])
                loyers.append(loyer)
                surfaces.append(surface)
        return loyers, surfaces

if __name__ == '__main__':
    b1 = Book("Python", 10, 123)
    print(f"Price: {b1.net_price():.2f}")
    h1 = HouseCsv("data/house/house.csv")
    loyers, surfaces = h1.load()
    print(loyers)