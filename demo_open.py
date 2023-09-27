# f = open("data/house/house.csv")
# for row in f:
#     print(row)
#
# f = open("data/nouveau.txt", "w")
# for i in range(10):
#     f.write(f"Toto{i}\n")
#
# with open("data/house/house.csv") as f:
#     for row in f:
#         print(row)

import csv
with open("data/house/house.csv") as f:
    reader = csv.DictReader(f)
    loyers = []
    for row in reader:
        loyer = float(row["loyer"])
        surface = float(row["surface"])
        loyers.append(loyer)
    print(loyers)

