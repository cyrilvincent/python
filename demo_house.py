# with open("data/house/house.csv") as f:
#     with open("data/house/out.csv", "w") as g:
#         for row in f:
#             g.write(row)
import csv

with open("data/house/house.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        loyer = int(row["loyer"])
        surface = int(row["surface"])
        print(loyer / surface)