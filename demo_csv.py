import csv
import pickle

with open("data/house/house.csv") as f:  # Read par défaut "r"
    reader = csv.DictReader(f, delimiter=",")
    loyer_m2 = []
    for row in reader:
        loyer = int(row["loyer"])
        surface = int(row["surface"])
        loyer_m2.append(loyer / surface)
    print(loyer_m2)
    print(sum(loyer_m2)/len(loyer_m2))

    # TP Créer un nouveau module house.py
    # Créer la classe House avec les attributs loyer et surface
    # Créer la méthode load(path) -> list[House]


class House:

    def __init__(self, loyer: int, surface: int):
        self.loyer = loyer
        self.surface = surface

    def loyer_m2(self) -> float:
        return self.loyer / self.surface

    def __repr__(self):
        return f"House: loyer={self.loyer}, surface={self.surface}"

    @staticmethod
    def load(path: str) -> list:
        with open(path) as f:
            reader = csv.DictReader(f, delimiter=",")
            houses = []
            for row in reader:
                loyer = int(row["loyer"])
                surface = int(row["surface"])
                house = House(loyer, surface)
                houses.append(house)
        return houses
    
    
    
if __name__ == "__main__":
    houses: list[House] = House.load("data/house/house.csv")
    print([h.loyer_m2() for h in houses])

    with open("data/house/house.pkl", "wb") as f:
        pickle.dump(houses, f)

    with open("data/house/house.pkl", "rb") as f:
        houses = pickle.load(f)

