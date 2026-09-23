# Créer la classe HouseRepository
# Créer les attributs non paramétrable surfaces, loyers = []
# Créer la méthode load(path) qui assigne surfaces et loyers
# Créer l'attribut loyer_m2 = []
# Créer la méthode compute_loyer_m2()
import csv

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

    def save_pickle(self):
        # sauvegarder les loyers et surfaces
        # pickle.dump((x, y), f)
        # pass

        # load_pickle(path)
        # save_json module json dump(indent=2)
        # load_json
        pass


if __name__ == '__main__':
    repo = HouseRepository()
    repo.load("data/house/house.csv")
    repo.compute_loyer_m2()
    print(repo.loyer_m2)

