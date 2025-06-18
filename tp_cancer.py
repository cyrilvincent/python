# Charger data/cancer/data.csv
# Créer les listes radius_worsts, area_worsts, ids, diagnosis
# Afficher la moyenne des listes
import csv
import pickle

class CancerService:

    def __init__(self):
        self.ids = []
        self.diagnosis = []
        self.radius = []
        self.areas = []
        self.radius0 = []
        self.radius1 = []

    def load(self, path):
        with open(path) as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.ids.append(int(row["id"]))
                diagnosis = int(row["diagnosis"])
                self.diagnosis.append(diagnosis)
                self.radius.append(float(row["radius_worst"]))
                self.areas.append(float(row["area_worst"]))
                if diagnosis == 0:
                    self.radius0.append(float(row["radius_worst"]))
                else:
                    self.radius1.append(float(row["radius_worst"]))

    def avg(self, l: list[float]) -> float:
        return sum(l) / len(l)

    def save(self):
        with open("data/cancer/data.pkl", "wb") as f:
            pickle.dump(self, f)

    def load_pickle(self):
        with open("data/cancer/data.pkl", "rb") as f:
            self = pickle.load(f)



if __name__ == '__main__':
    c = CancerService()
    c.load("data/cancer/data.csv")
    c.save()
    c.load_pickle()
    print(c.ids)
    print(c.avg(c.radius))
    print(c.avg(c.radius0))
    print(c.avg(c.radius1))


