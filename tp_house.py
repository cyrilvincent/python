# Lire house.csv
# Créer les listes surfaces et loyers
# Créer la liste loyer_m2
# Appeler la fonction stats

import math
import csv
import my_module

print(f"pi: {math.pi:.2f}")

surfaces = []
loyers = []
loyers_m2 = []
with open("data/house/house.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        surface = int(row["surface"])
        loyer = int(row["loyer"])
        surfaces.append(surface)
        loyers.append(loyer)
        loyers_m2.append(loyer / surface)

print(my_module.stats(surfaces))
print(my_module.stats(loyers))
print(my_module.stats(loyers_m2))



