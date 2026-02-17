import csv
import tp_tuple
import pickle

# with open("data/house/house.csv", "r") as f:
#     with open("data/house/house2.csv", "w") as w:
#         for row in f:
#             print(row.strip())
#             w.write(row)
#             row.split(",")
# print("End")
#
# with open("data/house/house.csv", "r") as f:
#     reader = csv.DictReader(f)
#     for row in reader:
#         print(int(row["loyer"])/int(row["surface"]))

# 1 load_csv(path) -> tuple[list[int], list[int]] # loyers et surfaces
# 2 for loyer, surface in zip(loyers, surfaces) Créer la liste loyer_m2
# 3 Afficher le loyer_m2 moyen

def load_csv(path: str, delimiter=",") -> tuple[list[int], list[int]]:
    with open(path, "r") as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        loyers = []
        surfaces = []
        for row in reader:
            loyers.append(int(row["loyer"]))
            surfaces.append(int(row["surface"]))
    return loyers, surfaces

if __name__ == '__main__':
    loyers, surfaces = load_csv("data/house/house.csv")
    loyers_m2 = [loyer / surface for loyer, surface in zip(loyers, surfaces)]
    print(tp_tuple.min_max_avg(loyers_m2))
    # with open("data/house/house_m2.pkl", "wb") as f:
    #     pickle.dump(loyers_m2, f)
    with open("data/house/house_m2.pkl", "rb") as f:
        loyers_m2 = pickle.load(f)
        print(loyers_m2)

