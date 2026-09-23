# Créer la classe HouseRepository
# Créer les attributs non paramétrable surfaces, loyers = []
# Créer la méthode load(path) qui assigne surfaces et loyers
# Créer l'attribut loyer_m2 = []
# Créer la méthode compute_loyer_m2()
import csv
import pickle
import json

class HouseRepository:

    def __init__(self):
        self.loyers = []
        self.surfaces = []
        self.loyer_m2 = []

    def load(self, path: str):
        with open(path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                loyer = int(row["loyer"])
                surface = int(row["surface"])
                self.loyers.append(loyer)
                self.surfaces.append(surface)

    def compute_loyer_m2(self):
        for loyer, surface in zip(self.loyers, self.surfaces):
            self.loyer_m2.append(loyer / surface)

    def save_pickle(self, path):
        with open(path, "wb") as f:
            pickle.dump((self.loyers, self.surfaces), f)

    def save_json(self, path):
        with open(path, "w") as f:
            json.dump((self.loyers, self.surfaces), f, indent=2)

    def load_pickle(self, path):
        with open(path, "rb") as f:
            self.loyers, self.surfaces = pickle.load(f)
    def load_json(self, path):
        with open(path, "r") as f:
            self.loyers, self.surfaces = json.load(f)


if __name__ == '__main__':
    repo = HouseRepository()
    repo.load("data/house/house.csv")
    repo.save_pickle("data/house/house.pkl")
    repo.load_pickle("data/house/house.pkl")
    repo.save_json("data/house/house.json")
    repo.load_json("data/house/house.json")
    repo.compute_loyer_m2()
    print(repo.loyer_m2)



