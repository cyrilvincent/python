import csv

# with open("data/house.csv") as f:
#     for row in f:
#         print(row, end='')
#     with open("data/toto.txt", "a") as f2:
#         f2.write("by cyril")

# print(content)

with open("data/house.csv") as f:
    reader = csv.DictReader(f)
    loyers = []
    surfaces = []
    for row in reader:
        loyer = int(row["loyer"])
        surface = int(row["surface"])
        print(loyer / surface)
        loyers.append(loyer)
        surfaces.append(surface)
    print(loyers)
    print(surfaces)
    print(min(loyers), max(loyers), sum(loyers) / len(loyers))

