import csv


# with open("data/house/house.csv") as f:
#     with open("data/house/house2.csv", "w") as g:
#         for row in f:
#             print(row, end="")
#             g.write(row)

with open("data/house/house.csv") as f:
    reader = csv.DictReader(f,)
    for row in reader:
        print(int(row["loyer"]) / int(row["surface"]))
