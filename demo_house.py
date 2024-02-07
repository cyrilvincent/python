import csv
import pickle
import json

import demo_tuple

with open("data/house/house.csv") as f:
    reader = csv.DictReader(f)
    loyers = []
    surfaces = []
    loyers_per_m2 = []
    for row in reader:
        loyer = float(row["loyer"])
        surface = float(row["surface"])
        loyers.append(loyer)
        surfaces.append(surface)
        loyers_per_m2.append(loyer / surface)

    print(demo_tuple.min_max_mean(loyers))
    print(demo_tuple.min_max_mean(surfaces))
    print(demo_tuple.min_max_mean(loyers_per_m2))

    with open("data/house/house.pkl", "wb") as f:
        pickle.dump(loyers_per_m2, f)

    with open("data/house/house.pkl", "rb") as f:
        loyers_per_m2 = pickle.load(f)

    with open("data/house/house.json", "w") as f:
        json.dump(loyers_per_m2, f)

    with open("data/house/house.json", "r") as f:
        loyers_per_m2 = json.load(f)

# Lire le fichier data/house/house.csv (il est dans le zip)
# Afficher les loyers
# Créer la liste loyers et ajouter tous les loyers dedans
# Idem pour surfaces
# Afficher le loyer min, max, moyen
# Idem pour surface
# Bonus idem pur loyer_per_m2