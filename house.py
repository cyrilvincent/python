import csv

class House:

    def __init__(self, path):
        self.path = path
        self.db = []
        with open(self.path) as f:
            reader = csv.DictReader(f)
            for row in reader:
                self.db.append((int(row["loyer"]), int(row["surface"])))

    def get_loyer_max(self):
        return max([row[0] for row in self.db])

    def get_loyerm2_max(self):
        return max([row[0] / row[1] for row in self.db])

    # def get_loyer_max(self):
    #     with open(self.path) as f:
    #         max = 0
    #         reader = csv.DictReader(f)
    #         for row in reader:
    #             loyer = int(row["loyer"])
    #             if loyer > max:
    #                 max = loyer
    #     return max
    #
    # def get_loyerm2_max(self):
    #     with open(self.path) as f:
    #         max = 0
    #         reader = csv.DictReader(f)
    #         for row in reader:
    #             loyer = int(row["loyer"]) / int(row["surface"])
    #             if loyer > max:
    #                 max = loyer
    #     return max

if __name__ == '__main__':
    house = House("data/house.csv")
    max2 = house.get_loyer_max()
    print(max2)
    max2 = house.get_loyerm2_max()
    print(max2)