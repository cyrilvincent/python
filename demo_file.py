import csv
import numpy as np

surfaces = []
loyers = []
with open("data/house/house.csv") as f:
    # with open("data/house/out.csv", "w") as out:
    #     for row in f:
    #         out.write(row)

    reader = csv.DictReader(f, delimiter=",")
    for row in reader:
        loyer = int(row["loyer"])
        surface = int(row["surface"])
        loyers.append(loyer)
        surfaces.append(surface)
        # print(loyer / surface)

surfaces = np.array(surfaces)
loyers = np.array(loyers)

filter = (surfaces > 100) & (loyers > 1000)
print(filter)
print(loyers[filter] / surfaces[filter])



